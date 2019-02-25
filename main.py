# coding: utf-8
import csv
from student import *
from group import *

def main():
    grp = Group()

    with open('C:/Users/Quentin/Desktop/MathsD/preferences.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for i,row in enumerate(spamreader):
            if(i!=0):
                idStudent = row[0]
                if(idStudent != ""):
                    stud = Student(idStudent)
                    del row[0]
                    preference = []
                    for note in row:
                        if(note == "AR"):
                            preference.append(0)
                        if(note == "I"):
                            preference.append(1)
                        if(note == "P"):
                            preference.append(2)
                        if(note == "AB"):
                            preference.append(3)
                        if(note == "B"):
                            preference.append(4)
                        if(note == "TB"):
                            preference.append(5)
                        if(note == "-1"):
                            preference.append(-1)
                    stud.setPreference(preference)
                    grp.addStudent(stud)
    for stud in  grp.members:
        print(str(stud.getIdStudent())+" prefere "+ str(grp.getPreferedMutualStudent(stud).getIdStudent()))
    for stud in  grp.members:
        print(grp.getPreferedMutualList(stud))
    for i in range(18,58):
        print("Avec "+ str(i) + " élèves, je forme "+ str(grp.getNbGrp3()) + " groupes de 3.")
main()
