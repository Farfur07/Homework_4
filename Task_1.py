a = input('n= ')

if len(a) != 4:
    print("wrong enter")

left = map(int, a[0:2])
right = map(int, a[2:4])

if sum(left) == sum(right):
    print('YOU ARE LUCKY!')
else:
    print('Bad day for you now((')



