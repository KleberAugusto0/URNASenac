import os
import sys
from pathlib import Path
<<<<<<< HEAD
import sys,os
=======
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
>>>>>>> eac0097ea6991426ade9f3ce211e056fdcde9e25

BASE_DIR = Path(__file__).resolve().parent
caminho_icone = BASE_DIR.parent / "Imagens" / "voting-box.png"
caminho_arquivo_qss = BASE_DIR.parent / "Estilos" / "estilo_tela_titulo.qss"


class TelaTituloEleitor(QWidget):
<<<<<<< HEAD
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Título de Eleitor")
        
=======
>>>>>>> eac0097ea6991426ade9f3ce211e056fdcde9e25

  def __init__(self, parent=None):
    super().__init__(parent)
    self.setWindowTitle("Título de Eleitor")
    self.setObjectName("tela_titulo_eleitor")

<<<<<<< HEAD
        icone_votar = QLabel()
        icone_votar.setFixedSize(80,80)
        icone_votar.setScaledContents(True)
        icone = QPixmap(caminho_icone)
        icone_votar.setPixmap(icone)
        layout_label = QVBoxLayout()
        txt_votar = QLabel("VOTAR")
        txt_votar.setObjectName("titulo")
        txt_titulo = QLabel("Informe seu Titulo")
        layout_label.addWidget(txt_votar)
        layout_label.addWidget(txt_titulo)
=======
    self.carregar_estilo()
>>>>>>> eac0097ea6991426ade9f3ce211e056fdcde9e25

    layout_principal = QVBoxLayout(self)
    layout_principal.setContentsMargins(20, 20, 20, 20)
    layout_principal.setSpacing(16)


    self.lbl_icone = QLabel()
    self.lbl_icone.setFixedSize(80, 80)
    self.lbl_icone.setScaledContents(True)


    if caminho_icone.exists():
      icone = QPixmap(str(caminho_icone))
      if not icone.isNull():
        self.lbl_icone.setPixmap(icone)

<<<<<<< HEAD
        layout_botoes = QHBoxLayout()
        bnt_cancelar = QPushButton("CANCELAR")
        bnt_cancelar.setObjectName("btn_cancelar")

        bnt_confirmar = QPushButton("CONFIRMAR")
        bnt_confirmar.setObjectName("btn_confirmar")

        layout_botoes.addStretch(1)
        layout_botoes.addWidget(bnt_cancelar)
=======
    txt_votar = QLabel("VOTAR")
    txt_votar.setObjectName("titulo")

    txt_subtitulo = QLabel("Informe seu Título")
    txt_subtitulo.setObjectName("txt_subtitulo")

    layout_label = QVBoxLayout()
    layout_label.addWidget(txt_votar)
    layout_label.addWidget(txt_subtitulo)
>>>>>>> eac0097ea6991426ade9f3ce211e056fdcde9e25

    layout_cabecalho = QHBoxLayout()
    layout_cabecalho.addWidget(self.lbl_icone)
    layout_cabecalho.addLayout(layout_label)

    layout_principal.addLayout(layout_cabecalho)

<<<<<<< HEAD
        layout.addStretch(1)
        
=======
 
    self.frame_input = QFrame()
    self.frame_input.setObjectName("background-inp")

    layout_frame = QVBoxLayout(self.frame_input)
    layout_frame.setSpacing(8)

    self.lbl_instrucao = QLabel("Título de Eleitor:")
    self.lbl_instrucao.setObjectName("layout")


    self.inp_titulo = QLineEdit()
    self.inp_titulo.setObjectName("inp_titulo")
    self.inp_titulo.setPlaceholderText("Digite o número do seu título")
    self.inp_titulo.setFixedSize(220, 36)

    layout_frame.addWidget(
        self.lbl_instrucao, alignment=Qt.AlignmentFlag.AlignCenter
    )
    layout_frame.addWidget(
        self.inp_titulo, alignment=Qt.AlignmentFlag.AlignCenter
    )

    layout_principal.addWidget(self.frame_input)


    layout_botoes = QHBoxLayout()

 
    self.btn_cancelar = QPushButton("CANCELAR")
    self.btn_cancelar.setObjectName("btn_cancelar")
    self.btn_cancelar.setCursor(
        Qt.CursorShape.PointingHandCursor
    ) 
    self.btn_cancelar.setFixedSize(110, 40)

    self.btn_confirmar = QPushButton("CONFIRMAR")
    self.btn_confirmar.setObjectName("btn_confirmar")
    self.btn_confirmar.setCursor(
        Qt.CursorShape.PointingHandCursor
    ) 
    self.btn_confirmar.setFixedSize(110, 40)

    layout_botoes.addWidget(self.btn_cancelar)
    layout_botoes.addWidget(self.btn_confirmar)

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
>>>>>>> eac0097ea6991426ade9f3ce211e056fdcde9e25
