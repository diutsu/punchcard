# Frank

Personal AI agent **skills library** and **v2 project documentation templates**, packaged for distribution via `npx skills`.

Repository: `https://github.com/diutsu/Frank`

---

## Repository Structure

```text
Frank/
├── skills/                   # Distributable agent skills (discovered by npx skills)
│   ├── code-discipline/      # Anti-slop code rules, module boundaries, & comment rules
│   ├── code-task/            # Sub-agent code step execution & structured report contract
│   ├── data-integrity/       # Idempotency, safe migrations, & financial/domain math rules
│   ├── debugging-method/     # Root-cause-first debugging protocol (reproduce -> isolate -> fix)
│   ├── do-task/              # Two-gate task execution workflow (v2 doc paths)
│   ├── docs-management/      # v2 frontmatter, subfolder taxonomy, & anti-accretion rules
│   ├── external-research/    # Web/vendor research protocol producing docs/investigations/
│   ├── handle-comments/      # [COMMENT] handler routing open doubts to Decision gates
│   ├── internal-research/    # Codebase/DB investigation protocol producing docs/investigations/
│   ├── migrate-project-docs/ # Convert flat legacy docs/ or stabilize a prototype
│   ├── operate-and-diagnose/ # CLI/server run & diagnose protocol
│   ├── operator-instructions/# Run queue + Decision gates + Binary Exit Rule
│   ├── progress-log/         # Curated 1-line project milestone log
│   ├── research-methodology/ # Epistemic hygiene, source tiers, & numerical discipline
│   ├── research-to-plan/     # 150-line capped plans with phase roll-forward
│   ├── skill-maintenance/    # Authoring, splitting, & auditing skills (tier DAG + CommonMark)
│   ├── ui-ux-discipline/     # Intentional UI states, hierarchy, & accessibility baseline
│   ├── validation-and-qa/    # Test pyramid, real-behavior verification, & pre-done checklist
│   └── write-docs/           # Technical prose, README/API/Changelog templates, & ADR shapes
├── doc-templates/            # Canonical starter template for new/migrated side projects
│   ├── CLAUDE.md             # Target project instructions (prototype -> structured stages)
│   └── docs/                 # Target project v2 documentation tree
└── docs/                     # Meta-documentation for the Frank repository itself
```

---

## Installing Skills in Any Environment

Install all skills (or specific skills) from this repository using `npx skills`:

```bash
# Install all skills from Frank
npx skills add https://github.com/diutsu/Frank

# Install a single skill
npx skills add https://github.com/diutsu/Frank --skill docs-management
```

---

## Bootstrapping a Side Project with `doc-templates/`

Copy `doc-templates/` into a new project root, or run `/migrate-project-docs` inside an existing project to transition it into the v2 documentation layout:

```bash
cp -rn doc-templates/* /path/to/your-project/
```
