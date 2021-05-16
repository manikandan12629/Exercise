x = [12, 35, 9, 56, 24]

def approach1():
    x.reverse()
    print(x)

def approach2():
    x = [12, 35, 9, 56, 24]
    myList=[]
    i = len(x)
    while i > 0 :
        myList.append(x[i-1])
        i-=1
    print(myList)

def approach3():
    x = [12, 35, 9, 56, 24]
    i = len(x)
    while i > 0 :
        y =  list((x[i-1]))
        i-=1
    print(y)


approach1()
approach2()
#approach3()