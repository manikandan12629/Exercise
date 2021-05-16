def approach1():
    global x, y, z
    x='abc'
    y='hello world !'
    z=' h e l   l  o '

    print('x length is {}, y length is {} and z lenth is {}'.format(len(x), len(y),len(z)))

def approach2():
    a = b = c = 0
    for i in x:
        a+=1
    for i in y:
        b+=1
    for i in z:
        c+=1

    print(f'x length is {a}, y length is {b} and z lenth is {c}')

approach1()
approach2()