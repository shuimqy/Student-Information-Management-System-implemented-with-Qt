from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLayout, QPushButton,
    QSizePolicy, QStackedWidget, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(698, 578)

        # 设置整体的样式表
        style_sheet = """
        QWidget {
            background-color: #f5f5f5;  /* 整体背景色设置为淡灰色 */
            font-size: 14px;  /* 全局字体大小 */
            font-family: Arial;  /* 全局字体家族 */
        }
        QPushButton {
            background-color: #007bff;  /* 按钮背景色为蓝色 */
            color: white;  /* 按钮文字颜色为白色 */
            border-radius: 5px;  /* 按钮边框圆角 */
            padding: 8px 15px;  /* 按钮内边距 */
            margin: 5px;  /* 按钮外边距，让按钮之间有间隔 */
        }
        QPushButton:hover {
            background-color: #0056b3;  /* 鼠标悬停时按钮背景色变深 */
        }
        QStackedWidget {
            border: 1px solid #ccc;  /* 堆叠部件添加边框 */
            border-radius: 3px;  /* 边框圆角 */
            background-color: white;  /* 堆叠部件内部背景色设为白色 */
        }
        """
        Form.setStyleSheet(style_sheet)

        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.toolbar_layout = QHBoxLayout()
        self.toolbar_layout.setObjectName(u"toolbar_layout")
        self.toolbar_layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.toolbar_layout.setContentsMargins(10, 10, 10, 0)  # 设置水平布局的外边距，使按钮与窗口边缘有间隔
        self.stu_info_in = QPushButton(Form)
        self.stu_info_in.setObjectName(u"stu_info_in")

        self.toolbar_layout.addWidget(self.stu_info_in)

        self.stu_info_search = QPushButton(Form)
        self.stu_info_search.setObjectName(u"stu_info_search")

        self.toolbar_layout.addWidget(self.stu_info_search)

        self.verticalLayout.addLayout(self.toolbar_layout)

        self.main_layout = QVBoxLayout()
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.main_layout.setContentsMargins(10, 0, 10, 10)  # 设置垂直布局的外边距，调整内部部件与窗口边缘间隔
        self.main_widget = QStackedWidget(Form)
        self.main_widget.setObjectName(u"main_widget")

        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setEnabled(False)
        self.main_widget.addWidget(self.page)

        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setEnabled(False)
        self.main_widget.addWidget(self.page_2)

        self.main_layout.addWidget(self.main_widget)

        self.verticalLayout.addLayout(self.main_layout)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)

        self.main_widget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.stu_info_in.setText(QCoreApplication.translate("Form", u"\u5b66\u751f\u4fe1\u606f\u5f55\u5165", None))
        self.stu_info_search.setText(QCoreApplication.translate("Form", u"\u5b66\u751f\u4fe1\u606f\u67e5\u8be2", None))
    # retranslateUi