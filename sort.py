import random
nsl = [random.randint(0,1000000) for i in range(100)]#not sorted list не отсортированный начальный список
nsl2 = nsl.copy()
c = 0 #счетчик перемещений для пузырька
i = 0
print("начальный список: ", nsl)
print("СОРТИРОВКА ПУЗЫРЕК:")
while i<len(nsl)-1:
    if nsl[i]<nsl[i+1]:
        nsl[i],nsl[i+1]=nsl[i+1],nsl[i]
        c+=1
        i=0
        print(nsl)
    else:
        i+=1
print("отсортированный список пузырьком: ", nsl)
print()
print("количество операций: ", c)

c2 = 0 #счетчик перемещений для выбора
print("СОРТИРОВКА ВЫБОРОМ:")
for j in range(len(nsl2)):
    max=j
    for k in range(j+1,len(nsl2)):
        if nsl2[k]>nsl2[max]:
            max=k
    if max != j:
        nsl2[j],nsl2[max]=nsl2[max],nsl2[j]
        c2+=1
        print(nsl2)
print("отсортированный список выбором: ", nsl2)
print("количество операций: ", c2)