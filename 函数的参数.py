#����x*2�Ĳ���
def power(x):
    return x * x


#����x * n �Ĳ���
def power(x,n):
    sum = 1
    while n > 0:
        n = n - 1
        sum = sum * x
    return sum


#�ɱ�����������ڲ����յ�����һ��tuple,��˺����Ĵ�����ȫ���䡣
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

#�ؼ��ֲ���
def person(name,age,**kw):
    print ('name:',name,'age:',age,'other:',kw)

#�����ؼ��ֲ��������ƹؼ��ֲ���������(���봫�������)
    
def person(name, age, *, city, job):
    print(name, age, city, job)
