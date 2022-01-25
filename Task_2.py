n = input('Enter number: ')

left = n[0:len(n)//2]
right = n[len(n)//2:len(n)]
rightReversed = right[::-1]

if left == rightReversed:
    print('number is palindrom')
else:
    print('number is not palindrom')






















