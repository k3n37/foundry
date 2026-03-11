# foundry

Foundational engineering exercises and reference implementations for the wider `k3n37` ecosystem.

## Why this repo exists

Every stronger platform repo in this ecosystem depends on fundamentals: algorithms, complexity analysis, data representation, debugging habits, and systems thinking. `foundry` is the place where those building blocks live in a focused, reusable form.

## Role in the ecosystem

- Upstream foundation for `kernel`
- Feeds reasoning patterns into `mesh`
- Supports architecture quality in `orbit`

## Current status

Early active lab with starter notes, reference problems, and a small runnable implementation.

## What good looks like

- Clear problem statements and tradeoff notes
- Small but correct implementations
- Reusable reference material for other repos
- No filler or “leetcode dump” feel

## Tech stack

- Python 3.12
- `pytest`
- Markdown docs

## Folder structure

```text
foundry/
├── docs/
│   └── notes.md
├── src/
│   └── foundations_lab/
│       ├── __init__.py
│       └── binary_search.py
├── tests/
│   └── test_binary_search.py
├── .editorconfig
├── .gitignore
├── README.md
└── ROADMAP.md
```

## Getting started

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pytest
pytest
```

## Roadmap

See [ROADMAP.md](./ROADMAP.md).

## Related repositories

- `kernel`: more focused problem and pattern catalog
- `mesh`: applies these fundamentals to concurrency and coordination
- `orbit`: downstream flagship platform that benefits from this repo’s rigor

## Future direction

Expand this repo carefully into a curated foundations library: memory models, network basics, concurrency primitives, and debugging case notes.
