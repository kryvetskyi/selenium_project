from dataclasses import dataclass


@dataclass
class Group:
    name: str = None
    header: str = None
    footer: str = None
