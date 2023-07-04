from models.group import Group


def test_modify_first_group(app):
    groups_before = app.group.get_all_groups()
    group = Group(name='New modified group name')
    group.id = groups_before[0].id
    app.group.modify_first_group(group)
    groups_after = app.group.get_all_groups()
    assert len(groups_after) == len(groups_before), "Groups list are not equal"
    groups_before[0] = group
    assert sorted(groups_before, key=Group.id_or_max) == sorted(groups_after, key=Group.id_or_max)


def test_modify_group_header(app):
    groups_before = app.group.get_all_groups()
    group = Group(name='New modified group name')
    group.id = groups_before[0].id
    app.group.modify_first_group(group)
    groups_after = app.group.get_all_groups()
    assert len(groups_after) == len(groups_before), "Groups list are not equal"
    groups_before[0] = group
    assert sorted(groups_before, key=Group.id_or_max) == sorted(groups_after, key=Group.id_or_max)
