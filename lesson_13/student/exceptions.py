__all__ = [
    'InvalidSubjectException',
    'InvalidGradeException',
    'InvalidNameException',
]


class BaseStudentException(Exception):
    pass


class InvalidNameException(BaseStudentException):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return f'Имя пользователя {self.value} не соответствует требованиям параметра {self.name}'


class InvalidSubjectException(BaseStudentException):
    def __init__(self, subject, full_name):
        self.subject = subject
        self.full_name = full_name

    def __str__(self):
        return f'Предмет {self.subject} не входит в учебную программу студента {self.full_name}'


class InvalidGradeException(BaseStudentException):
    def __init__(self, grade, min_lvl, max_lvl):
        self.grade = grade
        self.min_lvl = min_lvl
        self.max_lvl = max_lvl

    def __str__(self):
        return f'Оценка {self.grade} не входит в требуемый диапазон {self.min_lvl} - {self.max_lvl}'
