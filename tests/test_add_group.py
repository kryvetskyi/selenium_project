import pytest
import random
import string

from models.group import Group


def random_string(prefix, max_len):
    text = string.ascii_letters + string.digits + " " * 10 + string.punctuation
    return prefix + ''.join(random.choice(text) for _ in range(random.randrange(max_len)))


test_data = [Group(name="", header="", footer="")] + [
    Group(name=random_string('name', 10), header=random_string('header', 10), footer=random_string('footer', 10))
    for i in range(5)]


@pytest.mark.parametrize("group", test_data, ids=[repr(x) for x in test_data])
def test_create_group_parametrized(app, group):
    groups_before = app.group.get_all_groups()
    app.group.create(group)
    groups_after = app.group.get_all_groups()
    assert len(groups_before) + 1 == app.group.count(), "Group was not created"
    groups_before.append(group)

    assert sorted(groups_before, key=Group.id_or_max) == sorted(groups_after, key=Group.id_or_max)
