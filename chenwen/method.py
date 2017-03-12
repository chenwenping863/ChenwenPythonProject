def addSum(num):
    sum = 0
    for i in num:
        sum += i
    return sum

num = [1, 2, 3, 4, 4]
print addSum(num)
x = 1
def changex():
    global x
    x = 10

changex()
print x