import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QDialog, QFrame, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QApplication
)


class TelaConfirmacaoVoto(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("tela_voto_nulo")
        self.setModal(True)
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint)
        self.setFixedSize(420, 320)
        self.montar_interface()


    def montar_interface(self):
        layout_raiz = QVBoxLayout(self)
        layout_raiz.setContentsMargins(24, 24, 24, 24)

        self.card = QFrame()
        self.card.setObjectName("card_voto_nulo")
        layout_raiz.addWidget(self.card)

        layout_card = QVBoxLayout(self.card)
        layout_card.setContentsMargins(20, 12, 20, 20)
        layout_card.setSpacing(0)

        self.btn_fechar = QPushButton("✕")
        self.btn_fechar.setObjectName("btn_fechar")
        self.btn_fechar.setCursor(Qt.PointingHandCursor)
        self.btn_fechar.setFixedSize(28, 28)
        self.btn_fechar.clicked.connect(self.reject)

        layout_topo = QHBoxLayout()
        layout_topo.addStretch()
        layout_topo.addWidget(self.btn_fechar)
        layout_card.addLayout(layout_topo)

        self.lbl_icone = QLabel()
        self.lbl_icone.setObjectName("lbl_icone")
        self.lbl_icone.setAlignment(Qt.AlignCenter)

        pixmap_icone = QPixmap("warning.webp")
        self.lbl_icone.setPixmap(
            pixmap_icone.scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        )

        layout_card.addWidget(self.lbl_icone, alignment=Qt.AlignHCenter)
        layout_card.addSpacing(16)

        self.lbl_titulo = QLabel("Voto nulo!")
        self.lbl_titulo.setObjectName("lbl_titulo")
        self.lbl_titulo.setAlignment(Qt.AlignCenter)
        layout_card.addWidget(self.lbl_titulo)
        layout_card.addSpacing(12)

        self.lbl_mensagem = QLabel("O número digitado não corresponde \n a nenhum candidato. \nDeseja confirmar o voto nulo?")
        self.lbl_mensagem.setObjectName("lbl_mensagem")
        self.lbl_mensagem.setAlignment(Qt.AlignCenter)
        layout_card.addWidget(self.lbl_mensagem)

        layout_card.addStretch()

        layout_botoes = QHBoxLayout()

    
        self.btn_cancelar = QPushButton("Cancelar")
        # self.btn_cancelar = self.btn_cancelar
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.btn_cancelar.setCursor(Qt.PointingHandCursor)
        self.btn_cancelar.setFixedSize(190, 48)
        self.btn_cancelar.setDefault(False)
        self.btn_cancelar.clicked.connect(self.reject)

        self.btn_confirmar = QPushButton("Confirmar")
        # self.btn_confirmar = self.btn_confirmar
        self.btn_confirmar.setObjectName("btn_confirmar")
        self.btn_confirmar.setCursor(Qt.PointingHandCursor)
        self.btn_confirmar.setFixedSize(190, 48)
        self.btn_confirmar.setDefault(True)
        self.btn_confirmar.clicked.connect(self.accept)


        layout_card.addLayout(layout_botoes)

        layout_botoes.setSpacing(16)   # espaço entre os botões

        layout_botoes.addWidget(self.btn_cancelar, alignment=Qt.AlignHCenter)
        layout_botoes.addWidget(self.btn_confirmar, alignment=Qt.AlignHCenter)

        

if __name__ == "__main__":
    app = QApplication(sys.argv)

    with open("estilo/estilo_pop_up_voto_nulo.qss", encoding="utf-8") as arquivo:
        app.setStyleSheet(arquivo.read())

    tela_confirmacao = TelaConfirmacaoVoto()
    tela_confirmacao.exec()


