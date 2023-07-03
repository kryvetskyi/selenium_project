import pytest

from application import Application
from group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_create_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group('test name', 'test header', 'test footer'))
    app.logout()


def test_create_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group("", "", ""))
    app.logout()
