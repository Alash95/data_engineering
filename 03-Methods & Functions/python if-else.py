n = int(input())

if n % 2 == 0 and 2 <= n <= 5:
    print('Not Wierd')

elif n % 2 == 0 and 6 <= n <= 20:
    print('Wierd')

elif n % 2 == 0 and n > 20:
    print('Not Wierd')

else:
    print('Wierd')