'''program to show that if divisible by 3 output: Tipsy
if divisible by 7 output:Topsy and if divisible by both 7  and 3 output:TipsyTopsy '''

a=int(input('enter a number :'))

if a%7==0 and a%3==0:
    print('TipsyTopsy')
    
elif a%3==0:
    print('Tipsy')
 
elif a%7==0:
    print('Topsy')

else:
    print('Not divisible by 3 and 7')
   
