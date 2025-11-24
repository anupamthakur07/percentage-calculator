# percentage calculator
print('Welcome to the percentage calculator')
while True:
 print("select from the below \n1.start\n2.exit")
 choice=input('enter your choice:')
 if (choice=='1'):
   a,b,c,d,e=map(int,input('enter your marks:').split(','))
   #formula used
   percentage=(a+b+c+d+e)*100/500
#calculating percentage and remark
   if (percentage>=90):
     print('excelent! your percentage is:',percentage, end='%')
   elif(percentage>=80 and percentage<=90):
     print('great! your percentage is :',percentage,end="%")
   elif(percentage>=33 and percentage<=80):
     print('good your percentage is:',percentage,end='%')
   else:
     print('oho! failed',percentage,end='%')
     #asking user for calculating again
   repeat=input("\ndo you want to calculate again(yes/no): ")
   if repeat!='yes':
     print('thank you for using our programme ')
     break
#exit from the programme 

 elif (choice=='2'):
  print('thank you for using our programme ')
  break
 else:

  print('please choose only 1 or 2')

