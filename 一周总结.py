#coding:utf-8
__author__ = '5'
#输出第一个程序
print "Hello,World"

#使用list
classmates = ['Micheal','Bob','Tracy']
print 'classmates=',classmates
print 'len(classmates)=',len(classmates)
print 'classmates[0]=',classmates[0]
print 'classmates[1]=',classmates[1]
classmates.pop()
print 'classmates =', classmates

#使用tuple
classmates = ('Micheal','Bob','Tracy')
print 'classmates = ',classmates
print 'len(classmates)=',len(classmates)
print 'classmates[1] = ',classmates[1]



#循环
names = ['Micheal','Bob','Tracy']
for name in names:
    print name

for x in range(10):
    print x

#计算1 + 2 + 3 .。。100
sum = 0
x = 1
while x <= 100:
    sum = sum + x
    x = x + 1

print sum

#计算1 * 2 * 3 *4 * 。。。。100
scc = 0
x = 1
while x <= 100:
    scc = scc + x
    x = x + 1
print scc


#使用dict
d = {'Micheal':95,
     'Bob':75,
     'Tracy':85
     }
print 'd[\'Micheal\']',d['Micheal']
print 'd[\'Bob\']',d['Bob']
print 'd[\'Tracy\']',d['Tracy']
print 'd.get(\'Thomes\'，-1)=',d.get('Thomas',-1)

#使用set
s1 = set([1,1,2,2,3,3])
print s1
s2 = set([2,3,4])
print s2
#调用函数
x = abs(100)
y = abs(-20)
print x,y
print 'max(1,2,3)=',max(1,2,3)
print 'min(1,2,3)=',min(1,2,3)

#定义函数
import math

def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('Bad operand type')
    if x >= 0 :
        return x
    else:
        return -x

def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx,ny
n = my_abs(-10)
print n

x , y =move(100,100,60,math.pi / 6)
print (x,y)

#计算power2
def power(x):
    return x * x

power(2)

#计算power(x,n)
def power(x,n):
    s = 1
    while n > 0:
        n = n -1
        s = s * x
    return s

#可变参数
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum

calc([1,2,3])  #需要组装list 或者 tuple

#不需要组装的情况
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

calc(12,3)

#关键字参数
def person(name,gender,**kw):
    print 'name:',name,'age:',age,'other:',kw


