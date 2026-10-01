import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout, QLabel, QPushButton, QVBoxLayout)


class TelaVotoNulo(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("tela_voto_nulo")
        self.setModal(True)
        self.setWindowFlags(Qt.WindowType.Dialog | Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setFixedSize(420, 320)
        self.montar_interface()

    def montar_interface(self):
        layout_raiz = QVBoxLayout(self)
        layout_raiz.setContentsMargins(0, 0, 0, 0)

        self.card = QFrame()
        self.card.setObjectName("card_voto_nulo")
        self.card.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
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

        pixmap_icone = QPixmap(str(__import__("pathlib").Path(__file__).resolve().parent.parent / "imagens" / "icone_alerta.png"))
        if not pixmap_icone.isNull():
            self.label_icone.setPixmap(
                pixmap_icone.scaled(
                    64, 64, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation
                )
            )

        layout_card.addWidget(self.label_icone, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout_card.addSpacing(16)

        self.label_titulo = QLabel("Voto nulo!")
        self.label_titulo.setObjectName("label_titulo")
        self.label_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_card.addWidget(self.label_titulo)
        layout_card.addSpacing(12)

        self.label_mensagem = QLabel(
            "O número digitado não corresponde \na nenhum candidato. \nDeseja confirmar o voto nulo?"
        )
        self.label_mensagem.setObjectName("label_mensagem")
        self.label_mensagem.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_card.addWidget(self.label_mensagem)

        layout_card.addStretch()

        layout_botoes = QHBoxLayout()
        layout_botoes.setSpacing(16)

        self.botao_cancelar = QPushButton("Cancelar")
        self.botao_cancelar.setObjectName("botao_cancelar")
        self.botao_cancelar.setCursor(Qt.CursorShape.PointingHandCursor)
        self.botao_cancelar.setDefault(False)
        self.botao_cancelar.clicked.connect(self.reject)

        self.botao_confirmar = QPushButton("Confirmar")
        self.botao_confirmar.setObjectName("botao_confirmar")
        self.botao_confirmar.setCursor(Qt.CursorShape.PointingHandCursor)
        self.botao_confirmar.setDefault(True)
        self.botao_confirmar.clicked.connect(self.accept)

        layout_botoes.addWidget(self.botao_cancelar)
        layout_botoes.addWidget(self.botao_confirmar)

        layout_card.addLayout(layout_botoes)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    caminho_qss = "estilo/estilo_pop_up_voto_nulo.qss"
    try:
        with open(caminho_qss, encoding="utf-8") as arquivo:
            app.setStyleSheet(arquivo.read())
    except FileNotFoundError:
        print(f"Aviso: Não foi possível carregar o QSS em '{caminho_qss}'. Verifique a pasta.")

    tela_voto_nulo = TelaVotoNulo()
    tela_voto_nulo.exec()