import random
list_ = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
n = random.choice(list_)
print("Выпало число:",n)
list_2=[]
for i in range (1,21):
    for k in range (2,21):
        x = i + k
        if i >= k:
            continue
        if n % x == 0 or n == x :
            list_2.append(i)
            list_2.append(k)
print ('Ваш пароль:',''.join(map(str,list_2)))