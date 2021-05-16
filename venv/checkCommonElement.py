def approach1():
    global a, b
    a = [1, 2, 3, 4, 5]
    b = [5, 6, 7, 8, 9]
    for vala in a:
        for valb in b:
            if vala == valb:
                print("common values present")


def approach2():
    [print("common values present") for vala in a if vala in b]


def approach3():
    c = set(a)
    d = set(b)
    if not c.isdisjoint(d):
        print("common values present")


approach1()
approach2()
approach3()
