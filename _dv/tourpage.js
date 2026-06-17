// Tour page — live progress bar, Continue button, and an ordered checklist.
// Called from a tour note via:
//   ```dataviewjs
//   dv.view("_dv/tourpage", {list: "founders-of-religious-traditions", core: false, category: "religion"})
//   ```
const { list, core, category } = input ?? {};
const base = (l) => String(l.path ?? l).split("/").pop().replace(/\.md$/, "");

let members;
if (core) {
  members = dv.pages('"concepts"').where(p =>
    p.category === category && (!p.lists || p.lists.length === 0));
} else {
  members = dv.pages('"concepts"').where(p => {
    let ls = p.lists ?? []; if (!Array.isArray(ls)) ls = [ls];
    return ls.some(l => base(l) === list);
  });
}

const arr = members.sort(p => p.tour_order ?? 0, "asc").array();
const total = arr.length;
const read = arr.filter(p => p.read === true).length;
const pct = total ? Math.round((100 * read) / total) : 0;
const filled = Math.round(pct / 5);
const bar = "█".repeat(filled) + "░".repeat(20 - filled);

dv.paragraph(`**Progress:** ${read} / ${total}　\`${bar}\`　${pct}%`);
const nextUnread = arr.find(p => p.read !== true);
if (nextUnread) dv.paragraph(`▶▶ **Continue:** ${nextUnread.file.link}`);
else dv.paragraph(`🎉 **Tour complete — ${total}/${total} read!**`);

dv.table(["#", "✓", "Node"],
  arr.map((p, i) => [i + 1, p.read === true ? "✅" : "☐", p.file.link]));
