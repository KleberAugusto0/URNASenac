from PySide6.QtWidgets import QLabel, QVBoxLayout,QPushButton,QWidget,QApplication,QFrame
from PySide6.QtCore import Qt
import sys,os

class Menu_urna(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu")
        layout = QVBoxLayout()
        self.setLayout(layout)

        btn_zerezima = QPushButton("Rélatorio inicial (Zerézima)")
        layout.addWidget(btn_zerezima)
        btn_votar = QPushButton("Votar")
        layout.addWidget(btn_votar)
        btn_relatorio = QPushButton("Relatório Final")
        layout.addWidget(btn_relatorio)
        btn_sair = QPushButton("Sair")
        layout.addWidget(btn_sair)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Menu_urna()
    janela.show()
    sys.exit(app.exec())