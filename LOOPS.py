'''
there are 2 type of loop:

1.for loop: we know the number of iteration
2.while loop: we don't know number of iteration

both are used for number of iteration.


'''


# for i in range(1,20):
#     print(i)


# a= 0
# while a<=10:
#     a+=1
# print(a)


# i=1
# while i>=20:
#     print(i)
#     i+=1


# list =[1,2,3,4,5,6,7,8,9]
# result=[num**2 for num in list]
# print(result[::-1])

# list =[1,2,3,4,5,6,7,8,9]
# result=[num**2 for num in list if num % 2!=0]
# print(result[::-1])

# list =[45,12,55,19,45,10,57,55,18]

# print(min(list))


# list =[29,90,67,89,54,32,67,10]
# max = list[0]
# for i in list :
#     if i> max:
#         max=i
# print(max)



# list =[29,90,67,89,54,32,67,100]
# min = list[0]
# for i in list :
#     if i<min:
#         min=i
# print(min)


# list =[29,90,67,89,54,32,67,100]
# add= 8
# for i in list :
#     add =add+1

# print(add)




# list= [1,2,3,4,5,6,7,8,9,10,3,4,5,8,1]
# duplicate=[]
# seen = set()
# for i in list:
#     if i in seen:
#         duplicate.append(i)
#     else:
#         seen.add(i)

# print ('list=', list)

# print("duplicate=", duplicate)



number= int(input('enter the number: '))
for i in range (2,number):
    if number%i==0:
        print('this is not prime number.')
        break
    else:
        print('this is prime number')
