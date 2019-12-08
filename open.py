from PyQt5.QtGui import *
import pandas as pd
import  matplotlib.pyplot as plt
from PyQt5.QtWidgets import QDialog

df = pd.read_excel('C:/Users/홍석찬/Desktop/nlp-master/s_test.xlsx')
dx = df[['x']]

class MyDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        lblName = QLebel("원하는 데이터를 선택하세요")
        btX = QpushButton("x axis")
        btT = QpushButton("Exit")

        layout = QVBoxLayout ()
        layout.add