import os
import sys
from pathlib import Path
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

BASE_DIR = Path(__file__).resolve().parent
caminho_icone = BASE_DIR.parent / "Imagens" / "voting-box.png"
caminho_arquivo_qss = BASE_DIR.parent / "Estilos" / "estilo_tela_titulo.qss"


class TelaTituloEleitor(QWidget):

  def __init__(self, parent=None):
    super().__init__(parent)
    self.setWindowTitle("Título de Eleitor")
    self.setObjectName("tela_titulo_eleitor")

    self.carregar_estilo()

    layout_principal = QVBoxLayout(self)
    layout_principal.setContentsMargins(20, 20, 20, 20)
    layout_principal.setSpacing(16)


    self.label_icone = QLabel()
    self.label_icone.setFixedSize(80, 80)
    self.label_icone.setScaledContents(True)


    if caminho_icone.exists():
      icone = QPixmap(str(caminho_icone))
      if not icone.isNull():
        self.label_icone.setPixmap(icone)

    txt_votar = QLabel("VOTAR")
    txt_votar.setObjectName("titulo")

    txt_subtitulo = QLabel("Informe seu Título")
    txt_subtitulo.setObjectName("txt_subtitulo")

    layout_label = QVBoxLayout()
    layout_label.addWidget(txt_votar)
    layout_label.addWidget(txt_subtitulo)

    layout_cabecalho = QHBoxLayout()
    layout_cabecalho.addWidget(self.label_icone)
    layout_cabecalho.addLayout(layout_label)

    layout_principal.addLayout(layout_cabecalho)

 
    self.frame_input = QFrame()
    self.frame_input.setObjectName("background-inp")

    layout_frame = QVBoxLayout(self.frame_input)
    layout_frame.setSpacing(8)

    self.label_instrucao = QLabel("Título de Eleitor:")
    self.label_instrucao.setObjectName("layout")


    self.inp_titulo = QLineEdit()
    self.inp_titulo.setObjectName("inp_titulo")
    self.inp_titulo.setPlaceholderText("Digite o número do seu título")
    self.inp_titulo.setFixedSize(220, 36)

    layout_frame.addWidget(
        self.label_instrucao, alignment=Qt.AlignmentFlag.AlignCenter
    )
    layout_frame.addWidget(
        self.inp_titulo, alignment=Qt.AlignmentFlag.AlignCenter
    )

    layout_principal.addWidget(self.frame_input)


    layout_botoes = QHBoxLayout()

 
    self.botao_cancelar = QPushButton("CANCELAR")
    self.botao_cancelar.setObjectName("botao_cancelar")
    self.botao_cancelar.setCursor(
        Qt.CursorShape.PointingHandCursor
    ) 
    self.botao_cancelar.setFixedSize(110, 40)

    self.botao_confirmar = QPushButton("CONFIRMAR")
    self.botao_confirmar.setObjectName("botao_confirmar")
    self.botao_confirmar.setCursor(
        Qt.CursorShape.PointingHandCursor
    ) 
    self.botao_confirmar.setFixedSize(110, 40)

    layout_botoes.addWidget(self.botao_cancelar)
    layout_botoes.addWidget(self.botao_confirmar)

    layout_principal.addLayout(layout_botoes)
    layout_principal.addStretch(1)

  def carregar_estilo(self):

    if caminho_arquivo_qss.exists():
      try:
        with open(caminho_arquivo_qss, "r", encoding="utf-8") as arquivo:
          self.setStyleSheet(arquivo.read())
      except Exception as e:
        print(f"Erro ao ler o arquivo QSS: {e}")
    else:
      caminho_fallback = (
          BASE_DIR.parent / "estilo" / "estilo_tela_titulo.qss"
      )
      if caminho_fallback.exists():
        with open(caminho_fallback, "r", encoding="utf-8") as arquivo:
          self.setStyleSheet(arquivo.read())


if __name__ == "__main__":
  app = QApplication(sys.argv)
  janela = TelaTituloEleitor()
  janela.resize(400, 300)
  janela.show()
  sys.exit(app.exec())
  layout.addStretch(1)
