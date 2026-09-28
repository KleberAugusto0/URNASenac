import sys
from pathlib import Path
from PySide6.QtWidgets import (
    QApplication, QDialog, QLabel, QPushButton, 
    QVBoxLayout, QHBoxLayout, QFrame
)
from PySide6.QtCore import Qt

class PopupAtencao(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Dialog)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.init_ui()

    def init_ui(self):
        layout_principal = QVBoxLayout(self)
        layout_principal.setContentsMargins(10, 10, 10, 10)

        self.card_container = QFrame()
        self.card_container.setObjectName("card_container")
        
        layout_card = QVBoxLayout(self.card_container)
        layout_card.setContentsMargins(24, 20, 24, 20)
        layout_card.setSpacing(16)

        layout_cabecalho = QHBoxLayout()
        layout_cabecalho.setSpacing(12)

        icon_info = QLabel("i")
        icon_info.setObjectName("icon_info")

        label_titulo = QLabel("Atenção")
        label_titulo.setObjectName("label_titulo")

        layout_cabecalho.addWidget(icon_info)
        layout_cabecalho.addWidget(label_titulo)
        layout_cabecalho.addStretch()

        label_mensagem = QLabel("Você precisa realizar a Zeressima\nantes de poder votar.")
        label_mensagem.setObjectName("label_mensagem")
        label_mensagem.setAlignment(Qt.AlignmentFlag.AlignCenter)

        botao_ok = QPushButton("OK")
        botao_ok.setObjectName("botao_ok")
        botao_ok.setCursor(Qt.CursorShape.PointingHandCursor)
        botao_ok.clicked.connect(self.accept)

        layout_botao = QHBoxLayout()
        layout_botao.addStretch()
        layout_botao.addWidget(botao_ok)
        layout_botao.addStretch()

        layout_card.addLayout(layout_cabecalho)
        layout_card.addWidget(label_mensagem)
        layout_card.addSpacing(4)
        layout_card.addLayout(layout_botao)

        layout_principal.addWidget(self.card_container)
        self.setFixedSize(360, 200)

        self.carregar_estilo()

    def carregar_estilo(self):
        base_dir = Path(__file__).resolve().parent
        caminhos_possiveis = [
            base_dir / "estilo.qss",
            base_dir / "estilo" / "estilo.qss",
            base_dir / "estilos" / "estilo.qss",
            base_dir.parent / "estilo" / "estilo.qss",
            base_dir.parent / "estilo.qss"
        ]
        
        qss_encontrado = None
        for caminho in caminhos_possiveis:
            if caminho.exists():
                qss_encontrado = caminho
                break

        if qss_encontrado:
            self.setStyleSheet(qss_encontrado.read_text(encoding="utf-8"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    popup = PopupAtencao()
    popup.exec()