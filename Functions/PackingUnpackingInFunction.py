def Calc(fNo, sNo):
    return fNo+sNo, fNo-sNo


num1=int(input('first number :'))
num2=int(input('second number :'))

# unpacking
addVal,subVal=Calc(num1,num2)
print('summation is :',addVal)
print('substraction is :',subVal)