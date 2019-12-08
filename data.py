from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout, QPushButton
import pandas as pd
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QDialog

df = pd.read_excel('C:/Users/홍석찬/Desktop/nlp-master/s_test.xlsx')
dx = df[['Score']]


print(df);
print(dx);



class MyDialog(QDialog):
    def __init__(self):
        print("시1발");
        QDialog.__init__(self)
        print("시2발");

        lblName = QLabel("원하는 데이터를 선택하세요")
        btX = QPushButton("x axis")
        btT = QPushButton("Exit")

        print(btT);

        layout = QVBoxLayout()
        layout.addWidget(lblName)
        layout.addWidget(btX)
        layout.addWidget(btT)
        self.setLayout(layout)

        btX.clicked.connect(self.btnXClicked)
        btT.clicked.connect(self.btnTClicked)

    def btnXClicked(self):
        plt.plot(dx)
        plt.show()

    def btnTClicked(self):
        QPushButton(self,command=self.quit)

app = QApplication([])
dialog = MyDialog()
dialog.show()
app.exec_()


