from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLineEdit, QPushButton, QSizePolicy, QTabWidget,
    QTableView, QTextEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(605, 533)

        # 设置整体的样式表
        style_sheet = """
        QWidget {
            background-color: #f8f8f8;  /* 设置整体背景色为淡灰色 */
            font-size: 13px;  /* 设置全局字体大小 */
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
        QLineEdit, QTextEdit, QComboBox {
            border: 1px solid #ccc;  /* 输入框、文本编辑框和下拉框边框 */
            border-radius: 3px;  /* 边框圆角 */
            padding: 3px;  /* 内边距 */
        }
        QTableView {
            border: 1px solid #ccc;  /* 表格视图边框 */
            gridline-color: #e0e0e0;  /* 表格内部网格线颜色 */
            alternate-background-color: #f0f0f0;  /* 表格交替行背景色 */
            background-color: white;  /* 表格整体背景色 */
            selection-background-color: #007bff;  /* 选中行背景色 */
            selection-color: white;  /* 选中行文字颜色 */
        }
        QHeaderView::section {
            background-color: #007bff;  /* 表头背景色 */
            color: white;  /* 表头文字颜色 */
            padding: 5px;  /* 表头内边距 */
            border-bottom: 1px solid #ccc;  /* 表头下边框 */
        }
        """
        Form.setStyleSheet(style_sheet)

        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")

        self.widget = QWidget()
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 100, -1, 100)

        self.num_edit = QLineEdit(self.widget)
        self.num_edit.setObjectName(u"num_edit")

        self.verticalLayout.addWidget(self.num_edit)

        self.name_edit = QLineEdit(self.widget)
        self.name_edit.setObjectName(u"name_edit")

        self.verticalLayout.addWidget(self.name_edit)

        self.major_combobox = QComboBox(self.widget)
        self.major_combobox.setObjectName(u"major_combobox")

        self.verticalLayout.addWidget(self.major_combobox)

        self.search_button = QPushButton(self.widget)
        self.search_button.setObjectName(u"search_button")

        self.verticalLayout.addWidget(self.search_button)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.tableView = QTableView(self.widget)
        self.tableView.setObjectName(u"tableView")

        self.horizontalLayout.addWidget(self.tableView)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.tabWidget.addTab(self.widget, "")

        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_2 = QHBoxLayout(self.tab)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.num_edit2 = QLineEdit(self.tab)
        self.num_edit2.setObjectName(u"num_edit2")

        self.verticalLayout_3.addWidget(self.num_edit2)

        self.total_score_edit = QTextEdit(self.tab)
        self.total_score_edit.setObjectName(u"total_score_edit")

        self.verticalLayout_3.addWidget(self.total_score_edit)

        self.search_button2 = QPushButton(self.tab)
        self.search_button2.setObjectName(u"search_button2")

        self.verticalLayout_3.addWidget(self.search_button2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.tableView_2 = QTableView(self.tab)
        self.tableView_2.setObjectName(u"tableView_2")

        self.horizontalLayout_2.addWidget(self.tableView_2)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.tabWidget.addTab(self.tab, "")

        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_3 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")

        self.search_button3 = QPushButton(self.tab_2)
        self.search_button3.setObjectName(u"search_button3")

        self.verticalLayout_4.addWidget(self.search_button3)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.tableView_3 = QTableView(self.tab_2)
        self.tableView_3.setObjectName(u"tableView_3")

        self.horizontalLayout_3.addWidget(self.tableView_3)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_2.addWidget(self.tabWidget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.num_edit.setPlaceholderText(QCoreApplication.translate("Form", u"\u5b66\u53f7\uff1a", None))
        self.name_edit.setPlaceholderText(QCoreApplication.translate("Form", u"\u59d3\u540d\uff1a", None))
        self.major_combobox.setPlaceholderText(QCoreApplication.translate("Form", u"\u4e13\u4e1a\uff1a", None))
        self.search_button.setText(QCoreApplication.translate("Form", u"\u67e5\u8be2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), QCoreApplication.translate("Form", u"\u5b66\u751f\u4fe1\u606f\u67e5\u8be2", None))
        self.num_edit2.setPlaceholderText(QCoreApplication.translate("Form", u"\u5b66\u53f7\uff1a", None))
        self.search_button2.setText(QCoreApplication.translate("Form", u"\u67e5\u8be2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"\u67e5\u8be2\u5b66\u751f\u8bfe\u7a0b\u4fe1\u606f", None))
        self.search_button3.setText(QCoreApplication.translate("Form", u"\u67e5\u8be2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\u67e5\u8be2\u5b66\u4e1a\u9884\u8b66\u4fe1\u606f", None))
    # retranslateUi