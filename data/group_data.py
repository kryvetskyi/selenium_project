import random
import string

from models.group import Group


def random_string(prefix, max_len):
    text = string.ascii_letters + string.digits + " " * 10 + string.punctuation
    return prefix + ''.join(random.choice(text) for _ in range(random.randrange(max_len)))


test_data = [Group(name="", header="", footer="")] + [
    Group(name=random_string('name', 10), header=random_string('header', 10), footer=random_string('footer', 10))
    for i in range(5)]