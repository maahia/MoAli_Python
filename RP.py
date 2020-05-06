a, b = 250, 250

for i in range (250, 260):
    if a is not b:
        break
    a +=1
    print(a)
    b +=1
    print(b)
print("final a", a)
print("fional b" , b)
