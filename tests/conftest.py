import pytest

from fixture.application import Application


fixture = None


@pytest.fixture
def app():
    global fixture
    if fixture is None:
        fixture = Application()
        fixture.session.login(username="admin", password="secret")

    # Check if session is valid
    if not fixture.is_valid():
        fixture = Application()
        fixture.session.login(username="admin", password="secret")

    yield fixture


@pytest.fixture(scope="session", autouse=True)
def logout_and_destroy(request):
    def finalizer():
        global fixture
        if fixture is None:
            fixture = Application()
        fixture.session.logout()
        fixture.destroy()

    request.addfinalizer(finalizer)
