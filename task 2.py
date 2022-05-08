x1 = [10, 20, 23, 11, 17]
x2 = [13, 43, 24, 36, 12]
newlist = []
for i in x2 :
    bla = i % 2
    if bla == 0 :

       newlist.append(i)
for ii in x1 :
    if ii%2 != 0:

       newlist.append(ii)

for lol in newlist:
    print(lol)

print(type(newlist))

