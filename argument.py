'''


'''

def func(x,y):
    z=x,y
    print(z)
func(90,10)
func("90","mahto")



def fun( *x):
    for i in x:
        print(i)

fun(90,10)
fun(90,'mahto')
fun('kumar','mahto')
