const data = window.AEGIS_INJECTS || [];
const q = document.querySelector('#q');
const dim = document.querySelector('#dim');
const cards = document.querySelector('#cards');
const stats = document.querySelector('#stats');

[...new Set(data.map(x => x.dimension))].sort().forEach(d => {
  const o = document.createElement('option'); o.value = d; o.textContent = d; dim.appendChild(o);
});
function addText(parent, tag, text, className) {
  const el = document.createElement(tag); if (className) el.className = className;
  el.textContent = String(text ?? ''); parent.appendChild(el); return el;
}
function render() {
  const term = q.value.toLowerCase();
  const rows = data.filter(x => (!dim.value || x.dimension === dim.value) && JSON.stringify(x).toLowerCase().includes(term));
  stats.textContent = `${rows.length} of ${data.length} disclosed injects`;
  cards.replaceChildren();
  rows.forEach(x => {
    const article=document.createElement('article'); article.className='card'; article.tabIndex=0;
    addText(article,'span',x.dimension,'tag'); article.append(' '); addText(article,'span',x.id,'id');
    addText(article,'h3',x.title); addText(article,'p',x.scenario); addText(article,'div',`Evidence: ${x.evidence}`,'evidence');
    cards.appendChild(article);
  });
}
q.addEventListener('input',render); dim.addEventListener('change',render); render();
