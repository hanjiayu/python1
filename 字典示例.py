#һ���򵥵����ݿ�

#�ֵ�ʹ��������Ϊ����ÿ��������һ���ֵ�����ʾ�������phone���͡�addr���ֱ��ʾ���ǵĵ绰����͵�ַ

people = {

    'Alice':{
        'phone':'2341',
        'addr':'Foo drive 23'
        },
    'Beth':{
        'phone':'9102',
        'addr':'Bar street 42'
        },
    'Cecil':{
        'phone':'3158',
        'addr':'Baz avenue 90'
        }

    }
#��Ե绰����͵�ַʹ�õ������Ա�ǩ�����ڴ�ӡ�����ʱ���õ�
labels = {
    'phone':'phone number',
    'addr':'address'
    }
name = raw_input('Name:')

#���ҵ绰���뻹�ǵ�ַ
request = raw_input('Phone number(p) or address(a)?')

#ʹ����ȷ�ļ���
if request =='p':key = 'phone'
if request == 'a':key = 'addr'

#����������ֵ��е���Ч���Ŵ�ӡ��Ϣ��
if name in people:
    print "%s's %s is %s." %(name,labels[key],people[name][key])
