from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication,QTableView,QTextEdit,QWidget,QMessageBox,QLineEdit,QVBoxLayout,QStackedWidget
from PySide6.QtGui import QStandardItemModel,QStandardItem
import pymysql
import ui_main
import ui_load
import ui_welcome
import ui_search
class MyWindow(QWidget,ui_main.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #主界面初始化
        self.widget=欢迎_window()
        self.main_widget.addWidget(self.widget)
        self.main_widget.setCurrentIndex(2)
        #录入界面的初始化
        self.widget1=录入_window()
        self.main_widget.addWidget(self.widget1)
        #查询界面初始化
        self.widget2=查询_window()
        self.main_widget.addWidget(self.widget2)
        #主界面的按钮绑定
        self.stu_info_in.clicked.connect(self.录入_load)
        self.stu_info_search.clicked.connect(self.查询_load)
    def 录入_load(self):
        self.main_widget.setCurrentIndex(3)
    def 查询_load(self):
        self.main_widget.setCurrentIndex(4)
class 欢迎_window(QWidget,ui_welcome.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
class 录入_window(QWidget,ui_load.Ui_Form):
    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
        cursor.execute("SELECT ClassID FROM class")
        for i in cursor.fetchall():
            self.class_combobox.addItem(str(i[0]))
        self.input_button.clicked.connect(self.inPut)
        self.search_course_button.clicked.connect(self.course_combobox_init)
        self.score_input_button.clicked.connect(self.score_input)        
    def inPut(self):
        # print(self.class_combobox.currentIndex())
        if self.num_edit.text()!=''and self.class_combobox.currentIndex()!=-1 :
            print(f"({self.num_edit.text()},'{self.name_edit.text()}','{self.gender_combobox.currentText()}','{self.date_edit.text()}')")
            cursor.execute(f"INSERT INTO student(StudentID,StudentName,StudentGender,Birthday) \
                VALUES ({self.num_edit.text()},'{self.name_edit.text()}',\
                    '{self.gender_combobox.currentText()}','{self.date_edit.text()}')")
            cursor.execute(f"INSERT INTO `student-class`(StudentID,ClassID) \
                VALUES ({self.num_edit.text()},'{self.class_combobox.currentText()}')")  
            conn.commit()
            # cursor.execute(f"INSERT INTO student (StudentID,StudentName,StudentGender,Birthday) VALUES ({int(self.num_edit.text())},{str(self.name_edit.text())},{str(self.gender_combobox.currentText())},{str(self.date_edit.text())})")
        else:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("提示")
            msg_box.setText("学号和班级不能为空！！")
            msg_box.show()
            msg_box.exec()
    def score_input(self):
        if self.num_edit2.text()!='' and self.course_combobox.currentIndex()!=-1 and self.score_edit.text()!='':
            cursor.execute(f"INSERT INTO grade(StudentID,CourseID,Score) \
                           VALUES ({self.num_edit2.text()},'{self.course_combobox.currentText()}'\
                            ,{self.score_edit.text()})")
            conn.commit()
        else:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("提示")
            msg_box.setText("学号、课程、分数都不能为空！！")
            msg_box.show()
            msg_box.exec()
    def course_combobox_init(self):
        if self.num_edit2.text()!='':
            cursor.execute(f"SELECT mp.CourseID \
                           FROM student_major_view smv \
                           JOIN majorplan mp on mp.MajorID=smv.MajorID \
                           WHERE smv.StudentID={int(self.num_edit2.text())}")          
            for row in cursor.fetchall():
                self.course_combobox.addItem(row[0])
        else:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("提示")
            msg_box.setText("学号不能为空！！")
            msg_box.show()
            msg_box.exec()
class 查询_window(QWidget,ui_search.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tabWidget.setCurrentIndex(0)
        #选项表1
        self.search_button.clicked.connect(self.search)
        cursor.execute("SELECT MajorID FROM major")
        for row in cursor.fetchall():
            print(row)
            self.major_combobox.addItem(str(row[0]))
        self.model = QStandardItemModel()
        self.tableView.setModel(self.model)
        #选项表2
        self.search_button2.clicked.connect(self.searchClass)
        self.model2=QStandardItemModel()
        self.tableView_2.setModel(self.model2)
        #选项表3
        self.search_button3.clicked.connect(self.search3)
        self.model3=QStandardItemModel()
        self.tableView_3.setModel(self.model3)
    def search(self):
        if self.num_edit.text()!='' or self.name_edit.text()!=''or self.major_combobox.currentIndex()!=-1:
            if self.num_edit.text()!='':
                cursor.execute(f"SELECT * \
                               FROM student_major_view smv \
                               WHERE smv.StudentID={int(self.num_edit.text())}")
                self.model_clear()    
                for row in cursor.fetchall():
                    item1 = QStandardItem(str(row[0]))
                    item2 = QStandardItem(str(row[1]))
                    item3 = QStandardItem(str(row[2]))
                    item4 = QStandardItem(str(row[3]))
                    self.model.appendRow([item1, item2,item3,item4])
            elif self.name_edit.text()!='':
                cursor.execute(f"SELECT * \
                               FROM student_major_view smv \
                               WHERE smv.StudentName='{str(self.name_edit.text())}'")
                self.model_clear()    
                for row in cursor.fetchall():
                    item1 = QStandardItem(str(row[0]))
                    item2 = QStandardItem(str(row[1]))
                    item3 = QStandardItem(str(row[2]))
                    item4 = QStandardItem(str(row[3]))
                    self.model.appendRow([item1, item2,item3,item4])
            elif self.major_combobox.currentIndex!=-1:
                cursor.execute(f"SELECT * \
                               FROM student_major_view smv \
                               WHERE smv.MajorID='{str(self.major_combobox.currentText())}'")
                self.model_clear()
                for row in cursor.fetchall():
                    item1 = QStandardItem(str(row[0]))
                    item2 = QStandardItem(str(row[1]))
                    item3 = QStandardItem(str(row[2]))
                    item4 = QStandardItem(str(row[3]))
                    self.model.appendRow([item1, item2,item3,item4])
        else:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("提示")
            msg_box.setText("学号、姓名、专业至少有一个不为空！！")
            msg_box.show()
            msg_box.exec()
    def searchClass(self):
        if self.num_edit2.text()!='':
            self.model_clear2()
            cursor.execute(f"SELECT * FROM newview nv \
                           WHERE nv.StudentID={int(self.num_edit2.text())}")
            must_course={}
            must_course['score']=0
            must_course['credits']=0
            all_course={}
            all_course['score']=0
            all_course['credits']=0
            for row in cursor.fetchall():
                if str(row[2])=='必修':
                    must_course['score']+=int(row[6])*int(row[5])
                    must_course['credits']+=int(row[5])
                all_course['score']+=int(row[6])*int(row[5])
                all_course['credits']+=int(row[5])
                item1 = QStandardItem(str(row[1]))
                item2 = QStandardItem(str(row[2]))
                item3 = QStandardItem(str(row[3]))
                item4 = QStandardItem(str(row[4]))
                item5 = QStandardItem(str(row[5]))
                item6 = QStandardItem(str(row[6]))
                self.model2.appendRow([item1, item2,item3,item4,item5,item6])
            self.total_score_edit.clear()
            self.total_score_edit.setText(f'必修课程平均成绩：{round(must_course['score']/must_course['credits'],2)}\n所有课程平均成绩：{round(all_course['score']/all_course['credits'],2)}')
        else:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("提示")
            msg_box.setText("学号不能为空！！")
            msg_box.show()
            msg_box.exec()
    def search3(self):
        self.model_clear3()
        cursor.execute("SELECT nv.StudentID,COUNT(nv.CourseName),SUM(nv.Credits) \
                       FROM newview nv where nv.Score<60 \
                       GROUP BY nv.StudentID \
                       HAVING SUM(nv.Credits)>2")
        for row in cursor.fetchall():
            item1 = QStandardItem(str(row[0]))
            item2 = QStandardItem(str(row[1]))
            item3 = QStandardItem(str(row[2]))
            self.model3.appendRow([item1, item2,item3])
    def model_clear(self):
        self.model.clear()
        self.headerItem11 = QStandardItem("学号")
        self.headerItem12 = QStandardItem("姓名")
        self.headerItem13 = QStandardItem("班级")
        self.headerItem14 = QStandardItem("专业")
        self.model.setHorizontalHeaderItem(0, self.headerItem11)
        self.model.setHorizontalHeaderItem(1, self.headerItem12)
        self.model.setHorizontalHeaderItem(2, self.headerItem13)
        self.model.setHorizontalHeaderItem(3, self.headerItem14)
    def model_clear2(self):
        self.model2.clear()
        self.headerItem21 = QStandardItem("课程名")
        self.headerItem22 = QStandardItem("性质")
        self.headerItem23 = QStandardItem("任课老师")
        self.headerItem24 = QStandardItem("学期")
        self.headerItem25 = QStandardItem("学分")
        self.headerItem26 = QStandardItem("成绩")
        self.model2.setHorizontalHeaderItem(0, self.headerItem21)
        self.model2.setHorizontalHeaderItem(1, self.headerItem22)
        self.model2.setHorizontalHeaderItem(2, self.headerItem23)
        self.model2.setHorizontalHeaderItem(3, self.headerItem24)
        self.model2.setHorizontalHeaderItem(4, self.headerItem25)
        self.model2.setHorizontalHeaderItem(5, self.headerItem26)
    def model_clear3(self):
        self.model3.clear()
        self.headerItem31 = QStandardItem("学号")
        self.headerItem32 = QStandardItem("挂科课程数")
        self.headerItem33 = QStandardItem("挂科总学分")
        self.model3.setHorizontalHeaderItem(0,self.headerItem31)
        self.model3.setHorizontalHeaderItem(1,self.headerItem32)
        self.model3.setHorizontalHeaderItem(2,self.headerItem33)
if __name__ == '__main__':
    conn = pymysql.connect(
    host="localhost",
    user="root",
    password="123456",
    database="mydatabase"
)
    cursor = conn.cursor()
    app = QApplication([])
    window=MyWindow()
    window.show()
    app.exec()
    print(111)
    cursor.close()
    conn.close()