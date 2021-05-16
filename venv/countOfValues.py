'''
Given an unsorted list of some elements(may or may not be integers), Find the frequency of each distinct element in the list using a dictionary.
Example:
Input : [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,4, 4, 4, 2, 2, 2, 2]
Output : 1 : 5
         2 : 4
         3 : 3
         4 : 3
         5 : 2
Explanation : Here 1 occurs 5 times, 2 occurs 4 times and so on...
The problem can be solved in many ways. A simple approach would be to iterate over the list and use each distinct element of the list as a key of the dictionary and store the corresponding count of that key as values.
'''
def approach1():
    global x
    x= [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
    y = set(x)
    a = {}
    for z in y:
        d = str(z)
        i = x.count(z)
      #  a[d]=i
        a.update({d:i})
    print(a)

def approach2():
    a=[]
    b={}
    for y in x:
        if y not in a:
            a.append(y)
            c=str(y)
          #  b[c]=x.count(y)
            b.update({c:x.count(y)})

    print(b)

approach1()
approach2()
