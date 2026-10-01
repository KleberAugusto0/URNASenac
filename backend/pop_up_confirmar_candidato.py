import os
import sys
from PySide6.QtCore import Qt, QTimer, QUrl
from PySide6.QtGui import QPixmap
from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
)


class TelaConfirmacaoVoto(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("tela_confirmar_candidato")
        self.setModal(True)
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint)
        self.setFixedSize(420, 320)

        

        self.reprodutor = QMediaPlayer(self)
        self.audio = QAudioOutput(self)
        self.reprodutor.setAudioOutput(self.audio)

        base_dir = os.path.dirname(os.path.abspath(__file__))
        caminho_som = os.path.join(base_dir, "..", "efeitos_sonoros", "som_urna.mp3")
        if not os.path.exists(caminho_som):
            caminho_som = os.path.join(base_dir, "efeitos_sonoros", "som_urna.mp3")

        self.reprodutor.setSource(QUrl.fromLocalFile(caminho_som))

        self.montar_interface()

    def tocar_som_e_confirmar(self):
        self.reprodutor.play()
        QTimer.singleShot(1500, self.accept)

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
        self.botao_fechar.setCursor(Qt.PointingHandCursor)
        self.botao_fechar.setFixedSize(28, 28)
        self.botao_fechar.clicked.connect(self.reject)

        layout_topo = QHBoxLayout()
        layout_topo.addStretch()
        layout_topo.addWidget(self.botao_fechar)
        layout_card.addLayout(layout_topo)

        self.label_icone = QLabel()
        self.label_icone.setObjectName("label_icone")
        self.label_icone.setAlignment(Qt.AlignCenter)

        pixmap_icone = QPixmap("imagens/") #Parametro que recebe a foto do candidato
        self.label_icone.setPixmap(
            pixmap_icone.scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        )

        
        layout_card.addWidget(self.label_icone, alignment=Qt.AlignHCenter)
        layout_card.addSpacing(13)

        self.label_titulo_candidato = QLabel("Candidato")
        self.label_titulo_candidato.setObjectName("label_titulo")
        self.label_titulo_candidato.setAlignment(Qt.AlignCenter)
        layout_card.addWidget(self.label_titulo_candidato)
        layout_card.addSpacing(10)

        self.label_titulo = QLabel("Mateus") #Parametro do nome do candidato
        self.label_titulo.setObjectName("label_titulo")
        self.label_titulo.setAlignment(Qt.AlignCenter)
        layout_card.addWidget(self.label_titulo)
        layout_card.addSpacing(10)

        self.label_mensagem = QLabel("13") #Parametro do numero 
        self.label_mensagem.setObjectName("label_mensagem")
        self.label_mensagem.setAlignment(Qt.AlignCenter)
        layout_card.addWidget(self.label_mensagem)

        layout_card.addStretch()

        layout_botoes = QHBoxLayout()

    
        self.botao_cancelar = QPushButton("Cancelar")

        self.botao_cancelar.setObjectName("botao_cancelar")
        self.botao_cancelar.setCursor(Qt.PointingHandCursor)
        self.botao_cancelar.setDefault(False)
        self.botao_cancelar.clicked.connect(self.reject)

        self.botao_confirmar = QPushButton("Confirmar")
        self.botao_confirmar.setObjectName("botao_confirmar")
        self.botao_confirmar.setCursor(Qt.PointingHandCursor)
        self.botao_confirmar.setDefault(True)
        self.botao_confirmar.clicked.connect(self.tocar_som_e_confirmar)


        layout_card.addLayout(layout_botoes)

        layout_botoes.setSpacing(16)   # espaço entre os botões

        layout_botoes.addWidget(self.botao_cancelar)
        layout_botoes.addWidget(self.botao_confirmar)




if __name__ == "__main__":
    app = QApplication(sys.argv)

    with open("estilo/estilo_confirmar_candidato.qss", encoding="utf-8") as arquivo:
        app.setStyleSheet(arquivo.read())

    tela_confirmacao = TelaConfirmacaoVoto()
    tela_confirmacao.exec()