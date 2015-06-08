#计算x*2的参数
def power(x):
    return x * x


#计算x * n 的参数
def power(x,n):
    sum = 1
    while n > 0:
        n = n - 1
        sum = sum * x
    return sum


#可变参数，函数内部接收到的是一个tuple,因此函数的代码完全不变。
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

#关键字参数
def person(name,age,**kw):
    print ('name:',name,'age:',age,'other:',kw)

#命名关键字参数：限制关键字参数的名字(必须传入参数名)
    
def person(name, age, *, city, job):
    print(name, age, city, job)
