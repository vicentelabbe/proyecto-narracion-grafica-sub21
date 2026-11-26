from pathlib import Path
import pandas as pd
import json
b=Path(__file__).resolve().parents[1]/'base_datos'
w=Path(__file__).resolve().parents[3]/'docs'
d=pd.read_csv(b/'base_integrada_2015_2024.csv')
assert not d.duplicated().any()
assert not (d.minutos_individuales<0).any()
assert not (d.minutos_individuales>d.appearances*90).any()
bad=d.edad_al_cierre_temporada.lt(0)|d.edad_al_cierre_temporada.gt(21)|d.edad_al_cierre_temporada.isna()
d[bad].to_csv(b/'exclusiones_edad.csv',index=False)
d=d[~bad].copy()
d.to_csv(b/'base_analitica_beta.csv',index=False)
g=d.groupby('temporada').minutos_individuales.agg(registros='size',con_minutos='count',minutos='sum').reset_index()
g['sin_minutos']=g.registros-g.con_minutos
g.to_csv(b/'cobertura_beta.csv',index=False)
club=d.groupby(['temporada','club'],dropna=False).minutos_individuales.agg(registros='size',con_minutos='count',minutos=lambda x:x.sum(min_count=1)).reset_index()
club['sin_minutos']=club.registros-club.con_minutos
club.to_csv(b/'clubes_beta.csv',index=False)
a=pd.read_csv(b/'comparacion_edades_completa.csv')
ages=pd.DataFrame({'edad':[21,22,23,24],'promedio':[a[f'minutos_{i}'].mean() for i in range(21,25)],'mediana':[a[f'minutos_{i}'].median() for i in range(21,25)],'n':len(a)})
ages.to_csv(b/'edades_beta.csv',index=False)
h=pd.read_csv(b/'juveniles_fbref_2015_2017.csv')
cols=['temporada','nombre','club','anio_nacimiento','minutos_individuales','pct_minutos_programados']
obj={'coverage':g,'clubs':club,'ages':ages,'history':h[cols]}
(w/'data.js').write_text('window.DATA='+json.dumps({k:json.loads(v.to_json(orient='records',force_ascii=False)) for k,v in obj.items()},ensure_ascii=False)+';',encoding='utf-8')
print(g.to_string(index=False))
