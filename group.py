class Group:
    def __init__(self):
        self.members = []

    def addStudent(self, student):
        self.members.append(student)

    def getSize(self):
        return len(self.members)

    def displayGroup(self):
        print("Etudiants : ")
        for student in self.members:
            student.displayStudent()

    def getPreferenceCombined(self):
        n = len(self.members)
        grid = [[0] * n for i in range(n)]

        for i,row in enumerate(grid):
            for j,elem in enumerate(row):
                grid[i][j] = self.members[i].getPrefStudent()[j] + self.members[j].getPrefStudent()[i]

        for row in grid:
            print(' '.join([str(elem) for elem in row]))
        return grid
