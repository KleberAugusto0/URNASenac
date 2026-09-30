from PySide6.QtWidgets import QWidget,QVBoxLayout, QLabel, QPushButton,QHBoxLayout,QApplication,QLineEdit,QFrame
from PySide6.QtGui import QPixmap,Qt
from pathlib import Path
import sys,os
BASE_DIR = Path(__file__).resolve().parent
caminho_icone = BASE_DIR.parent / "imagens"/ "voting-box.png"
caminho_arquivo_qss = BASE_DIR.parent / "estilo" / "estilo_tela_titulo.qss"


class TelaTituloEleitor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Título de Eleitor")
        with open("estilo/estilo_tela_titulo.qss", "r", encoding="utf-8") as arquivo:
                self.setStyleSheet(arquivo.read())
        
        

        layout = QVBoxLayout()
        self.setLayout(layout)

        icone_votar = QLabel()
        icone_votar.setFixedSize(80,80)
        icone_votar.setScaledContents(True)
        icone = QPixmap(caminho_icone)
        icone_votar.setPixmap(icone)
    
        
        layout_label = QVBoxLayout()
        txt_votar = QLabel("VOTAR")
        txt_votar.setObjectName("titulo")
        txt_titulo = QLabel("Informe seu Titulo")
        txt_titulo.setObjectName("txt_subtitulo")
        layout_label.addWidget(txt_votar)
        layout_label.addWidget(txt_titulo)

        layout_horizontal = QHBoxLayout()
        layout_horizontal.addWidget(icone_votar)
        layout_horizontal.addLayout(layout_label)

        layout.addLayout(layout_horizontal)



        frame = QFrame()
        frame.setObjectName("background-inp")
        layout_frame = QVBoxLayout()
        layout_frame.setSpacing(0)
        frame.setLayout(layout_frame)
        inp_titulo = QLineEdit()
        inp_titulo.setPlaceholderText("Digite o número do seu título")
        inp_titulo.setFixedSize(200,30)
        txt_titulo_de_eleitor = QLabel("Título de Eleitor:")
        txt_titulo_de_eleitor.setObjectName("layout")
        layout_frame.addWidget(txt_titulo_de_eleitor,alignment=Qt.AlignmentFlag.AlignCenter)
        layout_frame.addWidget(inp_titulo,alignment=Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(frame)

        layout_botoes = QHBoxLayout()
        bnt_cancelar = QPushButton("CANCELAR")
        bnt_cancelar.setObjectName("btn_cancelar")
        bnt_cancelar.setFixedSize(90,40)

        bnt_confirmar = QPushButton("CONFIRMAR")
        bnt_confirmar.setObjectName("btn_confirmar")
        bnt_confirmar.setFixedSize(90,40)

        
        layout_botoes.addWidget(bnt_cancelar)

        layout_botoes.addWidget(bnt_confirmar)

        layout.addLayout(layout_botoes)

        layout.addStretch(1)