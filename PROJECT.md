# Project: ObsoleteKnowledge Vault

## Architecture
- Concepts are stored in concepts/<folder>/<slug>.md where <folder> is the category name.
- MOC lists are stored in lists/<slug>.md.
- Globals: index.md maintains the master catalogue. BUILD-ORDER.md lists all topics to build.
- Verification: python _scratch/validate.py ensures 0 duplicates and correct formats.

## Milestones
| Phase | Name | Scope | Dependencies | Status |
|---|---|---|---|---|
| 3 | Science | Remaining 22 science topics | Phase 2 | PLANNED |
| 4 | Mathematics | 6 math topics | Phase 3 | PLANNED |
| 5 | Literature | 23 literature topics | Phase 4 | PLANNED |
| 6 | History | 52 history topics | Phase 5 | PLANNED |
| 7 | Music | 15 music topics | Phase 6 | PLANNED |
| 8 | Performance | 3 performance topics | Phase 7 | PLANNED |
| 9 | Visual Art | 11 art topics | Phase 8 | PLANNED |
| 10 | Geography | 6 geography topics | Phase 9 | PLANNED |
| 11 | Social Science | 9 social science topics | Phase 10 | PLANNED |
| 12 | Philosophy | 2 philosophy topics | Phase 11 | PLANNED |
| 13 | Popular Culture | 7 pop culture topics | Phase 12 | PLANNED |
| 14 | Sports | 6 sports topics | Phase 13 | PLANNED |
| 15 | Miscellaneous | 4 misc topics | Phase 14 | PLANNED |

## Interface Contracts
- Node structure must match AGENTS.md template: frontmatter, summary, you gotta know, connections, see also, footer.
- Basenames must be globally unique.
- Lists must list all member nodes, and member nodes must list all lists they belong to.
- Checkmarks ✅ must be prefix to completed topics in index.md.
