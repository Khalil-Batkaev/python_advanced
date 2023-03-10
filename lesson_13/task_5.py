import json
from pathlib import Path

from lesson_13.task_3 import AccessError, LevelError
from task_4 import User


class Project:
    _users = set()

    def __init__(self):
        self.me = None

    def read_json(self, file: Path):

        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for lvl, value in data.items():
            for idx, password in value.items():
                self._users.add(User(int(lvl), int(idx), password))

        return self._users

    def sign_in(self, name, idx):
        spam_user = User(name=name, idx=idx, lvl=0)
        if spam_user not in self._users:
            raise AccessError(name, idx)
        for user in self._users:
            if user == spam_user:
                self.me = user
                return user

    def add_user(self, user: User):
        if user.lvl < self.me.lvl:
            raise LevelError(user.lvl, self.me.lvl)
        self._users.add(user)
        return user


if __name__ == '__main__':
    project = Project()
    res = project.read_json(Path('names.json'))
    print(f'{res = }')
    print(project.sign_in("john", 456))
    # print(project.sign_in("john", 4565))
    print(project.sign_in("nick", 123))
    print(project.add_user(User(name='iddqd', idx=963, lvl=2)))
    print(project._users)
    