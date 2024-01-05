import array

fin = int(input("a quel nombre faut t'il s'arreter?"))

a = array.array("L", [True for i in range(fin)])

a[0] = False
a[1] = False

for i in range(fin):
    if a[i] == True:
        for j in range(2, int(fin / i)):
            a[i * j] = False
        print("%s est un nom!bre premires." % i)
