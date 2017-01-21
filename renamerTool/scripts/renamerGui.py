import renamer
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin

# PySide import setup compatible with 2016 and 2017
try:
    from PySide2.QtCore import *
    from PySide2.QtGui import *
    from PySide2.QtWidgets import *
except ImportError:
    from PySide.QtCore import *
    from PySide.QtGui import *


class RenamerGUI(MayaQWidgetDockableMixin, QWidget):
    def __init__(self, parent=None):
        super(RenamerGUI, self).__init__(parent=parent)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        self.setObjectName("RenamerGUI")
        self.setWindowTitle("Renamer Tool v0.1.0")
        self.setGeometry(50, 50, 250, 150)
        self.setWindowFlags(Qt.Window)

        # Init UI
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.button = QPushButton("Create", self)
        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        """Execute test command when button is clicked"""
        self.test()

    @staticmethod
    def test():
        renamer.test()


def main():
    gui = RenamerGUI()
    gui.show(dockable=True)
    return gui


if __name__ == "__main__":
    main()
