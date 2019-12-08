
# To show progress bar
from tqdm import tqdm
import check
import excel as xl
import google_nl as g
import print_results

from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout, QPushButton
import pandas as pd
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QDialog



if __name__ == '__main__':
    # If check won't go through, program will show error msg and exit
    FILE, NEW_FILE, TYPE = check.arguments()
    # FILE = "test.xlsx"
    # NEW_FILE = "test2.xlsx"

    if TYPE == '.txt':
        TXT = open(FILE, "r")
        SEN = g.analyze_sentiment(TXT.read())
        TXT.close()
        print_results.text(SEN)
    elif TYPE == 'excel':
        DATA, ROWS_NB = xl.get_xl(FILE, NEW_FILE)
        print(range(ROWS_NB));
        print(tqdm(range(ROWS_NB)))

        for ROW in tqdm(range(ROWS_NB)):
            print(ROW)
            print("######")
            print(DATA.iloc[ROW, 0])

            SEN = g.analyze_sentiment(DATA.iloc[ROW, 0])
            print(SEN)
            DATA.iloc[ROW, 1] = round(SEN.score, 1) * 10
            DATA.iloc[ROW, 2] = round(SEN.magnitude, 1)
        DATA.to_excel(NEW_FILE, index=None)
        print_results.excel(NEW_FILE)

# Project files
df = pd.read_excel('C:/Users/홍석찬/Desktop/nlp-master/s_test.xlsx')
dx = df[['Score']]

class MyDialog(QDialog):
    def __init__(self):

        QDialog.__init__(self)

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


