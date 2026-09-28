import sys, os
from PySide6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFrame, QApplication
from PySide6.QtCore import Qt


class PopupAtencao(QDialog):
    # CORREÇÃO 1: Alterado de _init_ para __init__
    def __init__(self, parent=None):
        # CORREÇÃO 1: Alterado de _init_ para __init__
        super().__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.inicializar_tela()
        self.carregar_estilo()

    def inicializar_tela(self):
        self.card_container = QFrame(self)
        self.card_container.setObjectName("card_container")

        layout_card = QVBoxLayout(self.card_container)
        layout_card.setContentsMargins(24, 20, 24, 20)
        layout_card.setSpacing(16)

        layout_cabecalho = QHBoxLayout()
        layout_cabecalho.setAlignment(Qt.AlignCenter)
        layout_cabecalho.setSpacing(8)

        self.label_icone = QLabel("i")
        self.label_icone.setObjectName("label_icone")

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

        layout_card.addLayout(layout_cabecalho)
        layout_card.addWidget(self.label_mensagem)
        layout_card.addWidget(self.botao_ok, alignment=Qt.AlignCenter)

        layout_raiz = QVBoxLayout(self)
        layout_raiz.addWidget(self.card_container)
        layout_raiz.setContentsMargins(0, 0, 0, 0)

    def carregar_estilo(self):
       
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        caminho_qss = os.path.join(diretorio_atual, "..", "estilo", "estilo_candidato.qss")
        if os.path.exists(caminho_qss):
            with open(caminho_qss, "r", encoding="utf-8") as arquivo_qss:
                self.setStyleSheet(arquivo_qss.read())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = PopupAtencao()
    janela.show()
    sys.exit(app.exec())
