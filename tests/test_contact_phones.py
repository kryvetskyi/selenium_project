import re


def remove_special_symbols(s):
    pattern = r"[^\w\s]"
    return re.sub(pattern, "", s)


def merge_phones_as_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: remove_special_symbols(x),
                                                   filter(lambda x: x is not None,
                                                   [contact.home_phone, contact.mobile_phone, contact.work_phone]))))


def test_contact_phones_on_view_page(app):
    contact_from_home_page = app.contact.get_contact_list()[2]
    contact_from_view_page = app.contact.get_contact_info_from_view_page(3)
    assert contact_from_home_page.phones_from_home_page == merge_phones_as_on_home_page(contact_from_view_page)


def test_contact_phones_on_edit_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(3)

    assert contact_from_home_page.phones_from_home_page == merge_phones_as_on_home_page(contact_from_edit_page)

