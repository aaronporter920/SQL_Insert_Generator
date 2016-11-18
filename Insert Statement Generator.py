#---------------------------------------
#----I308 Insert Statement Generator----
#---------------------------------------
#-------------Aaron Porter--------------
#---------------------------------------


import random
#variables to work with later
classes = []
students = []
roster = []
classlst = []
semesterhascourse = ""
facultyteachesincourse = ""
schedule = ""
studentsched = ""
SQL = ""


#information to randomize
classrooms = [1145,2123,1111,1106,2222,2213,1265,2007,2050,2043]
semester = [101,201,301,102,202,302]
number = 0
courses = {77777:"Biblical Biology",77778:"Evolution",77779:"Everybody Poops",77780:"Swurfology",77781:"How to Get Away With Murder",77782:"Using Technology to Cover Your Tracks",77783:"You Can't Handle the Swurf",77784:"Police Academy",77785:"Addition",77786:"Subtraction",77787:"Divison",77788:"Swurfiplication",77789:"How to Build a Lovebot",77790:"Programming your Emotions",77791:"Soviet Coding",77792:"How I Learned to Stop Worrying and Love the Swurf",77793:"Pig Latin Computing",77794:"Informatics in 300 B.C.",77795:"Wumbology",77796:"Discrete Swurfimatics"}

#Starts inser statement
studentsched += "INSERT INTO Class\nVALUES"
for key in courses:
      classlst.append(key)

for item in semester:
      for i in range(12):
            number +=1
            course = random.choice(classlst)
            classNum = str(course)+str(number)
            classes.append(classNum)

            studentsched += "("+str(classNum)+",'"+courses[course]+"',"+str(random.randrange(1,4))+","+str(course)+"),"
            studentsched += "\n"
            semesterhascourse += "(0"+str(item)+","+str(course)+"),\n"
            classroom = str(random.choice(classrooms))
      
            if classroom[0] == "1":
                  schedule += "(,'Riley Hall',"+str(classNum)+",0"+classroom+"),\n"
            elif classroom[0] == "2":
                  schedule += "(,'McNeal Annex',"+str(classNum)+",0"+classroom+"),\n"
            #faculty ID , class #
            if course < 77781:
                  facultyteachesincourse+= "("+random.choice(["1006791001","1006791008"])+","+str(classNum)+"),\n"
            elif course >= 77781 and course <77785:
                  facultyteachesincourse+= "("+random.choice(["1006791002","1006791010"])+","+str(classNum)+"),\n"
            elif course >= 77785 and course <77789:
                  facultyteachesincourse+= "("+random.choice(["1006791003","1006791005"])+","+str(classNum)+"),\n"
            elif course >= 77789 and course <77793:
                  facultyteachesincourse+= "("+random.choice(["1006791004","1006791009"])+","+str(classNum)+"),\n"
            elif course >= 77793:
                  facultyteachesincourse+= "("+random.choice(["1006791006","1006791007"])+","+str(classNum)+"),\n"
           
studentsched += "\n\n\n"
studentsched += "INSERT INTO StudentSchedule\nVALUES"
for i in range(50):
      students.append(6791001+i)
for item in classes:
      classSize = random.randrange(3,11)
      for i in range(classSize):
            student = random.choice(students)
            if student not in roster:
                  roster.append(student)
      for i in range(len(roster)):
            studentsched += "(000"+str(roster[i])+","+str(item)+","+str(random.randrange(50,100))+"),\n"



studentsched += "\n\n\n"
studentsched += "INSERT INTO SemesterHasCourse\nVALUES"
studentsched += semesterhascourse
studentsched += "\n\n\n"
studentsched += "INSERT INTO Schedule\nVALUES"
studentsched += schedule
studentsched += "\n\n\n"
studentsched += "INSERT INTO FacultyTeachesInClass\nVALUES"
#faculty teaches in class
studentsched  += facultyteachesincourse



file=open('sched.txt','w')
file.write(studentsched)
file.close()      
