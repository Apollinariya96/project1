import random
a=0
s=0
nov_ch=0
m=random.randint(0,1)
if m==1:
    n=0
    t=0
else:
    n=random.randint(0,1)
    if n==1:
        t=0
    else:
        t=1
a=[m,n,t]
print(a)
print("Выберите дверь")
k=int(input())
#Если первая дверь - "нужная"
#Мы выбираем первую дверь
if m==1 and k==1:
    chislo_1=random.randint(n,t)
#    if chislo_1==n:
    print("Открываю вторую дверь: ", chislo_1)
#    nov_ch=int(chislo_1)
#Мы выбираем вторую дверь
if m==1 and k==2:
    print("Хех,а я открою третью: ", t)
    nov_ch=int(m)
#    print(nov_ch)
#Мы выбираем третью дверь
if m==1 and k==3:
        print("А вот и не открою. Открываю вторую: ",n)
        nov_ch=int(m)
#        print(nov_ch)
#Если вторая дверь нужная
#Мы выбираем вторую дверь
if n==1 and k==2:
    chislo_2=random.randint(m,t)
    print("Открываю третью дверь:", chislo_2)
#Мы выбираем первую дверь
if n==1 and k==1:
    print("А где пожалуйста? Без пожалуйста могу открыть только третью: ",t)
    nov_ch=int(n)
#Мы выбираем третью дверь
if n==1 and k==3:
    print("А где пожалуйста? Без пожалуйста могу открыть только первую: ", m)
    nov_ch=int(n)
#Если третья дверь нужная
#Выбираем третью дверь
if t==1 and k==3:
    chislo_3=random.randint(m,n)
    print("Открываю первую дверь: ",chislo_3)
#Выбираем первую дверь
if t==1 and k==1:
    print("А вот и не открою. Открываю вторую: ", n)
    nov_ch=int(t)
#Выбираем вторую дверь
if t==1 and k==2:
    print("Хех, а я открою третью: ", m)
    nov_ch=int(t)
print("Вы хотите изменить свой выбор или по-прежнему выбираете", k, "дверь?")
print("1-не менять выбор, 2-изменить выбор")
vibor=int(input())
if vibor ==1:
    s=int(k-1)
#    print(s)
    print(a[s])
    if a[s]==1:
        print("Вы выиграли")
    else:
        print("Увы, вы проиграли")
if vibor==2:
    print(nov_ch)
    if nov_ch==1:
        print("Поздравляем! Вы выиграли!")
if nov_ch==0:
    print("Вы проиграли")
#версия 2
#Если вторая дверь - "нужная"
#if k==2:
#    if k==n:
#        if m<=1:
#            print(m)
#        else:
#            print(t)
#Если третья дверь - "нужная"
#if k==3:
#Мы выбираем третью дверь
#    if k==t:
#        if m<=1:
#            print(m)
#        else:
#           print(n)
