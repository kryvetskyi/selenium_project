
def test_delete_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.delete_first_group()
    app.session.logout()


def test_delete_group_by_index(app):
    app.session.login(username="admin", password="secret")
    app.group.delete_group_by_index(2)
    app.session.logout()
