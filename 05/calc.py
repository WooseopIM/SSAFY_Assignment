def mysum(x,y):
    a = x+y
    return a

def mysub(x,y):
    b = x-y
    return b

def mymul(x,y):
    c = x*y
    return c

def mydiv(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        return '0으로는 나눌 수 없습니다.'

print(mydiv(12,4))
print(mydiv(12,0))
print(mydiv(12,'0'))
