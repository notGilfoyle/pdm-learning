from app import get_github_zen


def test_offline_logic():
    # A trivial unit test that doesn't hit the network —
    # just proves pytest runs inside pdm's env and can import your module.
    assert isinstance("hello", str)


def test_function_exists():
    assert callable(get_github_zen)