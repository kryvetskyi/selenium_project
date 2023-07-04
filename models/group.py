from dataclasses import dataclass
from sys import maxsize


@dataclass
class Group:
    name: str = None
    header: str = None
    footer: str = None
    id: str = None

    def __repr__(self):
        return f'Group(name={self.name}, id={self.id})'

    def __eq__(self, other):
        return isinstance(other, Group) and self.name == other.name \
            and (self.id == other.id or self.id is None or other.id is None)

    def __hash__(self):
        return hash(self.id)

    def id_or_max(self):
        return int(self.id) if self.id else maxsize
