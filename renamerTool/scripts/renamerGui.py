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
        self.setGeometry(200, 300, 440, 330)
        self.setWindowFlags(Qt.Window)

        # Create Layouts and Widgets
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.replace_group = QGroupBox("Search and Replace")
        self.replace_grid = QGridLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("L_")
        self.replace_grid.addWidget(self.search_input, 0, 0)
        self.replace_input = QLineEdit()
        self.replace_input.setPlaceholderText("R_")
        self.replace_grid.addWidget(self.replace_input, 1, 0)
        self.replace_bttn = StandardButton("Replace")
        self.replace_grid.addWidget(self.replace_bttn, 1, 1)
        self.replace_grid.setColumnStretch(0, 1)
        self.replace_grid.setColumnStretch(1, 0)
        self.replace_group.setLayout(self.replace_grid)
        self.layout.addWidget(self.replace_group)

        self.prefix_group = QGroupBox("Add Prefix")
        self.prefix_hl = QHBoxLayout()
        self.prefix_input = QLineEdit()
        self.prefix_input.setPlaceholderText("L_")
        self.prefix_hl.addWidget(self.prefix_input)
        self.prefix_bttn = StandardButton("Add")
        self.prefix_hl.addWidget(self.prefix_bttn)
        self.prefix_hl.setStretch(0, 1)
        self.prefix_hl.setStretch(1, 0)
        self.prefix_group.setLayout(self.prefix_hl)
        self.layout.addWidget(self.prefix_group)

        self.suffix_group = QGroupBox("Add Suffix")
        self.suffix_hl = QHBoxLayout()
        self.suffix_input = QLineEdit()
        self.suffix_input.setPlaceholderText("_jnt")
        self.suffix_hl.addWidget(self.suffix_input)
        self.suffix_bttn = StandardButton("Add")
        self.suffix_hl.addWidget(self.suffix_bttn)
        self.suffix_hl.setStretch(0, 1)
        self.suffix_hl.setStretch(1, 0)
        self.suffix_group.setLayout(self.suffix_hl)
        self.layout.addWidget(self.suffix_group)

        self.number_group = QGroupBox("Rename and Number")
        self.number_hl = QHBoxLayout()
        self.number_input = QLineEdit()
        self.number_input.setPlaceholderText("L_part{a}_subpart{01}")
        self.number_hl.addWidget(self.number_input)
        self.number_bttn = StandardButton("Rename")
        self.number_hl.addWidget(self.number_bttn)
        self.number_hl.setStretch(0, 1)
        self.number_hl.setStretch(1, 0)
        self.number_group.setLayout(self.number_hl)
        self.layout.addWidget(self.number_group)

        self.layout.addStretch()

        self.make_connections()

    def make_connections(self):
        self.replace_bttn.clicked.connect(self.on_replace_bttn_clicked)
        self.prefix_bttn.clicked.connect(self.on_prefix_bttn_clicked)
        self.suffix_bttn.clicked.connect(self.on_suffix_bttn_clicked)
        self.number_bttn.clicked.connect(self.on_number_bttn_clicked)

    def on_replace_bttn_clicked(self):
        renamer.replace(self.search_input.text(), self.replace_input.text())

    def on_prefix_bttn_clicked(self):
        renamer.add_prefix(self.prefix_input.text())

    def on_suffix_bttn_clicked(self):
        renamer.add_suffix(self.suffix_input.text())

    def on_number_bttn_clicked(self):
        renamer.rename_and_number(self.number_input.text())


class StandardButton(QPushButton):
    STYLE_SHEET = """
    QPushButton {
        min-width: 62px;
        max-width: 62px;
    }
    """

    def __init__(self, label):
        super(StandardButton, self).__init__(label)
        self.setStyleSheet(StandardButton.STYLE_SHEET)


def main():
    gui = RenamerGUI()
    gui.show(dockable=False)
    return gui


if __name__ == "__main__":
    main()
