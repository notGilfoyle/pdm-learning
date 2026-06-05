import requests


def get_github_zen() -> str:
    """Fetch GitHub's 'zen' one-liner — a quick way to prove requests works."""
    resp = requests.get("https://api.github.com/zen", timeout=10)
    resp.raise_for_status()
    return resp.text


if __name__ == "__main__":
    print(get_github_zen())