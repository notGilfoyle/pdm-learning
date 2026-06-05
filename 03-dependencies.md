# Phase 3 — Managing Dependencies (Theory + Practical)

**Goal:** Add and remove packages the pdm way, understand dependency **groups**, and learn what
`pdm.lock` is for and how `install`/`sync` use it.

---

## Theory

### `pdm add` does three things at once

```bash
pdm add requests
```

1. **Resolves** `requests` *and* everything it needs (transitive deps) into a consistent set.
2. **Writes** the direct dep into `pyproject.toml` under `[project] dependencies`.
3. **Updates** `pdm.lock` with the exact pinned full tree, and **installs** into the venv.

Compare that to pip, where you'd `pip install requests` then manually `pip freeze`. pdm keeps
intent (`pyproject.toml`) and the locked result (`pdm.lock`) in sync automatically.

### Version specifiers

When you `pdm add requests`, pdm records something like `requests>=2.32.0`. Common specifiers:

- `>=2.32.0` — at least this version (pdm's default; allows compatible upgrades).
- `==2.32.0` — exactly this version (pin hard).
- `~=2.32.0` — "compatible release": `>=2.32.0, <2.33.0`.
- `>=2.0,<3.0` — a range.

You can request one explicitly: `pdm add "requests==2.32.3"`.

### Dependency groups: runtime vs dev

Not every dependency should ship with your app. Test runners (`pytest`), linters (`ruff`),
formatters — these are **development** tools. pdm keeps them in a separate **group** so they
don't pollute your runtime dependencies.

- Runtime: `pdm add requests`
- Dev group: `pdm add -dG dev pytest`
  - `-d` = development dependency, `-G dev` = put it in a group named `dev`.

Dev deps land under `[tool.pdm.dev-dependencies]` (or `[dependency-groups]`), **not** in
`[project] dependencies`. When someone installs your app for production, they can skip dev deps.

### `pdm.lock`, `pdm install`, and `pdm sync`

- **`pdm.lock`** — the exact, pinned, hashed full dependency tree. **Commit this to git.**
- **`pdm install`** — reads the lock (creating/refreshing it if needed) and makes your venv
  match: installs your project + locked deps. This is the command a teammate runs after cloning.
- **`pdm sync`** — installs *from the existing lock* without re-resolving. Makes the env exactly
  match the lockfile (can also remove extras with `--clean`).
- **`pdm lock`** — re-resolve and rewrite `pdm.lock` without installing.
- **`pdm update`** — upgrade deps to newer allowed versions and refresh the lock.

> Reproducibility in practice: clone a repo → `pdm install` → you get the **identical**
> environment the author had, because `pdm.lock` pins everything.

---

## Practical

Work inside `myapp/`:

```bash
cd /Users/roshan/code/pdm-learning/myapp
```

### 1. Add a runtime dependency

```bash
pdm add requests
```

Now inspect what changed:

```bash
cat pyproject.toml        # requests should appear under [project] dependencies
```

Open `pdm.lock` and skim it — notice it lists `requests` **plus** `urllib3`, `certifi`,
`charset-normalizer`, `idna`, each pinned to an exact version with hashes:

```bash
grep -A1 'name = ' pdm.lock | head -40
```

### 2. Add a dev dependency

```bash
pdm add -dG dev pytest
```

Check that pytest went into the **dev** group, not runtime:

```bash
cat pyproject.toml        # look for [tool.pdm.dev-dependencies] or [dependency-groups]
```

### 3. List what's installed

```bash
pdm list            # full table of installed packages
pdm list --tree     # dependency tree — see requests' children
```

### 4. Remove a dependency

Add something throwaway, then remove it, to see the round trip:

```bash
pdm add rich
pdm remove rich
```

Confirm `rich` is gone from both `pyproject.toml` and `pdm.lock`.

### 5. Simulate a fresh clone (the reproducibility payoff)

```bash
pdm install         # makes the venv match pyproject.toml + pdm.lock
```

This is the single command anyone needs after cloning your repo. No manual venv, no
`pip install -r requirements.txt`, no drift.

---

## What just happened

- `pdm add` resolved, recorded, locked, and installed — all in one step.
- Dev tools (`pytest`) are isolated in their own group.
- `pdm.lock` now guarantees a reproducible environment; `pdm install` rebuilds it anywhere.

> Commit:
> ```bash
> cd /Users/roshan/code/pdm-learning
> git add .
> git commit -m "Phase 3: add requests + pytest, lockfile"
> ```

---

## ✅ Checkpoint (see [EXERCISES.md](EXERCISES.md) Phase 3)

- `requests` is under `[project] dependencies`; `pytest` is in the dev group.
- You can point to where transitive deps (e.g. `urllib3`) appear — in `pdm.lock`, not `pyproject.toml`.
- You can explain the difference between `pdm install` and `pdm sync`.

Next: **[Phase 4 → Running code & scripts](04-running-code.md)**.
