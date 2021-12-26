"""
GUI example code.

Ref:
    https://wikidocs.net/21932
"""
import os
import sys

from PyQt5.QtCore import QCoreApplication, QDate, Qt
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QDesktopWidget,
    QLabel,
    QMainWindow,
    QPushButton,
    QToolTip,
    QVBoxLayout,
    QWidget,
    qApp,
)


class MyApp(QMainWindow):
    """Main Window class.

    Notes:
        - the main difference from QMainWidget is that it has its own layout.
        - it cannot employ layout libraries such as QHBoxLayout, QVBoxLayout.
    """

    def __init__(self) -> None:
        """Initialize."""
        super().__init__()

        # time information
        self.date = QDate.currentDate()

        self.initUI()

    def initUI(self) -> None:
        """Initialize UI."""
        # status bar
        self.statusBar().showMessage("Ready")

        # button
        exitAction = QAction(QIcon(os.path.join("icons", "exit.png")), "Exit", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("Exit application")
        exitAction.triggered.connect(qApp.quit)

        # menu bar
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu("&File")
        filemenu.addAction(exitAction)

        # tool bar
        self.toolbar = self.addToolBar("Exit")
        self.toolbar.addAction(exitAction)

        # time information
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))

        # gui baseline
        self.setWindowTitle("Main Window")
        # x_pos, y_pos, width, height
        self.setGeometry(300, 300, 300, 200)
        # it pops up in the center
        self.center()

        self.show()

    def center(self) -> None:
        """Make appliction pops up in the center."""
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


class MyWidget(QWidget):
    """Widget class."""

    def __init__(self) -> None:
        """Initialize."""
        super().__init__()
        self.initUI()

    def initUI(self) -> None:
        """Initialize UI."""
        self.setWindowTitle("My First Application")

        # program icon
        self.setWindowIcon(QIcon(os.path.join("icons", "paper.png")))
        # x_pos, y_pos, width, height
        self.setGeometry(300, 300, 300, 200)

        # tool tips
        QToolTip.setFont(QFont("SansSerif", 10))

        # show a tooltip in anywhere of widget
        self.setToolTip("This is a <b>QWidget</b> widget")

        # quit button
        btn = QPushButton("Quit", self)
        btn.setToolTip("Quit the program")
        btn.move(50, 50)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)

        # customize layout
        self.set_layout()

        self.show()

    def set_layout(self) -> None:
        """Customize layout."""
        lbl_red = QLabel("Red")
        lbl_green = QLabel("Green")
        lbl_blue = QLabel("Blue")

        lbl_red.setStyleSheet(
            "color: red;"
            "border-style: solid;"
            "border-width: 2px;"
            "border-color: #FA8072;"
            "border-radius: 3px"
        )
        lbl_green.setStyleSheet("color: green;" "background-color: #7FFFD4")
        lbl_blue.setStyleSheet(
            "color: blue;"
            "background-color: #87CEFA;"
            "border-style: dashed;"
            "border-width: 3px;"
            "border-color: #1E90FF"
        )

        vbox = QVBoxLayout()
        vbox.addWidget(lbl_red)
        vbox.addWidget(lbl_green)
        vbox.addWidget(lbl_blue)

        self.setLayout(vbox)


if __name__ == "__main__":
    widget = QApplication(sys.argv)
    ex = MyWidget()
    sys.exit(widget.exec_())

    # window = QApplication(sys.argv)
    # ex = MyApp()
    # sys.exit(window.exec_())


# Date
# now = QDate.currentDate()
# print(now.toString('d.M.yy'))                     -   2.1.19
# print(now.toString('dd.MM.yyyy'))                 -   02.01.2019
# print(now.toString('ddd.MMMM.yyyy'))              -   수.1월.2019
# print(now.toString(Qt.ISODate))                   -   2019-01-02
# print(now.toString(Qt.DefaultLocaleLongDate))     -   2019년 1월 2일 수요일

# Time
# time = QTime.currentTime()
# print(time.toString('h.m.s'))                     -   16.2.3
# print(time.toString('hh.mm.ss'))                  -   16.02.03
# print(time.toString('hh.mm.ss.zzz'))              -   16.02.03.610
# print(time.toString(Qt.DefaultLocaleLongDate))    -   오후 4:02:03
# print(time.toString(Qt.DefaultLocaleShortDate))   -   오후 4:02
