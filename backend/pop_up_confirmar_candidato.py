import sys
from pathlib import Path
from PySide6.QtCore import Qt, QTimer, QUrl
from PySide6.QtGui import QPixmap
from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout, QLabel, QPushButton, QVBoxLayout)

try:
    from .candidatos import Candidato
except ImportError:
    from candidatos import Candidato

BASE_DIR = Path(__file__).resolve().parent


class TelaConfirmacaoVoto(QDialog):
    def __init__(self, candidato: Candidato, parent=None):
        super().__init__(parent)
        self.setObjectName("tela_confirmar_candidato")
        self.candidato = candidato
        self.setModal(True)
        self.setWindowFlags(Qt.WindowType.Dialog | Qt.WindowType.FramelessWindowHint)
        self.setFixedSize(420, 320)

        self.reprodutor = QMediaPlayer(self)
        self.audio = QAudioOutput(self)
        self.audio.setVolume(1.0)
        self.reprodutor.setAudioOutput(self.audio)

        caminho_som = BASE_DIR.parent / "efeitos_sonoros" / "som_urna.mp3"
        if caminho_som.exists():
            self.reprodutor.setSource(QUrl.fromLocalFile(str(caminho_som.resolve())))

        self.montar_interface()
        self.carregar_estilo()

    def carregar_estilo(self):
        caminho = BASE_DIR.parent / "estilo" / "estilo_confirmar_candidato.qss"
        if caminho.exists():
            with open(caminho, "r", encoding="utf-8") as arquivo:
                self.setStyleSheet(arquivo.read())

    def tocar_som_e_confirmar(self):
        if self.reprodutor.source().isValid():
            self.reprodutor.play()
            QTimer.singleShot(1500, self.accept)
        else:
            self.accept()

    def montar_interface(self):
        layout_raiz = QVBoxLayout(self)
        layout_raiz.setContentsMargins(24, 24, 24, 24)

        self.card = QFrame()
        self.card.setObjectName("card_confirmar_candidato")
        layout_raiz.addWidget(self.card)

        layout_card = QVBoxLayout(self.card)
        layout_card.setContentsMargins(20, 12, 20, 20)
        layout_card.setSpacing(0)

        self.botao_fechar = QPushButton("✕")
        self.botao_fechar.setObjectName("botao_fechar")
        self.botao_fechar.setCursor(Qt.CursorShape.PointingHandCursor)
        self.botao_fechar.setFixedSize(28, 28)
        self.botao_fechar.clicked.connect(self.reject)

        layout_topo = QHBoxLayout()
        layout_topo.addStretch()
        layout_topo.addWidget(self.botao_fechar)
        layout_card.addLayout(layout_topo)

        self.label_icone = QLabel()
        self.label_icone.setObjectName("label_icone")
        self.label_icone.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_icone.setFixedSize(64, 64)

        caminho_foto = Path(self.candidato.foto)
        if not caminho_foto.is_absolute():
            caminho_foto = BASE_DIR.parent / caminho_foto
        if caminho_foto.exists():
            pixmap = QPixmap(str(caminho_foto))
            if not pixmap.isNull():
                self.label_icone.setPixmap(
                    pixmap.scaled(
                        64,
                        64,
                        Qt.AspectRatioMode.KeepAspectRatio,
                        Qt.TransformationMode.SmoothTransformation,
                    )
                )
        else:
            self.label_icone.setText("Sem foto")

        layout_card.addWidget(self.label_icone, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout_card.addSpacing(13)

        self.label_titulo_candidato = QLabel("Candidato")
        self.label_titulo_candidato.setObjectName("label_titulo")
        self.label_titulo_candidato.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_card.addWidget(self.label_titulo_candidato)
        layout_card.addSpacing(10)

        self.label_titulo = QLabel(self.candidato.nome)
        self.label_titulo.setObjectName("label_titulo")
        self.label_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_card.addWidget(self.label_titulo)
        layout_card.addSpacing(10)

        self.label_mensagem = QLabel(self.candidato.numero)
        self.label_mensagem.setObjectName("label_mensagem")
        self.label_mensagem.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_card.addWidget(self.label_mensagem)

        layout_card.addStretch()

        layout_botoes = QHBoxLayout()
        layout_botoes.setSpacing(16)

        self.botao_cancelar = QPushButton("Cancelar")
        self.botao_cancelar.setObjectName("botao_cancelar")
        self.botao_cancelar.setCursor(Qt.CursorShape.PointingHandCursor)
        self.botao_cancelar.clicked.connect(self.reject)

        self.botao_confirmar = QPushButton("Confirmar")
        self.botao_confirmar.setObjectName("botao_confirmar")
        self.botao_confirmar.setCursor(Qt.CursorShape.PointingHandCursor)
        self.botao_confirmar.setDefault(True)
        self.botao_confirmar.clicked.connect(self.tocar_som_e_confirmar)

        layout_botoes.addWidget(self.botao_cancelar)
        layout_botoes.addWidget(self.botao_confirmar)
        layout_card.addLayout(layout_botoes)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    teste = Candidato("002", "Barriguinha mole", "Presidente", "imagens/candidato_barriguinha_mole.webp")
    tela_confirmacao = TelaConfirmacaoVoto(teste)
    tela_confirmacao.exec()