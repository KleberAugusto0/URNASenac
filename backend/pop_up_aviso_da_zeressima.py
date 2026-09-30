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

        self.lbl_icone = QLabel()
        self.lbl_icone.setObjectName("lbl_icone_aviso")
        self.lbl_icone.setAlignment(Qt.AlignCenter)

        pixmap_icone = QPixmap("imagens/icone_informacao.png")
        self.lbl_icone.setPixmap(
            pixmap_icone.scaled(48, 48, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        )

        layout_card.addWidget(self.lbl_icone, alignment=Qt.AlignHCenter)
        layout_card.addSpacing(12)

        self.lbl_titulo = QLabel("Atenção")
        self.lbl_titulo.setObjectName("lbl_titulo_aviso")
        self.lbl_titulo.setAlignment(Qt.AlignCenter)
        layout_card.addWidget(self.lbl_titulo)
        layout_card.addSpacing(12)

        self.lbl_mensagem = QLabel("Você precisa realizar a Zerésima\nantes de poder votar.")
        self.lbl_mensagem.setObjectName("lbl_mensagem_aviso")
        self.lbl_mensagem.setAlignment(Qt.AlignCenter)
        layout_card.addWidget(self.lbl_mensagem)

        layout_card.addStretch()

        self.btn_ok = QPushButton("OK")
        self.btn_ok.setObjectName("btn_ok_aviso")
        self.btn_ok.setCursor(Qt.PointingHandCursor)
        self.btn_ok.setFixedSize(190, 48)
        self.btn_ok.setDefault(True)
        self.btn_ok.clicked.connect(self.accept)
        layout_card.addWidget(self.btn_ok, alignment=Qt.AlignHCenter)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    with open("estilo/estilo_aviso_zeresima.qss", encoding="utf-8") as arquivo:
        app.setStyleSheet(arquivo.read())
    tela_aviso = TelaAvisoZeresima()
    tela_aviso.exec()