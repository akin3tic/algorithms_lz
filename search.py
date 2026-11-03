import random
sl = [random.randint(0,1000000) for i in range(100)]#search list список для поиска


list = [67,93,105,52,97,69,22,17,76,11]
b = len(list)
a = 17
c = 0
for i in range(1,b):
    if a == list[i]:
        c +=1
        print(list[i])
if c == 0:
    print("chislik ne naiden")