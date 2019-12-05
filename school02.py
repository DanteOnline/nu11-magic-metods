class Group:

    # 1. Статический метод
    @staticmethod
    def show_help():
        print('Класс группа в школе')
        print('Что то еще делаем...')

    @staticmethod
    def create_groups(n):
        """
        создает столько гурпп сколько мы укажаем
        :return: список новых групп
        """
        names = ['A', 'B', 'C', 'D', 'E']
        result = []
        for i in range(n):
            name = names[i]
            new_group = Group(i, name)
            result.append(new_group)
        return result

    # Метод класса
    @classmethod
    def create_groups_classmetod(cls, n):
        """
                создает столько гурпп сколько мы укажаем
                :return: список новых групп
                """
        names = ['A', 'B', 'C', 'D', 'E']
        result = []
        for i in range(n):
            name = names[i]
            new_group = cls(i, name)
            result.append(new_group)
        return result

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


class StudentGroup(Group):

    @staticmethod
    def create_groups(n):
        """
        создает столько гурпп сколько мы укажаем
        :return: список новых групп
        """
        names = ['A', 'B', 'C', 'D', 'E']
        result = []
        for i in range(n):
            name = names[i]
            new_group = StudentGroup(i, name)
            result.append(new_group)
        return result


if __name__ == '__main__':
    Group.show_help()

    groups = Group.create_groups(3)

    for group in groups:
        print(group)

    groups = Group.create_groups_classmetod(3)

    print(groups)

    groups = StudentGroup.create_groups_classmetod(3)
    print(groups)


