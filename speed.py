a = int(input(' enter the value:'))
b = int(input('enter the value 2:'))
c = int(input('enter the value 3:'))
avg = (a + b + c) / 3
print('avg =', avg)
if avg > a and avg > b and avg > c:
    print('%d is greater than %d, %d and %d'%(avg, a,b,c))
elif avg > a and avg > c:
    print('%d is greater than %d,%d'%(avg,a,c))
elif avg > b and avg > c:
    print('%d is greater than %d,%d'%(avg,b,c))
elif avg > a:
    print('%d is greater than %d,'%(avg,a,))
elif avg > b:
    print('%d is greater than %d,'%(avg,b))
elif avg > c:
    print('%d is grater than %d,'%(avg,c))
else:
    print('Invalid Input')
