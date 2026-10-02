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

        self.botao_fechar = QPushButton("✕")
        self.botao_fechar.setObjectName("botao_fechar")
        self.botao_fechar.setCursor(Qt.CursorShape.PointingHandCursor)
        self.botao_fechar.setFixedSize(28, 28)
        self.botao_fechar.clicked.connect(self.accept)

        layout_topo = QHBoxLayout()
        layout_topo.addStretch()
        layout_topo.addWidget(self.botao_fechar)
        layout_card.addLayout(layout_topo)

        self.label_icone = QLabel()
        self.label_icone.setObjectName("label_icone")
        self.label_icone.setAlignment(Qt.AlignmentFlag.AlignCenter)

        pixmap_icone = QPixmap(str(__import__("pathlib").Path(__file__).resolve().parent.parent / "imagens" / "correto.png"))
        if not pixmap_icone.isNull():
            self.label_icone.setPixmap(
                pixmap_icone.scaled(
                    64, 64, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation
                )
            )

        layout_card.addWidget(self.label_icone, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout_card.addSpacing(16)

        self.label_titulo = QLabel("Voto registrado!")
        self.label_titulo.setObjectName("label_titulo")
        self.label_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_card.addWidget(self.label_titulo)
        layout_card.addSpacing(12)

        self.label_mensagem = QLabel("Seu voto foi registrado com sucesso.")
        self.label_mensagem.setObjectName("label_mensagem")
        self.label_mensagem.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_card.addWidget(self.label_mensagem)

        layout_card.addStretch()

        self.botao_ok = QPushButton("OK")
        self.botao_ok.setObjectName("botao_ok")
        self.botao_ok.setCursor(Qt.CursorShape.PointingHandCursor)
        self.botao_ok.setFixedSize(190, 48)
        self.botao_ok.setDefault(True)
        self.botao_ok.clicked.connect(self.accept)
        layout_card.addWidget(self.botao_ok, alignment=Qt.AlignmentFlag.AlignHCenter)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    caminho_qss = __import__("pathlib").Path(__file__).resolve().parent.parent / "estilo" / "estilo_confirmacao_voto.qss"
    if caminho_qss.exists():
        with open(caminho_qss, encoding="utf-8") as arquivo:
            app.setStyleSheet(arquivo.read())
    tela_confirmacao = TelaConfirmacaoVoto()
    tela_confirmacao.exec()