import pytest

from fixture.application import Application

fixture = None


@pytest.fixture
def app():
    global fixture
    if fixture is None or (not fixture.is_valid()):
        fixture = Application()

    fixture.session.ensure_login(username="admin", password="secret")

    yield fixture


@pytest.fixture(scope="session", autouse=True)
def logout_and_destroy(request):
    fixture = Application()

    def finalizer():
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(finalizer)
    yield fixture
