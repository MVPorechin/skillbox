from dataclasses import dataclass, asdict


@dataclass
class User:
    name: str
    age: int

    def get_name(self):
        print(self.name)


class UserHandle:
    def __init__(self, name, age):
        self.user = User(name, age)

    def get_dataclass(self):
        return asdict(self.user)

    def edit(self, key, value):
        self.user.__dict__[key] = value
