# coding: utf-8
import csv
from student import *
from group import *

def main():
    grp = Group()

    with open('C:/Users/Quentin/Desktop/MathsD/preferencesMedium.csv', newline='') as csvfile:
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
    print(" ")

    studToAssign = grp.getSortedStudents()
    nbGrp3Left = grp.getNbGrp3()
    finalRep = []
    while len(studToAssign) != 0:
        l = grp.getPreferedMutualList(studToAssign[0])
        print(studToAssign[0].getIdStudent())
        print("J'assigne : " + str(studToAssign[0].getIdStudent())+ " et sa matrice : "+ str(l))
        trouve = False
        j = 0



        while trouve == False:
            print("Je teste "+ str(j) + " et il me reste "+ str(studToAssign))
            if(l[j] in studToAssign):
                currentGrp = []
                currentGrp.append(l[j])
                currentGrp.append(studToAssign[0])
                print("J'ajoute " + str(l[j].getIdStudent()) + " et "+ str(studToAssign[0].getIdStudent()))
                print("Je retire "+str(l[j].getIdStudent()))
                studToAssign.remove(l[j])

                if nbGrp3Left > 0:
                    degreCourant = 10
                    while trouve == False:
                        for stud in studToAssign:
                            if grp.prefCombined[grp.getIndexStudent(stud)][grp.getIndexStudent(l[j])]>=degreCourant:
                                if grp.prefCombined[grp.getIndexStudent(stud)][grp.getIndexStudent(studToAssign[0])]>=degreCourant:
                                    if trouve == False:
                                        print("J'ajoute " + str(stud.getIdStudent()) + " de degré "+ str(degreCourant))
                                        studToAssign.remove(stud)
                                        currentGrp.append(stud)
                                        trouve = True
                        degreCourant = degreCourant-1
                    nbGrp3Left = nbGrp3Left-1
                else:
                    trouve = True

                print("Je retire "+str(studToAssign[0].getIdStudent()))
                studToAssign.remove(studToAssign[0])
                finalRep.append(currentGrp)
            j+=1
    for i,grp in enumerate(finalRep):
        print(" ")
        print("groupe "+ str(i))
        for j in finalRep[i]:
            print(str(j.getIdStudent()))
    writeDoc(finalRep)

def writeDoc(repartition):
    line = ""
    for i, grp in enumerate(repartition):
        for j in repartition[i]:
            line = line + str(j.getIdStudent()) + " "
        line = line + "; "
    line = line.split(";")
    print(line)

    with open('FGT.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        lines = list(reader)
        lines[0] = line

    with open('FGT.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)


main()
