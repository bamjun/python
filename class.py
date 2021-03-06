
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name, self.grade, self.age))

student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'C', 12),
    Student('dave', 'B', 10),
]

student_o = [
    ('john', 'A', 15),
    ('jane', 'C', 12),
    ('dave', 'B', 10),
]
print(sorted(student_objects, key=lambda student: student.age))
print(sorted(student_objects, key=lambda student: student.grade))
print(sorted(student_objects, key=lambda student: student.name))
print(sorted(student_o))

>> class.py
[('dave', 'B', 10), ('jane', 'C', 12), ('john', 'A', 15)]
[('john', 'A', 15), ('dave', 'B', 10), ('jane', 'C', 12)]
[('dave', 'B', 10), ('jane', 'C', 12), ('john', 'A', 15)]
[('dave', 'B', 10), ('jane', 'C', 12), ('john', 'A', 15)]



#######################################################################################################################################
#######################################################################################################################################
def difference(l1, l2): return list(filter(lambda x: x not in l2, l1)) + list(filter(lambda x: x not in l1, l2))

>>> def difference(l1, l2): return list(filter(lambda x: x not in l2, l1)) + list(filter(lambda x: x not in l1, l2))
...
>>> a = ['hello','world', 'foo']
>>> b = ['hello','world','im','steve']
>>> difference(a, b)
['foo', 'im', 'steve']
>>>
