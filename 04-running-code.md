# Phase 4 — Running Code & Scripts (Theory + Practical)

**Goal:** Run Python code inside pdm's environment without manually activating a venv, write a
small app that uses `requests`, define a named script, and run a `pytest` test.

---

## Theory

### `pdm run` — use the project env without activating it

With plain venv you'd `source .venv/bin/activate` before running anything. pdm gives you a
shortcut that runs a command **inside the project's environment** automatically:

```bash
pdm run python app.py
pdm run pytest
```

`pdm run` finds the project's venv, puts it on the path for that one command, and runs it. No
activate/deactivate dance, and it always targets the *right* environment even if you have
several projects.

> You *can* still `source .venv/bin/activate` if you want a persistent shell, but `pdm run` is
> the idiomatic, mistake-proof way — especially in scripts and CI.

### Named scripts: `[tool.pdm.scripts]`

You can give common commands short names in `pyproject.toml`:

```toml
[tool.pdm.scripts]
start = "python app.py"
test = "pytest"
```

Then:

```bash
pdm run start
pdm run test
```

This is pdm's equivalent of npm's `package.json` "scripts" — it documents how to run your
project and removes "what was that long command again?" friction.

---

## Practical

Work inside `myapp/`:

```bash
cd /Users/roshan/code/pdm-learning/myapp
```

### 1. Write a tiny app that uses `requests`

Create `app.py`:

```python
import requests


def get_github_zen() -> str:
    """Fetch GitHub's 'zen' one-liner — a quick way to prove requests works."""
    resp = requests.get("https://api.github.com/zen", timeout=10)
    resp.raise_for_status()
    return resp.text


if __name__ == "__main__":
    print(get_github_zen())
```

Run it **through pdm** so it uses the venv where `requests` is installed:

```bash
pdm run python app.py
```

You should see a short proverb printed. (If offline, that's fine — the test below doesn't need
the network.)

### 2. Add a named script

Edit `pyproject.toml` and add:

```toml
[tool.pdm.scripts]
start = "python app.py"
test = "pytest"
```

Now run:

```bash
pdm run start
```

Same output, shorter command.

### 3. Write a test and run pytest

Create `test_app.py`:

```python
from app import get_github_zen


def test_offline_logic():
    # A trivial unit test that doesn't hit the network —
    # just proves pytest runs inside pdm's env and can import your module.
    assert isinstance("hello", str)


def test_function_exists():
    assert callable(get_github_zen)
```

Run the tests via pdm (pytest is in your dev group from Phase 3):

```bash
pdm run test
```

Expected: pytest collects and passes 2 tests.

---

## What just happened

- `pdm run` executed your code and your tests inside the project venv — no manual activation.
- Named scripts (`start`, `test`) documented how to run the project.
- You proved the dev-group `pytest` works without it being a runtime dependency.

> Commit:
> ```bash
> cd /Users/roshan/code/pdm-learning
> git add .
> git commit -m "Phase 4: app.py, scripts, tests"
> ```

---

## ✅ Checkpoint (see [EXERCISES.md](EXERCISES.md) Phase 4)

- `pdm run start` runs your app.
- `pdm run test` passes.
- You can explain why `pdm run python app.py` is safer than activating the venv by hand.

Next: **[Phase 5 → Reproducibility & git](05-reproducibility-git.md)**.
