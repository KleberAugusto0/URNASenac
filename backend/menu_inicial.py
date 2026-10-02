from PySide6.QtWidgets import QLabel, QVBoxLayout,QPushButton,QWidget,QApplication,QFrame
from PySide6.QtCore import Qt
import sys,os

class MenuUrna(QWidget):
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
        btn_votar.setFixedSize(250,50)
    

        btn_relatorio = QPushButton("Relatório Final")
        layout.addWidget(btn_relatorio,alignment=Qt.AlignmentFlag.AlignCenter)
        btn_relatorio.setFixedSize(250,50)

        btn_sair = QPushButton("Sair")
        layout.addWidget(btn_sair,alignment=Qt.AlignmentFlag.AlignCenter)
        btn_sair.setFixedSize(250,50) 
        layout.addStretch(1)




        def zerezima():
            verificacao_zerezima = True
            #fazer logicoa pra chamar a tela
            pass


        def votar():
            if verificacao_zerezima == True:
                pass #fazer codigo para chamar a tela de votação
            elif verificacao_zerezima == False:
                pass#Fazer popup para fazer a zerezima primeiro


        def relatorio():
            pass

        def main():
            app =QApplication(sys.argv)
            janela = MenuUrna()
            janela.show
            sys.exit(app.exec())


