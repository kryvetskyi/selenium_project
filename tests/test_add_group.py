
from models.group import Group


def test_create_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group('test name', 'test header', 'test footer'))
    app.session.logout()


def test_create_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group("", "", ""))
    app.session.logout()
