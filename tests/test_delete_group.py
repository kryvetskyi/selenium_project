from models.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="new group name"))
    groups_before = app.group.get_all_groups()
    app.group.delete_first_group()
    groups_after = app.group.get_all_groups()
    assert len(groups_before) - 1 == len(groups_after), "Group was not deleted"
    assert groups_before[1:] == groups_after
