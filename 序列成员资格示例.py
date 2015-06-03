#检查用户名和PIN码

database = [
    ['albart','1234'],
    ['dilbert','4242'],
    ['smith','7524'],
    ['jones','9843']
]
username = raw_input('Username:')
pin = raw_input('PIN code:')

if [username,pin] in database:
    print 'Access grandted'
