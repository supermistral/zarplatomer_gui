# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_design.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

'''class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 1000)
        #MainWindow.setFixedSize(MainWindow.size())
        MainWindow.setStyleSheet("QPushButton#button_menu {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QPushButton#button_main {\n"
"    background-color: #FFC795;\n"
"    border-width: 3px;\n"
"    border-top-right-radius: 40px;\n"
"    border-bottom-right-radius: 16px;\n"
"    border-top-left-radius: 16px;\n"
"    border-color: #BA3800;\n"
"    border-style: inset;\n"
"    min-height: 50px;\n"
"    max-width: 300px;\n"
"    margin: 10px;\n"
"    border-bottom-left-radius: 40px;\n"
"}\n"
"\n"
"QPushButton#button_main:hover {\n"
"    background-color: #FFEAD1;\n"
"    background-color :qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.454545 rgba(255, 199, 149, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-style: outset;\n"
"    border-color: white;\n"
"    border-width: 3px;\n"
"    background-color: #FFB26E;\n"
"    background-color: #E1AD80;\n"
"    background-color: #EAAC76;\n"
"    background-color: #FFD6B2;\n"
"    font-size: 21px;\n"
"    \n"
"}\n"
"\n"
"QPushButton#button_main:pressed {\n"
"    background-color: qlineargradient(spread:reflect, x1:1, y1:0.562, x2:1, y2:0, stop:0.397727 rgba(225, 131, 76, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-color: #FF8247;\n"
"    border-style: solid;\n"
"    background-color: #E68F42;\n"
"}\n"
"\n"
"QMainWindow {\n"
"    background-color: #FFF6FE;\n"
"}\n"
"/*COMBOBOX*/\n"
"\n"
"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding-left: 5px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QComboBox#combobox1 {\n"
"    border-top-right-radius: 10px;\n"
"}\n"
"\n"
"QComboBox#combobox2 {\n"
"    border-bottom-right-radius: 10px;\n"
"}\n"
"\n"
"QComboBox#combobox1:hover, QComboBox#combobox2:hover  {\n"
"    background-color: #FFC699;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: dashed; \n"
"}\n"
"\n"
"QComboBox#combobox1:on, QComboBox#combobox2:on {\n"
"    margin-bottom: 5px;\n"
"    padding-left: 15px;\n"
"    padding-bottom: 2px;\n"
"    background-color: white;\n"
"    border-width: 1px;\n"
"}\n"
"QComboBox#combobox2:on {\n"
"    border-bottom-right-radius: 3px;\n"
"    border-top-right-radius: 10px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    padding-top: 3px;\n"
"    padding-left: 3px;\n"
"    margin-left: 0px;                                          /*смещение выползающего меню*/\n"
"    border-top: 2px dashed #A4A4A4;\n"
"    border-left: 2px dashed #A4A4A4;\n"
"    selection-background-color: #FFF9AD;\n"
"    selection-color: #9E54FF;\n"
"    background-color: white; \n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QListView::item {\n"
"    height: 30px;\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"    background-color: #FFF9AD;\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"    background-color: #FFF9AD;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: 1px solid black;\n"
"    border-top-left-radius: 15px;\n"
"    border-bottom-left-radius: 30px;\n"
"}\n"
"\n"
"QPushButton#button_valute {\n"
"    background-color: #B3FF9F;\n"
"    border: 2px outset black;\n"
"    border-radius: 3px;\n"
"    border-bottom-right-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"}\n"
"\n"
"QPushButton#button_valute:hover {\n"
"    background-color: #D7FFCD;\n"
"    border-width: 2px;\n"
"    border-color: lightgray;\n"
"    font-size: 16px;\n"
"    border-style: solid\n"
"}\n"
"\n"
"QPushButton#button_valute:pressed {\n"
"    background-color: #84CD72;\n"
"}\n"
"\n"
"QLabel#label {\n"
"    margin-top: 10px;\n"
"    padding-top: 5px;\n"
"    padding-left: 12px;\n"
"    border: 1px dotted lightgray;\n"
"    border-radius: 30px;\n"
"    background-color: #DCFFBD;\n"
"    line-height: 20pt;\n"
"    font-size: 18px;\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    background-color: #F5F5F5;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #05B8CC;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(-1, -1, 15, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 0, -1, 250)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(-1, 20, -1, 40)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.show_start_text = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.show_start_text.sizePolicy().hasHeightForWidth())
        self.show_start_text.setSizePolicy(sizePolicy)
        self.show_start_text.setMinimumSize(QtCore.QSize(0, 100))
        self.show_start_text.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.show_start_text.setFont(font)
        self.show_start_text.setFrameShadow(QtWidgets.QFrame.Plain)
        self.show_start_text.setTextFormat(QtCore.Qt.PlainText)
        self.show_start_text.setAlignment(QtCore.Qt.AlignCenter)
        self.show_start_text.setObjectName("show_start_text")
        self.horizontalLayout_8.addWidget(self.show_start_text)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(20)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QtCore.QSize(680, 45))
        self.lineEdit.setMaximumSize(QtCore.QSize(680, 45))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit.setFont(font)
        self.lineEdit.setAccessibleName("")
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(100)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_7.addWidget(self.lineEdit)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_7)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(8)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.combobox1 = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combobox1.sizePolicy().hasHeightForWidth())
        self.combobox1.setSizePolicy(sizePolicy)
        self.combobox1.setMinimumSize(QtCore.QSize(150, 30))
        self.combobox1.setMaximumSize(QtCore.QSize(150, 30))
        self.combobox1.setSizeIncrement(QtCore.QSize(0, 0))
        self.combobox1.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.combobox1.setFont(font)
        self.combobox1.setAccessibleName("")
        self.combobox1.setAccessibleDescription("")
        self.combobox1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.combobox1.setMaxVisibleItems(2)
        self.combobox1.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.combobox1.setObjectName("combobox1")
        self.combobox1.addItem("")
        self.combobox1.addItem("")
        self.verticalLayout_3.addWidget(self.combobox1)
        self.combobox2 = QtWidgets.QComboBox(self.centralwidget)
        self.combobox2.setMinimumSize(QtCore.QSize(150, 30))
        self.combobox2.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.combobox2.setFont(font)
        self.combobox2.setMaxVisibleItems(2)
        self.combobox2.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.combobox2.setObjectName("combobox2")
        self.combobox2.addItem("")
        self.combobox2.addItem("")
        self.verticalLayout_3.addWidget(self.combobox2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 20, -1, 10)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.button_main = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_main.sizePolicy().hasHeightForWidth())
        self.button_main.setSizePolicy(sizePolicy)
        self.button_main.setMinimumSize(QtCore.QSize(0, 76))
        self.button_main.setMaximumSize(QtCore.QSize(326, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.button_main.setFont(font)
        self.button_main.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.button_main.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.button_main.setDefault(False)
        self.button_main.setObjectName("button_main")
        self.horizontalLayout_4.addWidget(self.button_main)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 6, -1, 6)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setMinimumSize(QtCore.QSize(600, 30))
        self.progressBar.setMaximumSize(QtCore.QSize(600, 30))
        self.progressBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout.addWidget(self.progressBar, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 6, 0, 6)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.progressBar2 = QtWidgets.QProgressBar(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar2.sizePolicy().hasHeightForWidth())
        self.progressBar2.setSizePolicy(sizePolicy)
        self.progressBar2.setMinimumSize(QtCore.QSize(600, 30))
        self.progressBar2.setMaximumSize(QtCore.QSize(600, 30))
        self.progressBar2.setProperty("value", 0)
        self.progressBar2.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar2.setTextVisible(False)
        self.progressBar2.setObjectName("progressBar2")
        self.horizontalLayout_2.addWidget(self.progressBar2, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 6, -1, 6)
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.progressBar3 = QtWidgets.QProgressBar(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar3.sizePolicy().hasHeightForWidth())
        self.progressBar3.setSizePolicy(sizePolicy)
        self.progressBar3.setMinimumSize(QtCore.QSize(600, 30))
        self.progressBar3.setMaximumSize(QtCore.QSize(600, 30))
        self.progressBar3.setProperty("value", 0)
        self.progressBar3.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar3.setTextVisible(False)
        self.progressBar3.setObjectName("progressBar3")
        self.horizontalLayout_3.addWidget(self.progressBar3, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, 20, -1, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem2)
        self.button_menu = QtWidgets.QPushButton(self.centralwidget)
        self.button_menu.setMinimumSize(QtCore.QSize(100, 50))
        self.button_menu.setMaximumSize(QtCore.QSize(100, 50))
        self.button_menu.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img_menu.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_menu.setIcon(icon)
        self.button_menu.setIconSize(QtCore.QSize(70, 70))
        self.button_menu.setObjectName("button_menu")
        self.verticalLayout_5.addWidget(self.button_menu, 0, QtCore.Qt.AlignCenter|QtCore.Qt.AlignTop)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem3)
        self.button_valute = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_valute.sizePolicy().hasHeightForWidth())
        self.button_valute.setSizePolicy(sizePolicy)
        self.button_valute.setMinimumSize(QtCore.QSize(250, 30))
        self.button_valute.setMaximumSize(QtCore.QSize(250, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button_valute.setFont(font)
        self.button_valute.setObjectName("button_valute")
        self.verticalLayout_4.addWidget(self.button_valute, 0, QtCore.Qt.AlignLeft)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(250, 100))
        self.label.setMaximumSize(QtCore.QSize(250, 100))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout_6.addLayout(self.verticalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.combobox1.setView(QtWidgets.QListView(self.combobox1))
        self.combobox2.setView(QtWidgets.QListView(self.combobox2))

        self.combobox1.setToolTip("""Этот параметр влияет на точность поиска.

При СТРОГОМ поиске будет собрана информация только по тем вакансиям/резюме,
в наименованиях которых были найдены введенные слова из запроса.

При НЕСТРОГОМ поиске информация собирается по всякой вакансии/резюме,
где присутствуют введенные данные (включая описание, требования, наименование, места работы и т.п.)""")
        self.combobox2.setToolTip("""Этот параметр влияет на скорость выполнения программы и точность построения графика superjob.

При НЕПОЛНОМ поиске веб-сервис superjob.ru будет рассмотрен только за последние 30 дней.

При ПОЛНОМ поиске веб-сервис superjob.ru будет рассмотрен за весь период публикации существующих резюме""")
        #QtWidgets.QListView.setSpacing(self.combobox1, 20)
        self.label.hide()
        self.button_valute.hide()
        self.button_menu.clicked.connect(self.open_menu)
    
    def open_menu(self):
        if self.button_valute.isHidden():
            self.button_valute.show()
            self.label.show()
            self.verticalLayout.setContentsMargins(-1, 0, -1, 200)
            self.verticalLayout_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        else:
            self.button_valute.hide()
            self.label.hide()
            self.verticalLayout.setContentsMargins(-1, 0, -1, 250)
            self.verticalLayout_5.setAlignment(QtCore.Qt.AlignCenter|QtCore.Qt.AlignTop)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.show_start_text.setText(_translate("MainWindow", "Введите профессию"))
        self.combobox1.setCurrentText(_translate("MainWindow", "строгий поиск"))
        self.combobox1.setItemText(0, _translate("MainWindow", "строгий поиск"))
        self.combobox1.setItemText(1, _translate("MainWindow", "нестрогий поиск"))
        self.combobox2.setItemText(0, _translate("MainWindow", "неполный поиск"))
        self.combobox2.setItemText(1, _translate("MainWindow", "полный поиск"))
        self.button_main.setText(_translate("MainWindow", "Хочу результат"))
        self.button_valute.setText(_translate("MainWindow", "Узнать курс валют"))
        self.label.setText(_translate("MainWindow", "USD:\n"
"EUR:\n"
"Обновлено "))'''

'''class Ui_MainWindow_shedule(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 1000)
        MainWindow.setMaximumSize(QtCore.QSize(1000, 1000))
        MainWindow.setStyleSheet("QTabWidget::tab-bar {\n"
"    alignment: center;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    width: 266px;\n"
"    height: 45px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(100, 0, 800, 1000))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.tabWidget.setFont(font)
        self.tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab.sizePolicy().hasHeightForWidth())
        self.tab.setSizePolicy(sizePolicy)
        self.tab.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setKerning(True)
        self.tab.setFont(font)
        self.tab.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tab.setStyleSheet("")
        self.tab.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        #img = QtGui.QPixmap('from_jobfilter.jpg')
        #img = img.scaledToWidth(800)
        #self.label.setPixmap(img)
        #self.label.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(230, 600, 340, 60))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(0, 650, 800, 52))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.tab, "")
        self.tab2 = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setPointSize(16)
        self.tab2.setFont(font)
        self.tab2.setObjectName("tab2")
        self.label_4 = QtWidgets.QLabel(self.tab2)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.tabWidget.addTab(self.tab2, "")
        self.tab3 = QtWidgets.QWidget()
        self.tab3.setObjectName("tab3")
        self.label_5 = QtWidgets.QLabel(self.tab3)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.tabWidget.addTab(self.tab3, "")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        #self.pushButton.setGeometry(QtCore.QRect(950, 440, 51, 131))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setIcon(QtGui.QIcon('button2.jpg'))
        self.pushButton.setIconSize(QtCore.QSize(500, 500))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Ключевые навыки"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "headhunter.ru"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MainWindow", "jobfilter.ru"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), _translate("MainWindow", "superjob.ru"))'''

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
#        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 1000)
        MainWindow.setFixedSize(MainWindow.size())
        MainWindow.setStyleSheet("QPushButton#button_menu {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QPushButton#button_main {\n"
"    background-color: #FFC795;\n"
"    border-width: 3px;\n"
"    border-top-right-radius: 40px;\n"
"    border-bottom-right-radius: 16px;\n"
"    border-top-left-radius: 16px;\n"
"    border-color: #BA3800;\n"
"    border-style: inset;\n"
"    min-height: 50px;\n"
"    max-width: 300px;\n"
"    margin: 10px;\n"
"    border-bottom-left-radius: 40px;\n"
"}\n"
"\n"
"QPushButton#button_main:hover {\n"
"    border-style: outset;\n"
"    border-color: white;\n"
"    border-width: 3px;\n"
"    background-color: #FFD6B2;\n"
"    font-size: 21px;\n"
"    \n"
"}\n"
"\n"
"QPushButton#button_main:pressed {\n"
"    border-color: #FF8247;\n"
"    border-style: solid;\n"
"    background-color: #E68F42;\n"
"}\n"
"\n"
"QMainWindow {\n"
"    background-color: #FFF6FE;\n"
"}\n"
"/*COMBOBOX*/\n"
"\n"
"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding-left: 5px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QComboBox#combobox1 {\n"
"    border-top-right-radius: 10px;\n"
"}\n"
"\n"
"QComboBox#combobox2 {\n"
"    border-bottom-right-radius: 10px;\n"
"}\n"
"\n"
"QComboBox#combobox1:hover, QComboBox#combobox2:hover  {\n"
"    background-color: #FFC699;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: dashed; \n"
"}\n"
"\n"
"QComboBox#combobox1:on, QComboBox#combobox2:on { /* shift the text when the popup opens */\n"
"    margin-bottom: 5px;\n"
"    padding-left: 15px;\n"
"    padding-bottom: 2px;\n"
"    background-color: white;\n"
"    border-width: 1px;\n"
"}\n"
"QComboBox#combobox2:on {\n"
"    border-bottom-right-radius: 3px;\n"
"    border-top-right-radius: 10px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    padding-top: 3px;\n"
"    padding-left: 3px;\n"
"    margin-left: 0px;                                          /*смещение выползающего меню*/\n"
"    border-top: 2px dashed #A4A4A4;\n"
"    border-left: 2px dashed #A4A4A4;\n"
"    selection-background-color: #FFF9AD;\n"
"    selection-color: #9E54FF;\n"
"    background-color: white; \n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: 1px solid black;\n"
"    border-top-left-radius: 15px;\n"
"    border-bottom-left-radius: 30px;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px groove #FF8126;\n"
"    border-color: #FF9819;\n"
"}\n"
"\n"
"QListView::item {\n"
"    height: 30px;\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"    background-color: #FFF9AD;\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"    background-color: #FFF9AD;\n"
"}\n"
"\n"
"QPushButton#button_valute {\n"
"    background-color: #B3FF9F;\n"
"    border: 2px outset black;\n"
"    border-radius: 3px;\n"
"    border-bottom-right-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0.074, x2:1, y2:0, stop:0 rgba(238, 253, 168, 243), stop:1 rgba(255, 216, 216, 255));\n"
"}\n"
"\n"
"QPushButton#button_valute:hover {\n"
"    background-color: #D7FFCD;\n"
"    border-width: 2px;\n"
"    border-color: lightgray;\n"
"    font-size: 16px;\n"
"    border-style: solid;\n"
"    background: #F9FFCB;\n"
"    background: rgba(255, 216, 216, 255);\n"
"}\n"
"\n"
"QPushButton#button_valute:pressed {\n"
"    background-color: #84CD72;\n"
"    background: #debbba;\n"
"}\n"
"\n"
"QLabel#label {\n"
"    width: 250px;\n"
"    height: 100px;\n"
"    margin-top: 10px;\n"
"    padding-top: 5px;\n"
"    padding-left: 12px;\n"
"    border: 1px dotted lightgray;\n"
"    border-radius: 30px;\n"
"    background-color: #DCFFBD;\n"
"    line-height: 20pt;\n"
"    font-size: 18px;\n"
"    font-weight: 500;\n"
"    background: #DEFFA0;\n"
"    background: #F6FFBC; \n"
"    background: qlineargradient(spread:pad, x1:0, y1:0.074, x2:1, y2:0, stop:0 rgba(253, 246, 188, 254), stop:0.903409 rgba(255, 255, 255, 255));\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0.074, x2:1, y2:0, stop:0 rgba(238, 253, 168, 243), stop:1 rgba(255, 216, 216, 255));\n"
"}\n"
"\n"
"QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    background-color: #F5F5F5;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #05B8CC;\n"
"}\n"
"\n"
"QSpinBox {\n"
"    width: 200px;\n"
"    font-size: 18px;\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    color: #4E4E4E;\n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    width: 0px;\n"
"    height: 0px;\n"
"}\n"
"\n"
"QSpinBox::hover {\n"
"    border: 2px groove #FF8126;\n"
"    border-color: #FF9819;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 2px solid qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(238, 253, 168, 243), stop:1 rgba(255, 216, 216, 255));\n"
"    height: 10px; \n"
"    background: #FFF8B9;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0.074, x2:1, y2:0, stop:0 rgba(238, 253, 168, 243), stop:1 rgba(255, 216, 216, 255));\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    border: 5px solid gray;\n"
"    width: 16px;\n"
"    height: 20px;\n"
"    margin: -6px 0px; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 9px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: #FFE236;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background: #D3BA2A;\n"
"    border-color: #606060;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(-1, -1, 15, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(-1, 20, -1, 40)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.show_start_text = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.show_start_text.sizePolicy().hasHeightForWidth())
        self.show_start_text.setSizePolicy(sizePolicy)
        self.show_start_text.setMinimumSize(QtCore.QSize(0, 100))
        self.show_start_text.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.show_start_text.setFont(font)
        self.show_start_text.setFrameShadow(QtWidgets.QFrame.Plain)
        self.show_start_text.setTextFormat(QtCore.Qt.PlainText)
        self.show_start_text.setAlignment(QtCore.Qt.AlignCenter)
        self.show_start_text.setObjectName("show_start_text")
        self.horizontalLayout_8.addWidget(self.show_start_text)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(20)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QtCore.QSize(680, 45))
        self.lineEdit.setMaximumSize(QtCore.QSize(680, 45))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit.setFont(font)
        self.lineEdit.setAccessibleName("")
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(100)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_7.addWidget(self.lineEdit)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_7)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(8)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.combobox1 = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combobox1.sizePolicy().hasHeightForWidth())
        self.combobox1.setSizePolicy(sizePolicy)
        self.combobox1.setMinimumSize(QtCore.QSize(150, 30))
        self.combobox1.setMaximumSize(QtCore.QSize(150, 30))
        self.combobox1.setSizeIncrement(QtCore.QSize(0, 0))
        self.combobox1.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.combobox1.setFont(font)
        self.combobox1.setAccessibleName("")
        self.combobox1.setAccessibleDescription("")
        self.combobox1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.combobox1.setMaxVisibleItems(2)
        self.combobox1.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.combobox1.setObjectName("combobox1")
        self.combobox1.addItem("")
        self.combobox1.addItem("")
        self.verticalLayout_3.addWidget(self.combobox1)
        self.combobox2 = QtWidgets.QComboBox(self.centralwidget)
        self.combobox2.setMinimumSize(QtCore.QSize(150, 30))
        self.combobox2.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.combobox2.setFont(font)
        self.combobox2.setMaxVisibleItems(2)
        self.combobox2.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.combobox2.setObjectName("combobox2")
        self.combobox2.addItem("")
        self.combobox2.addItem("")
        self.verticalLayout_3.addWidget(self.combobox2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 20, -1, 10)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.button_main = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_main.sizePolicy().hasHeightForWidth())
        self.button_main.setSizePolicy(sizePolicy)
        self.button_main.setMinimumSize(QtCore.QSize(0, 76))
        self.button_main.setMaximumSize(QtCore.QSize(326, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.button_main.setFont(font)
        self.button_main.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.button_main.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.button_main.setDefault(False)
        self.button_main.setObjectName("button_main")
        self.horizontalLayout_4.addWidget(self.button_main)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 6, -1, 6)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setMinimumSize(QtCore.QSize(600, 30))
        self.progressBar.setMaximumSize(QtCore.QSize(600, 30))
        self.progressBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout.addWidget(self.progressBar, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 6, 0, 6)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.progressBar2 = QtWidgets.QProgressBar(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar2.sizePolicy().hasHeightForWidth())
        self.progressBar2.setSizePolicy(sizePolicy)
        self.progressBar2.setMinimumSize(QtCore.QSize(600, 30))
        self.progressBar2.setMaximumSize(QtCore.QSize(600, 30))
        self.progressBar2.setProperty("value", 0)
        self.progressBar2.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar2.setTextVisible(False)
        self.progressBar2.setObjectName("progressBar2")
        self.horizontalLayout_2.addWidget(self.progressBar2, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 6, -1, 0)
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.progressBar3 = QtWidgets.QProgressBar(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar3.sizePolicy().hasHeightForWidth())
        self.progressBar3.setSizePolicy(sizePolicy)
        self.progressBar3.setMinimumSize(QtCore.QSize(600, 30))
        self.progressBar3.setMaximumSize(QtCore.QSize(600, 30))
        self.progressBar3.setProperty("value", 0)
        self.progressBar3.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar3.setTextVisible(False)
        self.progressBar3.setObjectName("progressBar3")
        self.horizontalLayout_3.addWidget(self.progressBar3, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 350))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.button_menu = QtWidgets.QPushButton(self.frame)
        self.button_menu.setGeometry(QtCore.QRect(280, 30, 100, 50))
        self.button_menu.setMinimumSize(QtCore.QSize(100, 50))
        self.button_menu.setMaximumSize(QtCore.QSize(100, 50))
        self.button_menu.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images\\img_menu_normal.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_menu.setIcon(icon)
        self.button_menu.setIconSize(QtCore.QSize(60, 60))
        self.button_menu.setObjectName("button_menu")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setEnabled(True)
#        self.label.setGeometry(QtCore.QRect(450, 40, 250, 100))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
#        self.label.setMinimumSize(QtCore.QSize(250, 100))
#        self.label.setMaximumSize(QtCore.QSize(250, 100))
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.button_valute = QtWidgets.QPushButton(self.frame)
#        self.button_valute.setGeometry(QtCore.QRect(450, 0, 250, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_valute.sizePolicy().hasHeightForWidth())
        self.button_valute.setSizePolicy(sizePolicy)
#        self.button_valute.setMinimumSize(QtCore.QSize(250, 30))
#        self.button_valute.setMaximumSize(QtCore.QSize(250, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button_valute.setFont(font)
        self.button_valute.setObjectName("button_valute")
        self.spinBox = QtWidgets.QSpinBox(self.frame)
#        self.spinBox.setGeometry(QtCore.QRect(230, 170, 200, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
#        self.spinBox.setMinimumSize(QtCore.QSize(0, 30))
#        self.spinBox.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.spinBox.setFont(font)
        self.spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox.setSpecialValueText("")
        self.spinBox.setPrefix("")
        self.spinBox.setMaximum(300000)
        self.spinBox.setMinimum(30000)
        self.spinBox.setSingleStep(100)
        self.spinBox.setObjectName("spinBox")
        self.horizontalSlider = QtWidgets.QSlider(self.frame)
#        self.horizontalSlider.setGeometry(QtCore.QRect(180, 220, 300, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider.sizePolicy().hasHeightForWidth())
        self.horizontalSlider.setSizePolicy(sizePolicy)
#        self.horizontalSlider.setMinimumSize(QtCore.QSize(0, 25))
#        self.horizontalSlider.setMaximumSize(QtCore.QSize(300, 25))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setMaximum(300000)
        self.horizontalSlider.setMinimum(30000)
        self.verticalLayout_2.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.combobox1.setToolTip("""Этот параметр влияет на точность поиска.

При СТРОГОМ поиске будет собрана информация только по тем вакансиям/резюме,
в наименованиях которых были найдены введенные слова из запроса.

При НЕСТРОГОМ поиске информация собирается по всякой вакансии/резюме,
где присутствуют введенные данные (включая описание, требования, наименование, места работы и т.п.)""")
        self.combobox2.setToolTip("""Этот параметр влияет на скорость выполнения программы и точность построения графика superjob.

При НЕПОЛНОМ поиске веб-сервис superjob.ru будет рассмотрен только за последние 30 дней.

При ПОЛНОМ поиске веб-сервис superjob.ru будет рассмотрен за весь период публикации существующих резюме""")
        self.horizontalSlider.valueChanged.connect(self.change_max_zp)
        self.button_menu.move(425, 0)
        self.label.hide()
        self.button_valute.hide()
        self.horizontalSlider.hide()
        self.spinBox.hide()
        self.button_menu.clicked.connect(self.open_menu)
        self.combobox1.setView(QtWidgets.QListView(self.combobox1))
        self.combobox2.setView(QtWidgets.QListView(self.combobox2))
    
    def open_menu(self):
        if self.button_valute.isHidden():
            self.animate_button_menu((425, 375), (425, 505), (0, 0, 250, 30), False, (0, 0, 250, 100), (0, 30), (0, 160), (0, 0, 200, 30), (505, 530), (0, 0, 300, 25), (505, 480), (0, 190))
            self.button_valute.show()
            self.label.show()
            self.horizontalSlider.show()
            self.spinBox.show()
        else:
            self.animate_button_menu((375, 425), (505, 505), (250, 30, 0, 30), True, (250, 100, 0, 100), (30, 30), (160, 160), (200, 30, 0, 30), (530, 505), (300, 25, 0, 25), (480, 505), (190, 190))
            #self.button_valute.hide()
            #self.label.hide()
#            self.horizontalSlider.hide()
#            self.spinBox.hide()

    def animate_button_menu(self, dist, dist1, size1, finish, size2, h_l, h_l1, size3, dist3, size4, dist4, h_l2):
        
        self.anim = QtCore.QPropertyAnimation(self.button_menu, b"geometry")
        self.anim2 = QtCore.QPropertyAnimation(self.button_valute, b"geometry")
        self.anim2.setDuration(800)
        self.anim2.setKeyValueAt(0, QtCore.QRect(dist1[0], 0, size1[0], size1[1]))
        self.anim.setDuration(400)
      #  self.anim.setStartValue(QtCore.QRect(400, 30, 100, 100))
      #  self.anim.setEndValue(QtCore.QRect(200, 30, 100, 100))
        self.anim.setKeyValueAt(0, QtCore.QRect(dist[0], 0, 100, 100))
        self.anim.setKeyValueAt(1, QtCore.QRect(dist[1], 0, 100, 100))
        self.anim.setEasingCurve(QtCore.QEasingCurve.OutCubic)
        self.anim2.setKeyValueAt(1, QtCore.QRect(dist1[1], 0, size1[2], size1[3]))
        self.anim2.setEasingCurve(QtCore.QEasingCurve.OutCirc)
        self.anim3 = QtCore.QPropertyAnimation(self.label, b"geometry")
        self.anim3.setDuration(800)
        self.anim3.setKeyValueAt(0, QtCore.QRect(dist1[0], h_l[0], size2[0], size2[1]))
        self.anim3.setKeyValueAt(1, QtCore.QRect(dist1[1], h_l[1], size2[2], size2[3]))
        self.anim3.setEasingCurve(QtCore.QEasingCurve.OutCirc)
        self.anim4 = QtCore.QPropertyAnimation(self.spinBox, b"geometry")
        self.anim4.setDuration(800)
        self.anim4.setKeyValueAt(0, QtCore.QRect(dist3[0], h_l1[0], size3[0], size3[1]))
        self.anim4.setKeyValueAt(1, QtCore.QRect(dist3[1], h_l1[1], size3[2], size3[3]))
        self.anim4.setEasingCurve(QtCore.QEasingCurve.OutCirc)
        self.anim5 = QtCore.QPropertyAnimation(self.horizontalSlider, b"geometry")
        self.anim5.setDuration(800)
        self.anim5.setKeyValueAt(0, QtCore.QRect(dist4[0], h_l2[0], size4[0], size4[1]))
        self.anim5.setKeyValueAt(1, QtCore.QRect(dist4[1], h_l2[1], size4[2], size4[3]))
        self.anim5.setEasingCurve(QtCore.QEasingCurve.OutCirc)
        if finish:
            self.anim2.finished.connect(lambda: self.button_valute.hide())
            self.anim2.setDuration(400)
            self.anim3.finished.connect(lambda: self.label.hide())
            self.anim3.setDuration(400)
            self.anim4.finished.connect(lambda: self.spinBox.hide())
            self.anim4.setDuration(400)
            self.anim5.finished.connect(lambda: self.horizontalSlider.hide())
            self.anim5.setDuration(400)
        self.anim.start()
        self.anim2.start()
        self.anim3.start()
        self.anim4.start()
        self.anim5.start()
    
    def change_max_zp(self):
        value = self.horizontalSlider.value()
        self.spinBox.setValue(value)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.show_start_text.setText(_translate("MainWindow", "Введите профессию"))
        self.combobox1.setCurrentText(_translate("MainWindow", "строгий поиск"))
        self.combobox1.setItemText(0, _translate("MainWindow", "строгий поиск"))
        self.combobox1.setItemText(1, _translate("MainWindow", "нестрогий поиск"))
        self.combobox2.setItemText(0, _translate("MainWindow", "неполный поиск"))
        self.combobox2.setItemText(1, _translate("MainWindow", "полный поиск"))
        self.button_main.setText(_translate("MainWindow", "Хочу результат"))
        self.label.setText(_translate("MainWindow", "USD:\n"
"EUR:\n"
"Обновлено "))
        self.button_valute.setText(_translate("MainWindow", "Узнать курс валют"))

class Ui_MainWindow_shedule(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 1000)
        MainWindow.setMaximumSize(QtCore.QSize(1000, 1000))
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background: #FFF6FE;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    alignment: center;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    width: 264px;\n"
"    height: 45px;\n"
"    background: #FF9121;\n"
"    border: 1px solid gray;\n"
"}\n"
"\n"
"QTabBar::tab:first {\n"
"    border-top-left-radius: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:last {\n"
"    border-top-right-radius: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #fafafa, stop: 0.4 #f4f4f4,\n"
"                                stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);\n"
"     background: qlineargradient(spread:reflect, x1:1, y1:1, x2:1, y2:0.505, stop:0 rgba(255, 145, 33, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    background: qradialgradient(spread:reflect, cx:0.518528, cy:0.54, radius:0.667, fx:0.512, fy:0.545727, stop:0 rgba(255, 255, 255, 255), stop:0.758427 rgba(255, 145, 33, 255));\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color: white;\n"
"    font-size: 25px;\n"
"    border-bottom-color: lightgray;\n"
"}\n"
"\n"
"QPushButton#pushButton {\n"
"    border: 2px solid black;\n"
"    border-top-left-radius: 5px;\n"
"    border-bottom-left-radius: 5px;\n"
"    border-right: none;\n"
"    background: #e49546;\n"
"    background-image: url('./images/button_normal.jpg');\n"
"}\n"
"\n"
"QPushButton#pushButton:hover {\n"
"    background-image: url('./images/button_hover.jpg');\n"
"}\n"
"\n"
"QPushButton#pushButton:pressed {\n"
"    background: orange;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(100, 0, 800, 1000))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.tabWidget.setFont(font)
        self.tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab.sizePolicy().hasHeightForWidth())
        self.tab.setSizePolicy(sizePolicy)
        self.tab.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setKerning(True)
        self.tab.setFont(font)
        self.tab.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tab.setStyleSheet("")
        self.tab.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tab.setObjectName("tab")
        self.main_img1 = QtWidgets.QLabel(self.tab)
        self.main_img1.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.main_img1.setText("")
        self.main_img1.setObjectName("main_img1")
        self.label_key_skills = QtWidgets.QLabel(self.tab)
        self.label_key_skills.setGeometry(QtCore.QRect(230, 600, 340, 60))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label_key_skills.setFont(font)
        self.label_key_skills.setObjectName("label_key_skills")
        self.label_keys = QtWidgets.QLabel(self.tab)
        self.label_keys.setGeometry(QtCore.QRect(0, 650, 800, 52))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_keys.setFont(font)
        self.label_keys.setAlignment(QtCore.Qt.AlignCenter)
        self.label_keys.setObjectName("label_keys")
        self.statistics1 = QtWidgets.QLabel(self.tab)
        self.statistics1.setGeometry(QtCore.QRect(0, 702, 800, 231))
        self.statistics1.setText("")
        self.statistics1.setAlignment(QtCore.Qt.AlignCenter)
        self.statistics1.setObjectName("statistics1")
        self.tabWidget.addTab(self.tab, "")
        self.tab2 = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setPointSize(16)
        self.tab2.setFont(font)
        self.tab2.setObjectName("tab2")
        self.main_img2 = QtWidgets.QLabel(self.tab2)
        self.main_img2.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.main_img2.setText("")
        self.main_img2.setObjectName("main_img2")
        self.statistics2 = QtWidgets.QLabel(self.tab2)
        self.statistics2.setGeometry(QtCore.QRect(0, 600, 800, 300))
        self.statistics2.setText("")
        self.statistics2.setAlignment(QtCore.Qt.AlignCenter)
        self.statistics2.setObjectName("statistics2")
        self.tabWidget.addTab(self.tab2, "")
        self.tab3 = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setPointSize(16)
        self.tab3.setFont(font)
        self.tab3.setObjectName("tab3")
        self.main_img3 = QtWidgets.QLabel(self.tab3)
        self.main_img3.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.main_img3.setText("")
        self.main_img3.setObjectName("main_img3")
        self.statistics3 = QtWidgets.QLabel(self.tab3)
        self.statistics3.setGeometry(QtCore.QRect(0, 600, 800, 300))
        self.statistics3.setText("")
        self.statistics3.setAlignment(QtCore.Qt.AlignCenter)
        self.statistics3.setObjectName("statistics3")
        self.tabWidget.addTab(self.tab3, "")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(964, 430, 40, 167))
        self.pushButton.setText("")
        self.pushButton.setIconSize(QtCore.QSize(60, 200))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_key_skills.setText(_translate("MainWindow", "Ключевые навыки"))
        self.label_keys.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "headhunter.ru"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MainWindow", "jobfilter.ru"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), _translate("MainWindow", "superjob.ru"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_shedule()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
