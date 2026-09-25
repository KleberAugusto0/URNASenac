from PySide6.QtWidgets import QLabel, QVBoxLayout,QPushButton,QWidget,QApplication,QFrame
from PySide6.QtCore import Qt
import sys,os

class Menu_urna(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu")
        layout = QVBoxLayout()
        self.setLayout(layout)
        

        verificacao_zerezima = False

        layout.addStretch(1)
        txt_urna = QLabel("Urna Eletrónica")
        layout.addWidget(txt_urna)
        txt_urna.setAlignment(Qt.AlignmentFlag.AlignCenter) 

        btn_zerezima = QPushButton("Rélatorio inicial (Zerézima)")
        layout.addWidget(btn_zerezima,alignment=Qt.AlignmentFlag.AlignCenter)
        btn_zerezima.setFixedSize(250,50)

        btn_votar = QPushButton("Votar")
        layout.addWidget(btn_votar,alignment=Qt.AlignmentFlag.AlignCenter)
    

        btn_relatorio = QPushButton("Relatório Final")
        layout.addWidget(btn_relatorio,alignment=Qt.AlignmentFlag.AlignCenter)


        btn_sair = QPushButton("Sair")
        layout.addWidget(btn_sair,alignment=Qt.AlignmentFlag.AlignCenter) 
        layout.addStretch(1)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Menu_urna()
    janela.show()
    sys.exit(app.exec())