'''
what is decorator?
--> speacil funtion , take another function as argument and modify to return function.



'''

def decor_function(function):
    def product():
        print('this is very good product')
        function()

    return product()

@decor_function
def IIT():
    print('welcome to IIt Delhi')

#iterator is function to iterate the value
    list = [34,90,45,32,12,54,32]
    x= iter(list)
    print(next(x))
    print(next(x))

# generator function is special function used to return value and return statement 
#used to generate value and return statement


#yield combination of iterator and generator

def add (a,b):
    yield a
    yield b
print(add(23,78))
print(type(next))


a = 90
b = 20
print('A :',a)
print('B :',b)

a, b = b, a

print("A :",a)
print('B :',b)