// Across-fields view — surfaces this node's links that point to OTHER categories,
// grouped by domain, so interdisciplinary connections are visible while reading.
// Called via:  ```dataviewjs\n dv.view("_dv/crosslinks")\n```
const cur = dv.current();
const myCat = cur.category;
const collect = (v) => { let a = v ?? []; if (!Array.isArray(a)) a = [a]; return a; };
const links = [...collect(cur.related), ...collect(cur.requires)];

const seen = new Set();
const byCat = {};
for (const l of links) {
  let p = null; try { p = dv.page(l); } catch (e) {}
  if (!p || !p.category || p.category === myCat) continue;
  const key = p.file.path;
  if (seen.has(key)) continue; seen.add(key);
  (byCat[p.category] ??= []).push(p.file.link);
}
const cats = Object.keys(byCat).sort();
if (cats.length) {
  const parts = cats.map(c => `*${c}*　${byCat[c].join(" · ")}`);
  dv.paragraph("🔗 **Across fields** —　" + parts.join("　|　"));
}
