import json
from pathlib import Path

import pytest

from fixture.application import Application

fixture = None
target = None


@pytest.fixture
def app(request):
    global fixture
    global target
    if fixture is None or not fixture.is_valid():
        browser = request.config.getoption("--browser")
        if target is None:
            conf_file = Path(__file__).resolve().parent.parent / "target.json"

            with open(conf_file) as f:
                target = json.load(f)

        fixture = Application(browser, target["base_url"])

    fixture.session.ensure_login(username=target["username"], password=target["password"])

    yield fixture


@pytest.fixture(scope="session", autouse=True)
def logout_and_destroy(request):
    browser = request.config.getoption("--browser")
    conf_file = Path(__file__).resolve().parent.parent / "target.json"
    with open(conf_file) as f:
        target = json.load(f)

    fixture = Application(browser, target["base_url"])

    def finalizer():
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(finalizer)
    yield fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Specify browser")
    parser.addoption("--target", action="store", default="target.json", help="Specify url")
