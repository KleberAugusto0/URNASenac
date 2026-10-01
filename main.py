from PySide6.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QPushButton,
    QWidget,
    QApplication,
    QDialog,
    QHBoxLayout,
    QScrollArea,
    QFrame,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from datetime import datetime
import sys
import os


class MenuUrna(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Menu")

        layout = QVBoxLayout()
        self.setLayout(layout)
        

        verificacao_zerezima = True

        self.verificacao_zerezima = False
        
        layout.addStretch(1)

        txt_urna = QLabel("Urna Eletrônica")
        layout.addWidget(txt_urna)
        txt_urna.setAlignment(Qt.AlignmentFlag.AlignCenter)

        botao_zerezima = QPushButton("Rélatorio inicial (Zerézima)")
        layout.addWidget(botao_zerezima, alignment=Qt.AlignmentFlag.AlignCenter)
        botao_zerezima.setFixedSize(250, 50)

        botao_votar = QPushButton("Votar")
        botao_votar.clicked.connect(lambda:votar())
        layout.addWidget(botao_votar,alignment=Qt.AlignmentFlag.AlignCenter)
        botao_votar.setFixedSize(250,50)
    

        botao_relatorio = QPushButton("Relatório Final")
        layout.addWidget(botao_relatorio, alignment=Qt.AlignmentFlag.AlignCenter)
        botao_relatorio.setFixedSize(250, 50)

        botao_sair = QPushButton("Sair")
        botao_sair.setObjectName("botao_sair")
        layout.addWidget(botao_sair, alignment=Qt.AlignmentFlag.AlignCenter)
        botao_sair.setFixedSize(250, 50)

       
        botao_votar.clicked.connect(self.votar)
        botao_relatorio.clicked.connect(self.relatorio)
        botao_sair.clicked.connect(self.sairDoSistema)

        layout.addStretch(1)


    def votar(self):

        if self.verificacao_zerezima == True:
            pass  # fazer codigo para chamar a tela de votação

        elif self.verificacao_zerezima == False:
            pass  # fazer popup para fazer a zerezima primeiro

    def relatorio(self):
        pass

    def sairDoSistema(self):

        tela_sair = QDialog(self)

        tela_sair.setFixedSize(450, 280)

        tela_sair.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Dialog)

        tela_alinhamento = QVBoxLayout(tela_sair)
        layout_botoes = QHBoxLayout()

        botao_fechar = QPushButton("×")
        botao_fechar.setObjectName("botao_fechar_x")
        botao_fechar.clicked.connect(tela_sair.close)

        tela_alinhamento.addWidget(botao_fechar, alignment=Qt.AlignmentFlag.AlignRight)

        icone = QLabel()
        icone.setObjectName("quadrado_icone")

        caminho_imagem = os.path.dirname(os.path.abspath(__file__))
        caminho_imagem = os.path.join(caminho_imagem, "imagens", "exit.png")

        icone.setPixmap(QPixmap(caminho_imagem).scaled(78, 78, Qt.AspectRatioMode.KeepAspectRatio))

        tela_alinhamento.addWidget(icone, alignment=Qt.AlignmentFlag.AlignCenter)
        titulo = QLabel("Sair do sistema")
        titulo.setObjectName("titulo_popup")

        subtitulo = QLabel("Tem certeza que deseja sair?")
        subtitulo.setObjectName("subtitulo_popup")

        tela_alinhamento.addWidget(titulo, alignment=Qt.AlignmentFlag.AlignCenter)
        tela_alinhamento.addWidget(subtitulo, alignment=Qt.AlignmentFlag.AlignCenter)

        botao_cancelar = QPushButton("Cancelar")
        botao_cancelar.setObjectName("botao_cancelar_dialog")
        botao_cancelar.clicked.connect(tela_sair.close)

        botao_confirmar = QPushButton("Confirmar")
        botao_confirmar.setObjectName("botao_confirmar_dialog")
        botao_confirmar.clicked.connect(QApplication.quit)

        layout_botoes.addWidget(botao_cancelar)
        layout_botoes.addWidget(botao_confirmar)

        tela_alinhamento.addLayout(layout_botoes)
        caminho_estilo = os.path.join(
            os.path.dirname(__file__), "estilo", "estilo_sair.qss"
        )

        with open(caminho_estilo, "r", encoding="utf-8") as arquivo:
            tela_sair.setStyleSheet(arquivo.read())

        tela_sair.exec()

        self.botao_ok = QPushButton("Ok")
        self.botao_ok.setObjectName("botao_ok")
        self.botao_ok.setCursor(Qt.PointingHandCursor)
        self.botao_ok.clicked.connect(self.accept)

if __name__ == "__main__":

    app = QApplication(sys.argv)

    caminho_estiloMenu = os.path.join(os.path.dirname(__file__), "estilo", "estilo_menu.qss")

    with open(caminho_estiloMenu, "r", encoding="utf-8") as arquivo:
        app.setStyleSheet(arquivo.read())

    janela = MenuUrna()
    janela.show()

    sys.exit(app.exec())