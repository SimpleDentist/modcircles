import sys, random
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPen, QBrush
from PyQt5.QtCore import Qt
from UI import Ui_Form


class MyWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.flag = False

        self.pushButton.clicked.connect(self.flagon)

    def flagon(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag is True:
            qp = QPainter()
            qp.begin(self)
            self.drawCircle(qp)
            qp.end()

    def drawCircle(self, qp):
        size = self.size()

        for i in range(15):
            color = random.choice(("Qt.yellow", "Qt.blue", "Qt.red", "Qt.black", "Qt.green"))
            x = random.randint(1, size.width() - 1)
            y = random.randint(1, size.height() - 1)
            circlesize = random.randint(1, 100)
            eval("qp.setPen(QPen({}, 8, Qt.SolidLine))".format(color))
            eval("qp.setBrush(QBrush({}, Qt.SolidPattern))".format(color))
            qp.drawEllipse(x, y, circlesize, circlesize)


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())