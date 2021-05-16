class parent:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printName(self):
        print(self.fname, self.lname)


class child(parent):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.grad_year = year

    def printName(self):
        print(self.fname + " " + self.lname + " joined in", self.grad_year)


class sampIter():
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            self.a += 1
            return self.a
        else:
            raise StopIteration


mysamp = sampIter()
y = iter(mysamp)

for z in y:
    print(z)

# x= child("mani","kandan",2020)
# x.printName()

pow