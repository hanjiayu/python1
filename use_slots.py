class Student(object):
    __slots__=('name','age')#��tuple��������󶨵���������

class GraduateStudent(Student):
    pass

s = Student()
s.name = 'Micheal'
s.age = 25
try:
    s.score = 99
except AttributeError as e:
    print 'AttributeError:',e

g = GraduateStudent()
g.score = 99
print g.score
