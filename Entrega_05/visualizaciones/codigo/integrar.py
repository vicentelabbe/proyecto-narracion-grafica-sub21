from pathlib import Path
import pandas as pd, zipfile, unicodedata, json, re
from collections import defaultdict
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'salida';OUT.mkdir(exist_ok=True)
Z=ROOT/'Datos_integrados_2015_2024.zip'
if not Z.exists(): Z=ROOT.parent/'Datos_integrados_2015_2024.zip'
rows=[]
for line in (ROOT/'historico.txt').read_text(encoding='utf-8').splitlines():
    if '|' not in line: season=line;continue
    r=line.split('|'); rows.append([season,*r])
h=pd.DataFrame(rows,columns=['temporada','fila_fbref','nombre','position','club','edad_fbref','anio_nacimiento','appearances','titularidades','minutos_individuales'])
for col in ['fila_fbref','edad_fbref','anio_nacimiento','appearances','titularidades','minutos_individuales']:h[col]=pd.to_numeric(h[col],errors='coerce').astype('Int64')
h['nationality']='Chile';h['origen']='FBref (tabla aportada por el equipo)';h['anio_cierre']=h.temporada.str[-4:].astype(int);h['edad_al_cierre_temporada']=h.anio_cierre-h.anio_nacimiento
h['torneo']=h.temporada.map({'2015-2016':'Apertura y Clausura','2016-2017':'Apertura y Clausura','2017':'Transición'})
h['fuente']=h.temporada.map(lambda s:f'https://fbref.com/en/comps/35/{s}/stats/{s}-Liga-de-Primera-Stats')
h['partidos_programados']=h.temporada.map({'2015-2016':30,'2016-2017':30,'2017':15})
h['pct_minutos_programados']=100*h.minutos_individuales/(90*h.partidos_programados)
h['estado_validacion']='Edad cronológica; elegibilidad reglamentaria no verificada'
h.loc[h.anio_nacimiento.isna(),'estado_validacion']='Nacimiento pendiente'
assert not h.duplicated(['temporada','fila_fbref']).any()
assert (h.minutos_individuales<=h.appearances*90).all()
assert (h.titularidades<=h.appearances).all()
assert (h.minutos_individuales>=0).all()
h.to_csv(OUT/'fbref_juveniles_y_casos_pendientes_2015_2017.csv',index=False)
h[h.anio_nacimiento.isna()].to_csv(OUT/'fbref_nacimiento_pendiente.csv',index=False)
y=h[h.edad_al_cierre_temporada.le(21).fillna(False)].copy()
y.to_csv(OUT/'juveniles_fbref_2015_2017.csv',index=False)
with zipfile.ZipFile(Z) as z:
    old=pd.read_csv(z.open('base_integrada_2015_2024.csv'),low_memory=False)
    allmod=pd.read_csv(z.open('base_con_estados_2018_2024.csv'),low_memory=False)
m=old[old.origen.eq('Classificacao Geral')].copy(); integrated=pd.concat([y,m],ignore_index=True,sort=False)
integrated.to_csv(OUT/'base_integrada_2015_2024.csv',index=False)
def norm(s):return ' '.join(re.sub(r'[^a-z0-9 ]',' ',unicodedata.normalize('NFKD',str(s)).encode('ascii','ignore').decode().lower()).split())
lookup=defaultdict(set); modinfo={}
for pid,g in allmod.groupby('playerId'):
    r=g.iloc[0]; birth=pd.to_datetime(r.get('fecha_nacimiento'),errors='coerce')
    if pd.isna(birth):continue
    first=norm(r.get('firstName','')); last=norm(r.get('lastName','')); name=norm(r.get('name',''))
    variants={first+' '+last,name}
    if first and last and first!='nan' and last!='nan':
        variants.update([first.split()[0]+' '+last.split()[0],first.split()[0]+' '+last,first+' '+last.split()[0]])
    for v in variants:
        if v.strip():lookup[(v.strip(),birth.year)].add(pid)
    modinfo[pid]=(str(r.get('name','')), ';'.join(map(str,sorted(g.season.dropna().astype(int).unique()))))
cr=[]
for (nombre,born),g in y.groupby(['nombre','anio_nacimiento']):
    candidates=sorted(lookup.get((norm(nombre),int(born)),set()))
    cr.append(dict(nombre=nombre,anio_nacimiento=born,temporadas_historicas=';'.join(sorted(g.temporada.unique())),estado_cruce='Candidato único: verificar identidad' if len(candidates)==1 else 'Ambiguo' if candidates else 'Sin coincidencia automática',playerId_candidatos=';'.join(str(int(p)) for p in candidates),nombre_api=';'.join(modinfo[p][0] for p in candidates),temporadas_observadas_2018_2024='; '.join(modinfo[p][1] for p in candidates)))
c=pd.DataFrame(cr);c.to_csv(OUT/'cruce_juveniles_2015_2024.csv',index=False)
y=y.merge(c,on=['nombre','anio_nacimiento'],how='left',validate='many_to_one')
summary=[]
for season,g in integrated.groupby('temporada',sort=False):
    hist=season in ['2015-2016','2016-2017','2017']; ids=g.nombre.astype(str)+'|'+g.anio_nacimiento.astype(str) if hist else g.playerId
    summary.append(dict(temporada=season,origen=g.origen.iloc[0],registros=len(g),jugadores_distintos=ids.nunique(),registros_con_minutos=g.minutos_individuales.notna().sum(),registros_sin_minutos=g.minutos_individuales.isna().sum(),minutos_registrados=g.minutos_individuales.sum(min_count=1)))
s=pd.DataFrame(summary);s.to_csv(OUT/'cobertura_integrada_2015_2024.csv',index=False)
print(s.to_string(index=False));print('Extraídos',h.groupby('temporada').size().to_dict(),'total integrado',len(integrated),'cruces',c.estado_cruce.value_counts().to_dict())
# Club/season and age summaries for historical source only
clubs=y.groupby(['temporada','club']).agg(registros=('fila_fbref','size'),jugadores=('nombre','nunique'),minutos=('minutos_individuales','sum')).reset_index();clubs.to_csv(OUT/'minutos_juveniles_clubes_2015_2017.csv',index=False)
ages=y.groupby(['temporada','edad_al_cierre_temporada']).agg(registros=('fila_fbref','size'),minutos=('minutos_individuales','sum')).reset_index();ages.to_csv(OUT/'minutos_juveniles_edades_2015_2017.csv',index=False)
(OUT/'historico_web.json').write_text(y[['temporada','nombre','club','position','anio_nacimiento','edad_al_cierre_temporada','minutos_individuales','fila_fbref','estado_cruce','temporadas_observadas_2018_2024','fuente']].to_json(orient='records',force_ascii=False),encoding='utf-8')
