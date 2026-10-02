import sys
from pathlib import Path
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QDialog, QFrame, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QApplication

BASE_DIR = Path(__file__).resolve().parent


class TelaAvisoZeresima(QDialog):
    def __init__(self, acao="votar", parent=None):
        super().__init__(parent)
        self.setObjectName("tela_aviso")
        self.setModal(True)
        self.setWindowFlags(Qt.WindowType.Dialog | Qt.WindowType.FramelessWindowHint)
        self.setFixedSize(420, 320)
        self.acao = acao
        self.montar_interface()
        self.carregar_estilo()

    def carregar_estilo(self):
        caminho = BASE_DIR.parent / "estilo" / "estilo_aviso_zeresima.qss"
        if caminho.exists():
            with open(caminho, encoding="utf-8") as arquivo:
                self.setStyleSheet(arquivo.read())

    def montar_interface(self):
        layout_raiz = QVBoxLayout(self)
        layout_raiz.setContentsMargins(24, 24, 24, 24)

        self.card = QFrame()
        self.card.setObjectName("card_aviso")
        layout_raiz.addWidget(self.card)

        layout_card = QVBoxLayout(self.card)
        layout_card.setContentsMargins(24, 28, 24, 24)

        self.label_icone = QLabel()
        self.label_icone.setObjectName("label_icone_aviso")
        self.label_icone.setAlignment(Qt.AlignmentFlag.AlignCenter)
        caminho_icone = BASE_DIR.parent / "imagens" / "icone_informacao.png"
        if caminho_icone.exists():
            pixmap = QPixmap(str(caminho_icone))
            self.label_icone.setPixmap(pixmap.scaled(48, 48, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        layout_card.addWidget(self.label_icone, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout_card.addSpacing(12)

        self.label_titulo = QLabel("Atenção")
        self.label_titulo.setObjectName("label_titulo_aviso")
        self.label_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_card.addWidget(self.label_titulo)
        layout_card.addSpacing(12)

        acao_texto = "votar" if self.acao == "votar" else "emitir o Relatório Final"
        self.label_mensagem = QLabel(f"Você precisa realizar a Zerésima\nantes de poder {acao_texto}.")
        self.label_mensagem.setObjectName("label_mensagem_aviso")
        self.label_mensagem.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_card.addWidget(self.label_mensagem)
        layout_card.addStretch()

        self.botao_ok = QPushButton("OK")
        self.botao_ok.setObjectName("botao_ok_aviso")
        self.botao_ok.setCursor(Qt.CursorShape.PointingHandCursor)
        self.botao_ok.setFixedSize(190, 48)
        self.botao_ok.clicked.connect(self.accept)
        layout_card.addWidget(self.botao_ok, alignment=Qt.AlignmentFlag.AlignHCenter)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela_aviso = TelaAvisoZeresima()
    tela_aviso.exec()