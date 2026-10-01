import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QDialog, QFrame, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QApplication
)


class TelaAvisoZeresima(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("tela_aviso")
        self.setModal(True)
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint)
        self.setFixedSize(420, 320)
        self.montar_interface()

    def montar_interface(self):
        layout_raiz = QVBoxLayout(self)
        layout_raiz.setContentsMargins(24, 24, 24, 24)

        self.card = QFrame()
        self.card.setObjectName("card_aviso")
        layout_raiz.addWidget(self.card)

        layout_card = QVBoxLayout(self.card)
        layout_card.setContentsMargins(24, 28, 24, 24)
        layout_card.setSpacing(0)

        self.label_icone = QLabel()
        self.label_icone.setObjectName("label_icone_aviso")
        self.label_icone.setAlignment(Qt.AlignCenter)

        pixmap_icone = QPixmap("imagens/icone_informacao.png")
        self.label_icone.setPixmap(
            pixmap_icone.scaled(48, 48, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        )

        layout_card.addWidget(self.label_icone, alignment=Qt.AlignHCenter)
        layout_card.addSpacing(12)

        self.label_titulo = QLabel("Atenção")
        self.label_titulo.setObjectName("label_titulo_aviso")
        self.label_titulo.setAlignment(Qt.AlignCenter)
        layout_card.addWidget(self.label_titulo)
        layout_card.addSpacing(12)

        self.label_mensagem = QLabel("Você precisa realizar a Zerésima\nantes de poder votar.")
        self.label_mensagem.setObjectName("label_mensagem_aviso")
        self.label_mensagem.setAlignment(Qt.AlignCenter)
        layout_card.addWidget(self.label_mensagem)

        layout_card.addStretch()

        self.botao_ok = QPushButton("OK")
        self.botao_ok.setObjectName("botao_ok_aviso")
        self.botao_ok.setCursor(Qt.PointingHandCursor)
        self.botao_ok.setFixedSize(190, 48)
        self.botao_ok.setDefault(True)
        self.botao_ok.clicked.connect(self.accept)
        layout_card.addWidget(self.botao_ok, alignment=Qt.AlignHCenter)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    with open("estilo/estilo_aviso_zeresima.qss", encoding="utf-8") as arquivo:
        app.setStyleSheet(arquivo.read())
    tela_aviso = TelaAvisoZeresima()
    tela_aviso.exec()