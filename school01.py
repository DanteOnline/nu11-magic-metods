"""
Программа "Школа"
В школе есть группы
В группе есть школьники
У школьников есть родители
У группы есть номер и название например 5Б
"""
import math


class Group:

    def __init__(self, name, number):
        self.name = name
        self.number = number
        self._students = []

    def pop(self):
        pass

    def remove(self, student):
        self._students.remove(student)

    def add(self, student):
        self._students.append(student)

    def count(self):
        return len(self._students)

    def __str__(self):
        return f'{self.number} {self.name} кол-во человек: {len(self)}'

    def __len__(self):
        return len(self._students)

    def __getitem__(self, item):
        """
        Нумерация идет с 1 - го
        :param item:
        :return:
        """
        # return self._students[item - 1]
        return self._students[item]

    def len(self):
        return len(self._students)

    def __eq__(self, other):
        # Сравнение по названиями и числу
        # return self.name == other.name and self.number == other.number
        # Сравнение по студентам
        # return self._students == other._students
        # Сравнение по длине
        return len(self) == len(other)

    def __contains__(self, item):
        return item in self._students

    def __gt__(self, other):
        # По количесту студентов
        return len(self) > len(other)

    def __ge__(self, other):
        return len(self) >= len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __add__(self, other):
        if isinstance(other, list):
            new_group = Group(self.number, self.name)
            new_group._students = self._students + other
        else:
            group_number = (self.number + other.number) / 2
            group_name = self.name + other.name
            new_group = Group(group_number, group_name)
            new_group._students = self._students + other._students
        return new_group


if __name__ == '__main__':
    # TODO: сделать класс для школьника
    leo = 'Leo'
    max = 'Max'
    kate = 'Kate'

    group = Group('Б', 5)

    group.add(leo)
    group.add(kate)

    print(group)
    group_str = str(group)
    print(group_str)

    group.add(max)
    print(group)

    # Количество человек в группе
    # print(len(group._students)) - не верно брать закрытое свойтсво
    print(group.count())

    # Утиная типизация
    # СТатическая типизация
    # String str = "abc"
    # A -> B(A), C(A)
    # A my_var = B()

    print(len([1, 2, 3]))
    print(len('abcd'))

    a = [1, 2, 3]
    a.pop()
    # print(dir(object))
    print(len(group))

    print(group.len())

    #
    # objects = [group, a]
    #
    # for item in objects:
    #     print(len(item))
    #     print(item.len())

    # получение по индексу
    print(group[1])

    print('Студенты в группе')
    # будет работать цикл for благодаря getitem
    for student in group:
        print(student)

    # Сравнение 2-х групп
    group_3a = Group('A', 3)
    group_3a.add(leo)
    group_3a.add(kate)
    group_3a.add(max)

    print(group == group_3a)

    # как использовать магический метод на прямую, только так не надо делать
    print(group.__eq__(group_3a))

    group_3a.add('new')
    print(group == group_3a)

    print(group == [1, 2, 3])

    # есть ли leo в группе?
    print('Есть' if 'leo' in group else 'Нет')
    print('Есть' if 'Leo' in group else 'Нет')

    print(group > group_3a)
    print(group < group_3a)
    print('На равенство')
    print(group >= group_3a)
    print(group <= group_3a)
    print('Удалили new')
    group_3a.remove('new')
    print(group > group_3a)
    print(group < group_3a)
    print(group >= group_3a)
    print(group <= group_3a)

    # Урезали бюджет и 3-и группу будет вместе с 5ым теперь
    all_group = group + group_3a
    print(all_group)

    group += group_3a

    print(group)

    group_3a += ['John', 'Poll']

    print(group_3a)

    for item in group_3a:
        print(item)
