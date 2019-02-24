class Student:
    def __init__(self, idStudent):
        self.idStudent = idStudent
        self.prefStudent = []

    def getIdStudent(self):
        return int(self.idStudent)

    def getPrefStudent(self):
        return self.prefStudent

    def setPreference(self, table):
        self.prefStudent = table

    def displayStudent(self):
        print("Etudiant " + str(self.idStudent) + ", mes prefs : " + str(self.prefStudent[0]) + " " + str(self.prefStudent[1]))