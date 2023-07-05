from dataclasses import dataclass


@dataclass
class Contact:
    first_name: str = None
    last_name: str = None
    home_phone: str = None
    mobile_phone: str = None
    work_phone: str = None
    fax: str = None
    id: str = None
    phones_from_home_page: str = None

    def __repr__(self):
        return f"Contact(id={self.id}), name={self.first_name}, last name={self.last_name})"

    def __eq__(self, other):
        return isinstance(other, Contact) and (self.id is None or other.id is None or self.id == other.id) \
            and self.first_name == other.first_name and self.last_name == other.last_name

    def __hash__(self):
        return hash(self.id)
