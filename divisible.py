print('enter a number(numerator):')
numn = int(input())
print('enter a (denominator):')
numd = int(input())
if numn%numd == 0:
    print('\n' +str(numn) + ' is divisible by'+str(numd))
else:
    print('\n' +str(numn) + ' is not divisible by'+str(numd))
