import sys
from PySide6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFrame
from PySide6.QtCore import Qt
import sys,os
from pathlib import Path
from backend.tela_titulo_eleitor import TelaTituloEleitor


class MenuUrna(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu")
        layout = QVBoxLayout()
        self.setLayout(layout)
        

        verificacao_zerezima = True

        layout.addStretch(1)
        txt_urna = QLabel("Urna Eletrónica")
        layout.addWidget(txt_urna)
        txt_urna.setAlignment(Qt.AlignmentFlag.AlignCenter) 

        btn_zerezima = QPushButton("Rélatorio inicial (Zerézima)")
        layout.addWidget(btn_zerezima,alignment=Qt.AlignmentFlag.AlignCenter)
        btn_zerezima.setFixedSize(250,50)

        btn_votar = QPushButton("Votar")
        btn_votar.clicked.connect(lambda:votar())
        layout.addWidget(btn_votar,alignment=Qt.AlignmentFlag.AlignCenter)
        btn_votar.setFixedSize(250,50)
    

        btn_relatorio = QPushButton("Relatório Final")
        layout.addWidget(btn_relatorio,alignment=Qt.AlignmentFlag.AlignCenter)
        btn_relatorio.setFixedSize(250,50)

        btn_sair = QPushButton("Sair")
        layout.addWidget(btn_sair,alignment=Qt.AlignmentFlag.AlignCenter)
        btn_sair.setFixedSize(250,50) 
        layout.addStretch(1)


        tela_eleitor = TelaTituloEleitor()

    def inicializar_tela(self):
        self.card_container = QFrame(self)
        self.card_container.setObjectName("card_container")

        layout_card = QVBoxLayout(self.card_container)
        layout_card.setContentsMargins(24, 20, 24, 20)
        layout_card.setSpacing(16)

        layout_cabecalho = QHBoxLayout()
        layout_cabecalho.setAlignment(Qt.AlignCenter)
        layout_cabecalho.setSpacing(8)

        def votar():
            if verificacao_zerezima == True:
                self.close()
                tela_eleitor.show()
                
                
            elif verificacao_zerezima == False:
                pass#Fazer popup para fazer a zerezima primeiro

        self.label_titulo = QLabel("Atenção")
        self.label_titulo.setObjectName("label_titulo")

        layout_cabecalho.addWidget(self.label_icone)
        layout_cabecalho.addWidget(self.label_titulo)

        self.label_mensagem = QLabel("Você precisa realizar a Zerésima\nantes de poder votar.")
        self.label_mensagem.setObjectName("label_mensagem")
        self.label_mensagem.setAlignment(Qt.AlignCenter)

        self.botao_ok = QPushButton("Ok")
        self.botao_ok.setObjectName("botao_ok")
        self.botao_ok.setCursor(Qt.PointingHandCursor)
        self.botao_ok.clicked.connect(self.accept)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    with open("estilo/estilo.qss", "r", encoding="utf-8") as arquivo:
        app.setStyleSheet(arquivo.read())
    janela = MenuUrna()
    janela.show()
    sys.exit(app.exec())

