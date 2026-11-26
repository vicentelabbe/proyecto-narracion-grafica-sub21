const $ = id => document.getElementById(id);
const D = window.DATA;

const fmt = n => n == null ? 'Sin dato' : Math.round(n).toLocaleString('es-CL');

const neon = '#c6ff36';
const white = '#f5f5f0';
const muted = '#bcc1b4';
const gray = '#6e7268';
const bgTransparent = 'rgba(0,0,0,0)';

const baseLayout = {
  paper_bgcolor: bgTransparent,
  plot_bgcolor: bgTransparent,
  font: { family: 'IBM Plex Mono, monospace', color: white, size: 13 },
  margin: { l: 56, r: 22, t: 16, b: 58 },
  xaxis: {
    gridcolor: 'rgba(255,255,255,0.10)',
    zerolinecolor: 'rgba(255,255,255,0.18)',
    linecolor: 'rgba(255,255,255,0.18)',
    tickfont: { color: muted }
  },
  yaxis: {
    gridcolor: 'rgba(255,255,255,0.10)',
    zerolinecolor: 'rgba(255,255,255,0.18)',
    linecolor: 'rgba(255,255,255,0.18)',
    tickfont: { color: muted }
  },
  legend: { orientation: 'h', y: 1.12, x: 0, font: { color: muted } }
};

const config = { responsive: true, displayModeBar: false };

function draw(id, traces, extra = {}) {
  Plotly.react(id, traces, { ...baseLayout, ...extra }, config);
}

function opts(id, values) {
  values.forEach(v => $(id).add(new Option(v, v)));
}

const seasons = D.coverage.map(x => x.temporada);

function renderCoverage() {
  draw('coverage', [
    {
      type: 'bar',
      name: 'Con minutos',
      x: seasons,
      y: D.coverage.map(x => x.con_minutos),
      marker: { color: neon },
      hovertemplate: '%{x}<br>Con minutos: %{y}<extra></extra>'
    },
    {
      type: 'bar',
      name: 'Sin minutos',
      x: seasons,
      y: D.coverage.map(x => x.sin_minutos),
      marker: { color: gray },
      hovertemplate: '%{x}<br>Sin minutos: %{y}<extra></extra>'
    }
  ], {
    barmode: 'stack',
    height: 360,
    xaxis: { type: 'category', tickangle: -38, gridcolor: 'rgba(255,255,255,0.05)' },
    yaxis: { title: 'Registros', rangemode: 'tozero' }
  });

  const latest = D.coverage[D.coverage.length - 1];
  const first = D.coverage[0];
  $('coverage-summary').textContent = `La cobertura más reciente corresponde a ${latest.temporada}: ${latest.con_minutos} registros con minutos y ${latest.sin_minutos} sin minutos. En ${first.temporada}, en cambio, todos los casos recuperados tienen minutos.`;
}

opts('historical-season', ['Todas', ...seasons.slice(0, 3)]);
opts('club-season', seasons);
$('club-season').value = '2019';

function historical() {
  const q = $('search').value.toLocaleLowerCase();
  const s = $('historical-season').value;
  const order = $('order').value;

  let rows = D.history.filter(x =>
    (s === 'Todas' || x.temporada === s) &&
    (`${x.nombre} ${x.club}`).toLocaleLowerCase().includes(q)
  );

  rows.sort((a, b) => order === 'name'
    ? a.nombre.localeCompare(b.nombre)
    : (b.minutos_individuales - a.minutos_individuales)
  );

  $('result-count').textContent = `${rows.length} registros encontrados`;
  const body = $('historical-rows');
  body.replaceChildren();

  for (const row of rows) {
    const tr = document.createElement('tr');
    const values = [
      row.nombre,
      row.club,
      row.anio_nacimiento,
      fmt(row.minutos_individuales),
      `${row.pct_minutos_programados.toFixed(1)}%`
    ];

    values.forEach(value => {
      const td = document.createElement('td');
      td.textContent = value;
      tr.appendChild(td);
    });

    body.appendChild(tr);
  }
}

function clubs() {
  const season = $('club-season').value;
  const rows = D.clubs
    .filter(x => x.temporada === season)
    .sort((a, b) => (b.minutos ?? -1) - (a.minutos ?? -1));

  draw('clubs', [{
    type: 'bar',
    orientation: 'h',
    x: rows.map(x => x.minutos),
    y: rows.map(x => x.club + (x.sin_minutos ? ' *' : '')),
    marker: {
      color: rows.map((_, i) => i === 0 ? '#d7ff66' : neon),
      line: { color: 'rgba(255,255,255,0.1)', width: 1 }
    },
    text: rows.map(x => x.minutos == null ? 's/d' : fmt(x.minutos)),
    textposition: 'outside',
    cliponaxis: false,
    customdata: rows.map(x => x.sin_minutos),
    hovertemplate: '%{y}<br>%{x} minutos<br>Casos sin minutos: %{customdata}<extra></extra>'
  }], {
    height: Math.max(430, rows.length * 28 + 90),
    margin: { l: 165, r: 70, t: 8, b: 45 },
    xaxis: { title: 'Minutos registrados', rangemode: 'tozero' },
    yaxis: { automargin: true, autorange: 'reversed', gridcolor: 'rgba(255,255,255,0.03)' },
    showlegend: false
  });

  const top = rows[0];
  const missing = rows.filter(x => x.minutos == null).map(x => x.club);
  const missingText = missing.length ? ` Equipos sin dato completo: ${missing.join(', ')}.` : '';
  $('club-note').textContent = `${season}: ${top.club} lidera los minutos observados con ${fmt(top.minutos)} minutos registrados.${missingText} * Al menos un registro sin minutos. Compara siempre dentro de una misma temporada.`;
}

function ages() {
  const metric = $('metric').value;
  draw('ages', [{
    type: 'bar',
    x: D.ages.map(x => String(x.edad)),
    y: D.ages.map(x => x[metric]),
    marker: {
      color: [neon, '#b9ef2f', '#98ce2a', '#78a723'],
      line: { color: 'rgba(255,255,255,0.1)', width: 1 }
    },
    text: D.ages.map(x => fmt(x[metric])),
    textposition: 'outside',
    cliponaxis: false,
    hovertemplate: 'Edad %{x}<br>' + metric + ': %{y}<extra></extra>'
  }], {
    height: 350,
    margin: { l: 58, r: 24, t: 10, b: 55 },
    xaxis: { type: 'category', title: 'Edad al cierre del año' },
    yaxis: { title: 'Minutos', rangemode: 'tozero' },
    showlegend: false
  });
}

for (const id of ['historical-season', 'order']) {
  $(id).addEventListener('change', historical);
}
$('search').addEventListener('input', historical);
$('club-season').addEventListener('change', clubs);
$('metric').addEventListener('change', ages);

renderCoverage();
historical();
clubs();
ages();
