'''
there are 2 type of data type:

1.MUTABLE: mutable data can changes and modified and updates
 ex. list, dictionary,set

2.IMMUTABLES: does not change and modified
 ex.Tuples,

 
 Data Structure:

 1) LIST:
    list is collection of item, it is mutable data type , list order is changable
    list use [] , consuming more memmory, excution becomes slow.
    ex A=[10,50,40,81,]
           
        *ARRAY: is part of list , is aslo collection of item.
            store single data type.

2)  TUPLE:
    tuple order is unchangable, it is collection of item, it is immutable data type, use (),
    excution in tuple is fast as campare to list, consuming less memory as campare to list.

3) SET:
    collection of item, it is unorder and changable, use {}, consume less memory , it is mutable , 
    duplicate values are not allowed.

4) DIC:
    it is collection of item, it is store value in key value pair,it is unorder and changable.
    it is change value not key., it is mutable, use {}
'''

#list
list =[1,2,3,4,5,6,7,8,9,10]
list.append(2)
list.reverse()
list.remove(2)
list.sort()

print(list)


list_1=[10,12,51,45,43,1]
print(sum(list_1))

