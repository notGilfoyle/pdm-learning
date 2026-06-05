# Phase 2 — Your First PDM Project (Theory + Practical)

**Goal:** Create a real project with `pdm init`, understand every file it generates, and find
the virtualenv pdm built for you.

---

## Theory

### What `pdm init` does

`pdm init` is an interactive wizard. It asks a few questions and then scaffolds a standards-based
project. The important questions:

1. **Which Python interpreter?** pdm lists the ones it found (system, pyenv, etc.). Pick one.
2. **Library or application?** ("Is the project a library that will be uploaded to PyPI?")
   - **No / application** → for apps, scripts, services. Choose this for our course.
   - **Yes / library** → if you intend to package and publish to PyPI. Adds build config.
3. **Python requirement** — the minimum Python your project supports, e.g. `>=3.9`.
4. Name, version, license, author — metadata (sensible defaults are fine).

### Anatomy of `pyproject.toml`

After init you'll get a `pyproject.toml` roughly like:

```toml
[project]
name = "myapp"
version = "0.1.0"
description = "Default template for PDM package"
authors = [
    {name = "Roshan Sahu", email = "iamroshannn@gmail.com"},
]
dependencies = []            # ← your DIRECT runtime deps go here
requires-python = ">=3.9"
readme = "README.md"

[tool.pdm]
distribution = false         # false = application (not a publishable library)
```

- **`[project]`** is the **standard** (PEP 621) table — portable across tools.
- **`dependencies = []`** is where your direct deps will appear (you'll add them in Phase 3).
- **`[tool.pdm]`** holds pdm-specific settings.

### virtualenv vs `__pypackages__`

pdm can manage dependencies two ways:

- **Virtualenv** (default, what we use) — a classic isolated env. With `venv.in_project true`
  (set in Phase 1), it lives at `myapp/.venv/`.
- **`__pypackages__`** (PEP 582) — packages dropped into a local folder, no activation. More
  exotic; we skip it. Just know it exists.

---

## Practical

### 1. Create the sample project folder

```bash
cd /Users/roshan/code/pdm-learning
mkdir myapp
cd myapp
```

### 2. Run the wizard

```bash
pdm init
```

Answer the prompts:
- Pick your Python interpreter (the 3.9.6 one is fine).
- "Is the project a library...?" → **n** (it's an application).
- `requires-python` → accept `>=3.9` (or press enter for the default).
- Accept the defaults for name/version/author.

### 3. See what got created

```bash
ls -a
```

You should see at least:
- `pyproject.toml` — your project file (open and read it!)
- `.venv/` — the virtualenv pdm created (because of `venv.in_project true`)
- `src/` or a `myapp.py` / `README.md` depending on template — fine either way
- possibly `.pdm-python` — records which interpreter this project uses

```bash
cat pyproject.toml      # read your generated project file
```

### 4. Find and inspect the environment

```bash
pdm info          # shows project root, the Python interpreter, and the venv path
pdm info --env    # more environment detail
```

Notice the interpreter path points inside `.venv/`. **You never had to run
`python -m venv` or `source activate`** — pdm did it.

---

## What just happened

- You scaffolded a standards-based project with a single command.
- pdm created and linked a project-local virtualenv at `myapp/.venv/`.
- Your intent lives in `pyproject.toml`; there are no dependencies yet.

> Commit when you finish the phase:
> ```bash
> cd /Users/roshan/code/pdm-learning
> git add .
> git commit -m "Phase 2: pdm init for myapp"
> ```
> (Don't worry about `.venv/` showing up in git yet — we add a `.gitignore` in Phase 5.)

---

## ✅ Checkpoint (see [EXERCISES.md](EXERCISES.md) Phase 2)

- `myapp/pyproject.toml` exists and you can point to the `dependencies` line.
- `pdm info` shows an interpreter path inside `.venv/`.
- You can explain why you didn't need to run `python -m venv` yourself.

Next: **[Phase 3 → Managing dependencies](03-dependencies.md)**.
