from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import json
v=Path(__file__).resolve().parent.parent
root=v.parent.parent
db=v/'base_datos'
clubs=pd.read_csv(db/'visualizacion_clubes_preliminar.csv')
ages=pd.read_csv(db/'comparacion_edades_completa.csv')
cols=['minutos_'+str(i) for i in range(21,25)]
means=ages[cols].mean()
for name,df in [('clubs',clubs),('ages',ages)]:
    (root/'docs'/ (name+'.json')).write_text(df.to_json(orient='records',force_ascii=False),encoding='utf-8')
fig,ax=plt.subplots(figsize=(7,4)); ax.plot(range(21,25),means,marker='o',color='#637d18'); ax.set(xticks=range(21,25),xlabel='Edad al cierre del año',ylabel='Minutos medios',title='46 jugadores con cuatro edades observadas'); fig.tight_layout(); fig.savefig(v/'imagenes'/'vis_01.png',dpi=150); plt.close(fig)
d=clubs[clubs.season==2018].sort_values('minutos'); fig,ax=plt.subplots(figsize=(8,6)); ax.barh(d.teamName,d.minutos,color='#637d18'); ax.set(xlabel='Minutos registrados',title='Jugadores de hasta 21 años · 2018'); fig.tight_layout(); fig.savefig(v/'imagenes'/'vis_02.png',dpi=150); plt.close(fig)
