from models.group import Group


def test_modify_first_group(app):
    app.group.modify_first_group(Group(name='New name'))


def test_modify_group_header(app):
    app.group.modify_first_group(Group(header='New header'))
