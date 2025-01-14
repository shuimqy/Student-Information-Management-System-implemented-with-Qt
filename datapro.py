from sqlalchemy import create_engine
import pandas as pd
import random
from faker import Faker
engine = create_engine("mysql+pymysql://root:123456@localhost:3306/mydatabase")
student = pd.read_sql("SELECT StudentID FROM student", engine)['StudentID']
classID = pd.read_sql("SELECT ClassID FROM class", engine)

# print(classID['ClassID'])
# student-class表添加数据
""" 
class_list=classID['ClassID'].to_list()
student_class=[]
for stu in student:
  tmp=[]
  tmp.append(stu)
  tmp.append(random.choice(class_list))
  student_class.append(tmp)

# print(student_class)
df=pd.DataFrame(student_class,columns=['StudentID', 'ClassID'])
df.to_sql('student-class',engine,if_exists='append',index=False)
 """

 # teacher表添加数据
""" 
t=[]
n=0
n1=2400000
faker_cn = Faker('zh_CN')
while(n<68):
  n=n+1
  n1=n1+1
  tmp=[]
  tmp.append(n1)
  tmp.append(faker_cn.name())
  t.append(tmp)
df=pd.DataFrame(t,columns=['TeacherID', 'TeacherName'])
df.to_sql('teacher',engine,if_exists='append',index=False) 
 """
 # teacher-course表添加数据
""" 
teacher=pd.read_sql("select TeacherID from teacher",engine)
# print(teacher)
t_list=teacher['TeacherID'].to_list()
course=pd.read_sql("select CourseID from course",engine)['CourseID'].to_list()
# print(course)
tc=[]
t=0
for c in course:
  tmp=[]
  tmp.append(t_list[t])
  tmp.append(c)
  t=t+1
  tc.append(tmp)
df=pd.DataFrame(tc,columns=['TeacherID', 'CourseID'])
df.to_sql('teacher-course',engine,if_exists='append',index=False) 
 """

#添加grade表
"""
student_class=pd.read_sql("SELECT * FROM `student-class`", engine)
# print(student_class)
grade=[]
for ClassID,StuID in student_class.groupby('ClassID'):
  major=pd.read_sql(f"SELECT MajorID FROM class c where c.ClassID={ClassID}",engine)
  # print(major.values[0][0])
  # exit()
  course=pd.read_sql(f"SELECT CourseID FROM majorplan m where m.MajorID='{major.values[0][0]}'",engine)
  # print(course)
  for stu in StuID['StudentID']:
    for course_id in course['CourseID']:
      tmp=[]
      tmp.append(stu)
      tmp.append(course_id)
      tmp.append(random.randint(58,100))
      print(tmp)
      grade.append(tmp)
      # exit()
df=pd.DataFrame(grade,columns=['StudentID','CourseID','Score'])
df.to_sql('grade',engine,if_exists='append',index=False)
"""
