
from models.group import Group


def test_create_group(app):
    app.group.create(Group('test name', 'test header', 'test footer'))


def test_create_empty_group(app):
    app.group.create(Group("", "", ""))
