import pytest

from fixture.application import Application
from models.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_create_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group('test name', 'test header', 'test footer'))
    app.session.logout()


def test_create_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group("", "", ""))
    app.session.logout()
