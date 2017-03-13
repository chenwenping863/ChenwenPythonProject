num = [1, 2, 3, 4, 5, 6]
even = [i for i in num if i %2 == 0]
print even

even = [i *2 for i in num]
print even

#if a > 1 and a < 10
a = 10
if 1 < a <= 10:
    print a

A = {1, 2, 3, 4}
B = {4, 5, 6}
print A | B
print A & B