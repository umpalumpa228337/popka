print ('Hello World')



def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n-1)
print(fact(5))




mass = [1,2,3,4,5,6,7,12]
print(max(mass))




spisok = []
spisok.append(20)
spisok.append(2)
spisok.append(1)
spisok.append(67)
print(spisok)
print(spisok[0])
print(spisok[-1])