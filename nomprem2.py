fin = int(input("a quel nombre faut t'il s'arreter?"))
for i in range(2,fin):
    divisible=False
    for j in range(2,i):
        if i % j == 0:
            divisible=True
            break
    if divisible == False:
        print("%s est un nombre premier."% i)
