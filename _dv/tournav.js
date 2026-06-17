// Tour navigation — prev / next linear flow + a "Continue" jump to the next unread node.
// Called at the bottom of each node via:  ```dataviewjs\n dv.view("_dv/tournav")\n```
const cur = dv.current();
let lists = cur.lists ?? [];
if (!Array.isArray(lists)) lists = [lists];

const base = (l) => String(l.path ?? l).split("/").pop().replace(/\.md$/, "");

let members, tourBase;
if (lists.length) {
  tourBase = base(lists[0]);
  members = dv.pages('"concepts"').where(p => {
    let ls = p.lists ?? []; if (!Array.isArray(ls)) ls = [ls];
    return ls.some(l => base(l) === tourBase);
  });
} else {
  tourBase = `${cur.category}-core`;
  members = dv.pages('"concepts"').where(p =>
    p.category === cur.category && (!p.lists || p.lists.length === 0));
}

const arr = members.sort(p => p.tour_order ?? 0, "asc").array();
const total = arr.length;
const readCount = arr.filter(p => p.read === true).length;
const idx = arr.findIndex(p => p.file.path === cur.file.path);
const prev = idx > 0 ? arr[idx - 1] : null;
const next = (idx >= 0 && idx < total - 1) ? arr[idx + 1] : null;
const nextUnread = arr.find(p => p.read !== true && p.file.path !== cur.file.path);

const tourLink = dv.fileLink("tours/" + tourBase);
const row = [
  prev ? `◀ ${prev.file.link}` : "　",
  `**Tour:** ${tourLink}  (${readCount}/${total})`,
  next ? `${next.file.link} ▶` : "　",
];
dv.paragraph(row.join("　·　"));
if (nextUnread) dv.paragraph(`▶▶ **Continue:** ${nextUnread.file.link}`);
else dv.paragraph("🎉 You've read everything in this tour.");
