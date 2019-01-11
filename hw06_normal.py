# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

import random
import re

surname = ('Сидоров', 'Иванов', 'Петров', 'Осин', 'Волин', 'Сергеев', 'Дмитриев', 'Турин', 'Ткачев', 'Захаров', 'Лунев')
names = ('Ф.', 'А.', 'Д.', 'С.', 'Л.', 'В.', 'П.', 'Я.', 'Н.', 'Е.')
predmet = ('Математика', 'Русский язык', 'Физика', 'Английский язык', 'Химия', 'Биология')


class School():
    def __init__(self, name):
        self.name = name
        self.Class = []
        self.Student = []
        self.Teachers = []

    def addClass(self, Clas):
        self.Class.append(Clas)

    def showClass(self):
        print('Школа {} содержит:'.format(self.name))
        for i in self.Class:
            print('класс {}'.format(i))

    def showClass(self, name):
        for i in self.Class:
            if name == self.Class(i):
                for Std in self.Student:
                    print('Ученик {}'.format(self.Student(Std)))

    def addStdil(self, Stdil):
        self.Student.append(Stdil)

    def addTeacher(self, name_predmet):
        self.Teachers.append(name_predmet)

    def showStdilInfo(self, name):
        for st in self.Student:
            sm = re.findall(r'\w', st)
            if  sm == name:
                print('Ученик {}'.format(sm))

    def genSchool(self, Class, Student, Predmet):
        for dx in range(int(Class)):
            xclass = str(random.randint(5, 11)) + random.choice(('А', 'Б', 'В', 'Г'))
            self.addClass(xclass)
            for i in range(int(Student)):
                xclass1 = xclass + ' ' + (random.choice(surname) + ' ' + random.choice(names) + random.choice(names))
                self.addStdil(xclass1)
            for i in range(int(Predmet)):
                n = xclass + ' ' + (random.choice(surname) + random.choice(names) + random.choice(names)), (random.choice(predmet))
                self.addTeacher(n)

shool = School('№ 117')
shool.genSchool(10, 10, 6)
print(shool.Student)
print(shool.showStdilInfo('Осипов'))