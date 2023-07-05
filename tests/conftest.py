import pytest

from fixture.application import Application

fixture = None


@pytest.fixture
def app(request):
    global fixture
    if fixture is None or (not fixture.is_valid()):
        browser = request.config.getoption("--browser")
        base_url = request.config.getoption("--base_url")
        fixture = Application(base_url, browser)

    fixture.session.ensure_login(username="admin", password="secret")

    yield fixture


@pytest.fixture(scope="session", autouse=True)
def logout_and_destroy(request):
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--base_url")
    fixture = Application(base_url, browser)

    def finalizer():
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(finalizer)
    yield fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Specify browser")
    parser.addoption("--base_url", action="store", default="http://localhost:8888/addressbook/", help="Specify url")
