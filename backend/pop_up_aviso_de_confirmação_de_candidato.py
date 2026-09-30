import sys
from pathlib import Path
from PySide6.QtWidgets import (
    QApplication, QDialog, QLabel, QPushButton, 
    QVBoxLayout, QHBoxLayout, QFrame
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QPainter, QColor

class PopupCandidato(QDialog):
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
        layout_card.setContentsMargins(16, 12, 16, 20)
        layout_card.setSpacing(6)

        layout_topo = QHBoxLayout()
        layout_topo.addStretch()
        
        btn_fechar = QPushButton("✕")
        btn_fechar.setObjectName("btn_fechar")
        btn_fechar.setCursor(Qt.CursorShape.PointingHandCursor)
        btn_fechar.clicked.connect(self.reject)
        layout_topo.addWidget(btn_fechar)

        avatar_box = QLabel()
        avatar_box.setObjectName("avatar_box")
        avatar_box.setFixedSize(80, 80)
        avatar_box.setPixmap(self.criar_avatar_placeholder())

        layout_avatar = QHBoxLayout()
        layout_avatar.addStretch()
        layout_avatar.addWidget(avatar_box)
        layout_avatar.addStretch()

        label_subtitulo = QLabel("Candidato")
        label_subtitulo.setObjectName("label_subtitulo")
        label_subtitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        label_nome = QLabel("João Silva")
        label_nome.setObjectName("label_nome")
        label_nome.setAlignment(Qt.AlignmentFlag.AlignCenter)

        label_numero = QLabel("Nº 12345")
        label_numero.setObjectName("label_numero")
        label_numero.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout_botoes = QHBoxLayout()
        layout_botoes.setSpacing(12)

        botao_cancelar = QPushButton("Cancelar")
        botao_cancelar.setObjectName("botao_cancelar")
        botao_cancelar.setCursor(Qt.CursorShape.PointingHandCursor)
        botao_cancelar.clicked.connect(self.reject)

        botao_confirmar = QPushButton("Confirmar")
        botao_confirmar.setObjectName("botao_confirmar")
        botao_confirmar.setCursor(Qt.CursorShape.PointingHandCursor)
        botao_confirmar.clicked.connect(self.accept)

        layout_botoes.addWidget(botao_cancelar)
        layout_botoes.addWidget(botao_confirmar)

        layout_card.addLayout(layout_topo)
        layout_card.addLayout(layout_avatar)
        layout_card.addSpacing(12)
        layout_card.addWidget(label_subtitulo)
        layout_card.addWidget(label_nome)
        layout_card.addWidget(label_numero)
        layout_card.addSpacing(10)
        layout_card.addLayout(layout_botoes)

        layout_principal.addWidget(self.card_container)
        self.setFixedSize(320, 290)

        self.carregar_estilo()

    def criar_avatar_placeholder(self):
        pixmap = QPixmap(80, 80)
        pixmap.fill(QColor("#93B9D6"))
        
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(QColor("#05192F"))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawEllipse(28, 16, 24, 24)
        painter.drawEllipse(15, 46, 50, 42)
        painter.end()
        
        return pixmap

    def carregar_estilo(self):
        base_dir = Path(__file__).resolve().parent
        caminhos_possiveis = [
            base_dir / "estilo_pop_up_aviso_de_confirmação_de_candidato.qss",
            base_dir / "estilo" / "estilo_pop_up_aviso_de_confirmação_de_candidato.qss",
            base_dir / "estilos" / "estilo_pop_up_aviso_de_confirmação_de_candidato.qss",
            base_dir.parent / "estilo" / "estilo_pop_up_aviso_de_confirmação_de_candidato.qss",
            base_dir.parent / "estilo_pop_up_aviso_de_confirmação_de_candidato.qss"
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
    popup = PopupCandidato()
    popup.exec()