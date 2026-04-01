import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--target-browser",
        action="store",
        default=None,
        help="Browser to run tests on: chromium, firefox, webkit",
    )


@pytest.fixture(params=["chromium", "firefox", "webkit"])
def target_browser(request):
    name = request.config.getoption("--target-browser")
    if name and request.param != name:
        pytest.skip(f"Skipping {request.param}, running only {name}")
    return request.param
