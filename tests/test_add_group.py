import pytest

from data.group_data import test_data
from models.group import Group


@pytest.mark.parametrize("group", test_data, ids=[repr(x) for x in test_data])
def test_create_group_parametrized(app, group):
    groups_before = app.group.get_all_groups()
    app.group.create(group)
    groups_after = app.group.get_all_groups()
    assert len(groups_before) + 1 == app.group.count(), "Group was not created"
    groups_before.append(group)

    assert sorted(groups_before, key=Group.id_or_max) == sorted(groups_after, key=Group.id_or_max)
