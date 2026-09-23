'''
WHAT IS EXCEPTION?
it is unwanted and unexpected conditions in program.
when we write a program that time get any error is called excepton

how to handle exception
by using 5 methods
1.try
2.except
3.else
4.finally
5.raise

as specially use except method.

types of error
1.zero division error
2.value error
3.arithmetic error
4.atrribute error

'''
# try:
#     A = int(input("enter the number: "))
#     B = int(input("enter the number: "))
#     c = (A/B)
#     print(c)

# except ZeroDivisionError:
#     print("can not divider by zero")
# else:
#     print("divided by zero ")

# finally:
#     print("thanks")


# try:
#     a = 90
#     b = 'k'
#     c = a / b
#     print(c)

# except TypeError:
#     print('inside exception')

# else:
#     print("Inside else")

# finally:
#     print("thanks")


#arthmatic error
try:
    A = int(input("enter the number: "))
    B = int(input("enter the number: "))
    c = (A/B)
    print(c)

except ArithmeticError:
    print("can not divider by zero")
else:
    print("divided by zero ")

finally:
    print("thanks")
