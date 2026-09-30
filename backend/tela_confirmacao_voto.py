import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QApplication, QDialog, QFrame, QHBoxLayout, QLabel, QPushButton, QVBoxLayout
)


class TelaConfirmacaoVoto(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("tela_confirmacao")
        self.setModal(True)
        self.setWindowFlags(Qt.WindowType.Dialog | Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setFixedSize(420, 320)
        self.montar_interface()
        with open("estilo/estilo_confirmacao_voto.qss", encoding="utf-8") as arquivo:
                self.setStyleSheet(arquivo.read())
        

    def montar_interface(self):
        layout_raiz = QVBoxLayout(self)
        layout_raiz.setContentsMargins(0, 0, 0, 0)

        self.card = QFrame()
        self.card.setObjectName("card_confirmacao")
        self.card.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        layout_raiz.addWidget(self.card)

        layout_card = QVBoxLayout(self.card)
        layout_card.setContentsMargins(20, 12, 20, 20)
        layout_card.setSpacing(0)

        self.btn_fechar = QPushButton("✕")
        self.btn_fechar.setObjectName("btn_fechar")
        self.btn_fechar.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_fechar.setFixedSize(28, 28)
        self.btn_fechar.clicked.connect(self.accept)

        layout_topo = QHBoxLayout()
        layout_topo.addStretch()
        layout_topo.addWidget(self.btn_fechar)
        layout_card.addLayout(layout_topo)

        self.lbl_icone = QLabel()
        self.lbl_icone.setObjectName("lbl_icone")
        self.lbl_icone.setAlignment(Qt.AlignmentFlag.AlignCenter)

        pixmap_icone = QPixmap("Imagens/correto.png")
        if not pixmap_icone.isNull():
            self.lbl_icone.setPixmap(
                pixmap_icone.scaled(
                    64, 64, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation
                )
            )

        layout_card.addWidget(self.lbl_icone, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout_card.addSpacing(16)

        self.lbl_titulo = QLabel("Voto registrado!")
        self.lbl_titulo.setObjectName("lbl_titulo")
        self.lbl_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_card.addWidget(self.lbl_titulo)
        layout_card.addSpacing(12)

        self.lbl_mensagem = QLabel("Seu voto foi registrado com sucesso.")
        self.lbl_mensagem.setObjectName("lbl_mensagem")
        self.lbl_mensagem.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_card.addWidget(self.lbl_mensagem)

        layout_card.addStretch()

        self.btn_ok = QPushButton("OK")
        self.btn_ok.setObjectName("btn_ok")
        self.btn_ok.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_ok.setFixedSize(190, 48)
        self.btn_ok.setDefault(True)
        self.btn_ok.clicked.connect(self.accept)
        layout_card.addWidget(self.btn_ok, alignment=Qt.AlignmentFlag.AlignHCenter)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    caminho_qss = "estilo/estilo_confirmacao_voto.qss"
    try:
        with open(caminho_qss, encoding="utf-8") as arquivo:
            app.setStyleSheet(arquivo.read())
    except FileNotFoundError:
        pass

    tela_confirmacao = TelaConfirmacaoVoto()
    tela_confirmacao.exec()