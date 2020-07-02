# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QLocale)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
import pickle

class Ui_MainWindow(object):
    textToPredict=""
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(733, 404)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 20, 691, 341))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textEdit = QTextEdit(self.horizontalLayoutWidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setLocale(QLocale(QLocale.Uzbek, QLocale.Uzbekistan))

        self.verticalLayout.addWidget(self.textEdit)

        self.textBtn = QPushButton(self.horizontalLayoutWidget)
        self.textBtn.setObjectName(u"textBtn")
        icon = QIcon()
        icon.addFile(u"text.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.textBtn.setIcon(icon)
        self.textBtn.setIconSize(QSize(32, 32))
        self.textBtn.setFlat(False)

        self.verticalLayout.addWidget(self.textBtn)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setFamily(u"Cambria")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAutoFillBackground(True)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_4)

        self.classLabel = QLabel(self.horizontalLayoutWidget)
        self.classLabel.setObjectName(u"classLabel")
        font1 = QFont()
        font1.setFamily(u"Cambria")
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setWeight(75)
        self.classLabel.setFont(font1)
        self.classLabel.setAutoFillBackground(True)
        self.classLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.classLabel)

        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setAutoFillBackground(True)

        self.verticalLayout_2.addWidget(self.label)

        self.predictBtn = QPushButton(self.horizontalLayoutWidget)
        self.predictBtn.setObjectName(u"predictBtn")
        icon1 = QIcon()
        icon1.addFile(u"classify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.predictBtn.setIcon(icon1)
        self.predictBtn.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.predictBtn)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 733, 20))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.textBtn.clicked.connect(self.upload_text)
        self.predictBtn.clicked.connect(self.predict)
        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"КЛАССИФИКАТОР ТЕКСТОВЫХ ДОКУМЕНТОВ", None))
        self.textBtn.setText(QCoreApplication.translate("MainWindow", u"Загрузить текстовой документ...", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"КАТЕГОРИЯ:", None))
        self.classLabel.setText(QCoreApplication.translate("MainWindow", u"НЕ ОПРЕДЕЛЕНА", None))
        self.label.setText("")
        self.predictBtn.setText(QCoreApplication.translate("MainWindow", u"Классифицировать", None))
    # retranslateUi
    def upload_text(self):
        self.fileName,_ = QFileDialog.getOpenFileName(None, "Открыть текстовой файл", "~/Desktop/", "TXT File (*.txt)")
        if self.fileName is not None:
            text = open(self.fileName).read()
            self.textEdit.setPlainText(text)

    def predict(self):
        category_list = ["sport", "siyosat", "jamiyat", "iqtisodiyot", "texnologiyalar"]
        loaded_vec = CountVectorizer(vocabulary=pickle.load(open("count_vector.pkl", "rb")))
        loaded_tfidf = pickle.load(open("tfidf.pkl", "rb"))
        loaded_model = pickle.load(open("nb_model.pkl", "rb"))
        text = [self.textEdit.toPlainText()]
        X_new_counts = loaded_vec.transform(text)
        X_new_tfidf = loaded_tfidf.transform(X_new_counts)
        predicted = loaded_model.predict(X_new_tfidf)
        self.classLabel.setText(str.upper(category_list[predicted[0]]))

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
