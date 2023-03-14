from pathlib import Path

import pytest

from lesson_14.task_6.user import User
from lesson_14.task_6.project import Project


@pytest.fixture
def set_users():
    data = {
        User(name="qwerty", idx=987, lvl=1),
        User(name="nick", idx=123, lvl=1),
        User(name="abc", idx=741, lvl=1),
        User(name="john", idx=456, lvl=5),
    }
    return data


def test_read_json(set_users):
    project = Project()
    res = project.read_json(Path('names.json'))
    assert res == set_users


if __name__ == '__main__':
    pytest.main(['-v'])