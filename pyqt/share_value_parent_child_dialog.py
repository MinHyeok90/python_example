from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal, QTimer


class Ak47(QObject):
    bulletChanged = pyqtSignal(int)

    _instance = None  # singleton instance

    def __new__(cls, *args, **kwargs):
        if cls._instance is None or not isinstance(cls._instance, cls):
            cls._instance = super().__new__(cls)  # 객체 생성
            cls._instance.bullet = 30
            cls._instance.timer = QTimer()
            cls._instance.timer.timeout.connect(cls._instance.decrementBullet)
            cls._instance.timer.start(1000)
        return cls._instance  # 기존 객체 반환

    def decrementBullet(self):
        self.bullet -= 1
        self.bulletChanged.emit(self.bullet)


class ParentDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.ak47 = Ak47()

        self.button = QtWidgets.QPushButton("Fire")
        self.label = QtWidgets.QLabel(str(self.ak47.bullet))

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.label)

        self.setLayout(layout)

        self.button.clicked.connect(self.show_child)
        self.ak47.bulletChanged.connect(self.updateRemainingBullets)

    def show_child(self):
        child = ChildDialog(self.ak47, self)
        child.show()

    def updateRemainingBullets(self, num_bullets):
        self.label.setText(str(num_bullets))


class ChildDialog(QtWidgets.QDialog):
    def __init__(self, ak47, parent):
        super().__init__(parent)

        self.ak47 = ak47

        label = QtWidgets.QLabel(str(self.ak47.bullet))

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(label)

        self.setLayout(layout)

        self.ak47.bulletChanged.connect(self.updateRemainingBullets)

    def updateRemainingBullets(self, num_bullets):
        label = self.layout().itemAt(0).widget()
        label.setText(str(num_bullets))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    parent = ParentDialog()

    parent.show()

    app.exec_()