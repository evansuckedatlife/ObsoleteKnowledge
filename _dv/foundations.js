// Foundations checker — renders this node's prerequisites with live read-status.
// Called from each node via:  ```dataviewjs\n dv.view("_dv/foundations")\n```
const cur = dv.current();
let reqs = cur.requires ?? [];
if (!Array.isArray(reqs)) reqs = [reqs];

if (reqs.length) {
  const items = reqs.map(l => {
    let p = null;
    try { p = dv.page(l); } catch (e) {}
    return { l, exists: !!p, read: !!(p && p.read === true) };
  });
  const unread = items.filter(i => i.exists && !i.read);

  const head = (unread.length === 0)
    ? "✅ **Foundations** — you've read all prerequisites."
    : `⚠️ **Foundations — read ${unread.length} of these first:**`;
  dv.paragraph(head);

  dv.list(items.map(i => {
    const mark = !i.exists ? "▫️" : (i.read ? "✅" : "⛔");
    const tail = (i.exists && !i.read) ? "  ←  **read this first**" : "";
    return `${mark} ${i.l}${tail}`;
  }));
}
