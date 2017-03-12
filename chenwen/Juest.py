light = "Green"
if light == "red":
    print "Stop"
elif light == "Green":
    print "Go"
elif light == "yellow":
    print "slow down"


sum = 0;
i = 0;

while i <= 100:
    sum += i
    i += 1
print sum

num = [0, 1, 2, 3, 4]
for i in  num:
    print i + 10

contact = {"title" : "28731989", "Hanmeimei" : "83749839"}

for i in contact:
    print i, contact[i]

num = [0, 1, -2, 3, -4]
for i in num:
    if i < 0:
        continue
    print i

num = [1, 2, 3, 4, 5]
for i in num:
    sum += i
print i






