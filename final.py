class student:
    def __init__(self, name, id):
        self.name = name 
        self.id = id
        self.grades    =[]
        
    def addGrade(self,grade):
        self.grades.append(grade)
    def getPoint(marks)
        if(marks > 90):            # A grade
            return 4
        else if(marks > 80):    # B Grade
            return 3
        else if(marks > 70):    # C Grade
            return 2
        else                    # F Grade
            return 0
    def GPA(grades[]):
        tot = 0
        length = len(grades)
        for marks in grades:
            tot = tot + getPoint(marks)
        return tot/(length*4)
        
    def getGPA(self):
        GPA(self.grades)
            
        
        
s1 = student('Navdeep','A12345')
s1.addGrade(94)
s1.addGrade(84)
s1.GPA()