"""
Given different scored marks of students. We need to find grades. The test score is an average of the respective marks scored in assignments, tests and lab-works. The final test score is assigned using below formula.
10 % of marks scored from submission of Assignments
70 % of marks scored from Test
20 % of marks scored in Lab-Works
Grade will be calculated according to :
1. score >= 90 : "A"
2. score >= 80 : "B"
3. score >= 70 : "C"
4. score >= 60 : "D"
Also, calculate the total class average and letter grade of class.
"""


class Average(Grade):
    def __init__(self):
        self.students = {
            "arun": {
                "Assignments": 90,
                "Test": 100,
                "Lab": 100
            },
            "balaji": {
                "Assignments": 80,
                "Test": 92,
                "Lab": 78
            },
            "logesh": {
                "Assignments": 75,
                "Test": 65,
                "Lab": 80
            }
        }

    def approach1(self):
        for x in self.students.keys():
            for y in self.students[x]:
                if y == "Assignments":
                    z = (self.students[x].get(y) / 100) * 10
                    self.students[x][y] = z
                if y == "Test":
                    z = (self.students[x].get(y) / 100) * 70
                    self.students[x][y] = z
                if y == "Lab":
                    z = (self.students[x].get(y) / 100) * 20
                    self.students[x][y] = z
        for x in self.students.keys():
            q = 0
            for y in self.students[x]:
                z = self.students[x].get(y)
                q += z

            totalgrade = grade(q)
            print(f'{x} grade is ', totalgrade)


class Grade:
    def grade(self, totalmarks):
        if totalmarks in range(90, 100):
            return "A"
        elif totalmarks in range(80, 89):
            return "B"
        elif totalmarks in range(70, 79):
            return "c"
        else:
            return "D"


average = Average()
average.approach1()
