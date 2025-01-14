from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QGridLayout,
    QHBoxLayout, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(567, 450)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.input_button = QPushButton(Form)
        self.input_button.setObjectName(u"input_button")

        self.gridLayout.addWidget(self.input_button, 3, 0, 1, 2)

        self.date_edit = QDateEdit(Form)
        self.date_edit.setObjectName(u"date_edit")

        self.gridLayout.addWidget(self.date_edit, 1, 1, 1, 1)
        self.gridLayout.setContentsMargins(0,1,0,1)
        self.num_edit = QLineEdit(Form)
        self.num_edit.setObjectName(u"num_edit")

        self.gridLayout.addWidget(self.num_edit, 0, 0, 1, 1)

        self.gender_combobox = QComboBox(Form)
        self.gender_combobox.addItem("")
        self.gender_combobox.addItem("")
        self.gender_combobox.setObjectName(u"gender_combobox")

        self.gridLayout.addWidget(self.gender_combobox, 1, 0, 1, 1)

        self.name_edit = QLineEdit(Form)
        self.name_edit.setObjectName(u"name_edit")

        self.gridLayout.addWidget(self.name_edit, 0, 1, 1, 1)

        self.class_combobox = QComboBox(Form)
        self.class_combobox.setObjectName(u"class_combobox")

        self.gridLayout.addWidget(self.class_combobox, 2, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0,0,0,2)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.num_edit2 = QLineEdit(Form)
        self.num_edit2.setObjectName(u"num_edit2")

        self.horizontalLayout_2.addWidget(self.num_edit2)

        self.search_course_button = QPushButton(Form)
        self.search_course_button.setObjectName(u"search_course_button")

        self.horizontalLayout_2.addWidget(self.search_course_button)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.score_edit = QLineEdit(Form)
        self.score_edit.setObjectName(u"score_edit")

        self.gridLayout_2.addWidget(self.score_edit, 2, 0, 1, 1)

        self.score_input_button = QPushButton(Form)
        self.score_input_button.setObjectName(u"score_input_button")

        self.gridLayout_2.addWidget(self.score_input_button, 3, 0, 1, 1)

        self.course_combobox = QComboBox(Form)
        self.course_combobox.setObjectName(u"course_combobox")

        self.gridLayout_2.addWidget(self.course_combobox, 1, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout_2)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(2, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
        
        # 添加设置样式表的函数调用
        self.set_style_sheet(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.input_button.setText(QCoreApplication.translate("Form", u"\u4fe1\u606f\u5f55\u5165", None))
        self.num_edit.setPlaceholderText(QCoreApplication.translate("Form", u"\u5b66\u53f7\uff1a", None))
        self.gender_combobox.setItemText(0, QCoreApplication.translate("Form", u"\u7537", None))
        self.gender_combobox.setItemText(1, QCoreApplication.translate("Form", u"\u5973", None))

        self.gender_combobox.setPlaceholderText(QCoreApplication.translate("Form", u"\u6027\u522b\uff1a", None))
        self.name_edit.setPlaceholderText(QCoreApplication.translate("Form", u"\u59d3\u540d\uff1a", None))
        self.class_combobox.setPlaceholderText(QCoreApplication.translate("Form", u"\u73ed\u7ea7", None))
        self.num_edit2.setText("")
        self.num_edit2.setPlaceholderText(QCoreApplication.translate("Form", u"\u5b66\u53f7\uff1a", None))
        self.search_course_button.setText(QCoreApplication.translate("Form", u"\u67e5\u8be2\u8bfe\u7a0b", None))
        self.score_edit.setText("")
        self.score_edit.setPlaceholderText(QCoreApplication.translate("Form", u"\u6210\u7ee9\uff1a", None))
        self.score_input_button.setText(QCoreApplication.translate("Form", u"\u6210\u7ee9\u5f55\u5165", None))
        self.course_combobox.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bfe\u7a0bID", None))
        
    def set_style_sheet(self, Form):
        style_sheet = """
        QWidget {
            background-color: #f0f0f0;  /* 设置整体背景色为淡灰色 */
            font-size: 14px;  /* 设置全局字体大小 */
            font-family: Arial;  /* 设置全局字体家族 */
        }
        QPushButton {
            background-color: #007bff;  /* 按钮背景色为蓝色 */
            color: white;  /* 按钮文字颜色为白色 */
            border-radius: 5px;  /* 按钮边框圆角 */
            padding: 5px 10px;  /* 按钮内边距 */
        }
        QPushButton:hover {
            background-color: #0056b3;  /* 鼠标悬停时按钮背景色变深 */
        }
        QLineEdit, QComboBox {
            border: 1px solid #ccc;  /* 输入框和下拉框边框 */
            border-radius: 3px;  /* 边框圆角 */
            padding: 3px;  /* 内边距 */
        }
        QDateEdit {
            border: 1px solid #ccc;  /* 日期编辑框边框 */
            border-radius: 3px;  /* 边框圆角 */
            padding: 3px;  /* 内边距 */
        }
        """
        Form.setStyleSheet(style_sheet)
    # set_style_sheet

    # retranslateUi