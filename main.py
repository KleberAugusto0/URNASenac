
from PySide6.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QPushButton,
    QWidget,
    QApplication,
    QDialog,
    QHBoxLayout,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
import sys
import os


class MenuUrna(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Menu")

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.verificacao_zerezima = False

        layout.addStretch(1)

        txt_urna = QLabel("Urna Eletrônica")
        layout.addWidget(txt_urna)
        txt_urna.setAlignment(Qt.AlignmentFlag.AlignCenter)

        btn_zerezima = QPushButton("Rélatorio inicial (Zerézima)")
        layout.addWidget(
            btn_zerezima,
            alignment=Qt.AlignmentFlag.AlignCenter
        )
        btn_zerezima.setFixedSize(250, 50)

        btn_votar = QPushButton("Votar")
        layout.addWidget(
            btn_votar,
            alignment=Qt.AlignmentFlag.AlignCenter
        )
        btn_votar.setFixedSize(250, 50)

        btn_relatorio = QPushButton("Relatório Final")
        layout.addWidget(
            btn_relatorio,
            alignment=Qt.AlignmentFlag.AlignCenter
        )
        btn_relatorio.setFixedSize(250, 50)

        btn_sair = QPushButton("Sair")
        btn_sair.setObjectName("btn_sair")
        layout.addWidget(
            btn_sair,
            alignment=Qt.AlignmentFlag.AlignCenter
        )
        btn_sair.setFixedSize(250, 50)

        btn_zerezima.clicked.connect(self.zerezima)
        btn_votar.clicked.connect(self.votar)
        btn_relatorio.clicked.connect(self.relatorio)
        btn_sair.clicked.connect(self.sairDoSistema)

        layout.addStretch(1)

    def zerezima(self):

        tela_zerezima = QDialog(self)

        tela_zerezima.setFixedSize(900, 650)

        tela_zerezima.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.Dialog
        )

      
        caminho_estilo = os.path.join(
            os.path.dirname(__file__),
            "estilo",
            "estilo_zerezima.qss"
        )
        
        layout_principal = QVBoxLayout(tela_zerezima)

        botao_fechar = QPushButton("×")
        botao_fechar.setObjectName("btn_fechar_zerezima")
        botao_fechar.setFixedSize(45, 45)
        botao_fechar.clicked.connect(tela_zerezima.close)

        layout_principal.addWidget(
            botao_fechar,
            alignment=Qt.AlignmentFlag.AlignRight
        )

        titulo = QLabel("RELATÓRIO INICIAL")
        titulo.setObjectName("titulo_zerezima")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        icone = QLabel()
        icone.setObjectName("quadrado_icone")
        caminho_imagem = os.path.dirname(os.path.abspath(__file__))
        caminho_imagem = os.path.join(caminho_imagem,"imagens","voting-box.png")
        icone.setPixmap
        (QPixmap(caminho_imagem).scaled(150,150,Qt.AspectRatioMode.KeepAspectRatio))

        subtitulo = QLabel("ZERÉSIMA")
        subtitulo.setObjectName("subtitulo_zerezima")
        subtitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        layout_principal.addWidget(titulo)
        layout_principal.addWidget(subtitulo)

        caixa_informacoes = QWidget()
        caixa_informacoes.setObjectName("caixa_informacoes")

        layout_caixa = QVBoxLayout(caixa_informacoes)

        status = QLabel("URNA SEM VOTOS REGISTRADOS")
        status.setObjectName("status_zerezima")
        status.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout_caixa.addWidget(status)

        texto = QLabel(
            "A urna está pronta para iniciar o processo de votação."
        )
        texto.setObjectName("texto_informacao")
        texto.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout_caixa.addWidget(texto)

        candidatos = ["Candidato 01","Candidato 02","Candidato 03"]

        for candidato in candidatos:
            label = QLabel(f"{candidato} ...0 votos")
            label.setObjectName("texto_informacao")
            layout_caixa.addWidget(label)

        votos_brancos = QLabel(
            "Votos brancos ... 0"
        )
        votos_brancos.setObjectName("texto_informacao")

        votos_nulos = QLabel("Votos nulos ... 0")
        votos_nulos.setObjectName("texto_informacao")

        layout_caixa.addWidget(votos_brancos)
        layout_caixa.addWidget(votos_nulos)

        layout_principal.addWidget(caixa_informacoes)

        layout_botoes = QHBoxLayout()

        botao_voltar = QPushButton("Voltar")
        botao_voltar.setObjectName("btn_voltar_zerezima")
        botao_voltar.setFixedSize(220, 55)
        botao_voltar.clicked.connect(tela_zerezima.close)

        botao_confirmar = QPushButton("Confirmar Zerésima")
        botao_confirmar.setObjectName("btn_confirmar_zerezima")
        botao_confirmar.setFixedSize(260, 55)

        def confirmar_zerezima():
            self.verificacao_zerezima = True
            tela_zerezima.close()

        botao_confirmar.clicked.connect(confirmar_zerezima)

        layout_botoes.addWidget(botao_voltar)
        layout_botoes.addWidget(botao_confirmar)

        layout_principal.addLayout(layout_botoes)

        tela_zerezima.exec()

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

        tela_sair.setWindowFlags(Qt.WindowType.FramelessWindowHint|Qt.WindowType.Dialog)

        tela_alinhamento = QVBoxLayout(tela_sair)
        layout_botoes = QHBoxLayout()

        botao_fechar = QPushButton("×")
        botao_fechar.setObjectName("btn_fechar_x")
        botao_fechar.clicked.connect(tela_sair.close)

        tela_alinhamento.addWidget(botao_fechar,alignment=Qt.AlignmentFlag.AlignRight)

        icone = QLabel()
        icone.setObjectName("quadrado_icone")

        caminho_imagem = os.path.dirname(os.path.abspath(__file__))

        caminho_imagem = os.path.join(caminho_imagem,"imagens","exit.png")

        icone.setPixmap(QPixmap(caminho_imagem).scaled(78,78,Qt.AspectRatioMode.KeepAspectRatio))
        
        tela_alinhamento.addWidget(icone,alignment=Qt.AlignmentFlag.AlignCenter)
        titulo = QLabel("Sair do sistema")
        titulo.setObjectName("titulo_popup")
        
        subtitulo = QLabel("Tem certeza que deseja sair?")
        subtitulo.setObjectName("subtitulo_popup")
        
        tela_alinhamento.addWidget(titulo,alignment=Qt.AlignmentFlag.AlignCenter)
        tela_alinhamento.addWidget(subtitulo,alignment=Qt.AlignmentFlag.AlignCenter)

        botao_cancelar = QPushButton("Cancelar")
        botao_cancelar.setObjectName("btn_cancelar_dialog")
        botao_cancelar.clicked.connect(tela_sair.close)

        botao_confirmar = QPushButton("Confirmar")
        botao_confirmar.setObjectName("btn_confirmar_dialog")
        botao_confirmar.clicked.connect(QApplication.quit)

        layout_botoes.addWidget(botao_cancelar)
        layout_botoes.addWidget(botao_confirmar)

        tela_alinhamento.addLayout(layout_botoes)
        caminho_estilo = os.path.join(
            os.path.dirname(__file__),
            "estilo",
            "estilo_sair.qss"
        )

        with open(
            caminho_estilo,
            "r",
            encoding="utf-8"
        ) as arquivo:
            tela_sair.setStyleSheet(arquivo.read())

        tela_sair.exec()


if __name__ == "__main__":

    app = QApplication(sys.argv)

    caminho_estiloMenu = os.path.join(
        os.path.dirname(__file__),
        "estilo",
        "estilo_menu.qss"
    )

    with open(
        caminho_estiloMenu,
        "r",
        encoding="utf-8"
    ) as arquivo:
        app.setStyleSheet(arquivo.read())

    janela = MenuUrna()
    janela.show()

    sys.exit(app.exec())

