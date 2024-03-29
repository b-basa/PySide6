import sys
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QPushButton,
    QWidget,
)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QGridLayout Example")

        # Create a QGridLayout instance
        layout = QGridLayout()

        # Add widgets to the layout
        layout.addWidget(QPushButton("Button at (0, 0)"), 0, 0)
        layout.addWidget(QPushButton("Button at (0, 1)"), 0, 1)
        # Sometimes you can’t use keyword arguments when calling PyQt methods
        # layout.addWidget(QPushButton("Button Spans two Cols"), fromRow=1, fromColumn=0, rowSpan=1, columnSpan=2)
        layout.addWidget(QPushButton("Button Spans two Cols"), 1, 0, 1, 2)

        # Set the layout on the application's window
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
