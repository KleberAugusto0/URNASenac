from PySide6.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QPushButton,
    QWidget,
    QApplication,
    QDialog,
    QHBoxLayout,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
import sys
import os


class MenuUrna(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Menu")

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.verificacao_zerezima = False

        layout.addStretch(1)

        txt_urna = QLabel("Urna Eletrônica")
        layout.addWidget(txt_urna)
        txt_urna.setAlignment(Qt.AlignmentFlag.AlignCenter)

        btn_zerezima = QPushButton("Rélatorio inicial (Zerézima)")
        layout.addWidget(
            btn_zerezima,
            alignment=Qt.AlignmentFlag.AlignCenter
        )
        btn_zerezima.setFixedSize(250, 50)

        btn_votar = QPushButton("Votar")
        layout.addWidget(
            btn_votar,
            alignment=Qt.AlignmentFlag.AlignCenter
        )
        btn_votar.setFixedSize(250, 50)

        btn_relatorio = QPushButton("Relatório Final")
        layout.addWidget(
            btn_relatorio,
            alignment=Qt.AlignmentFlag.AlignCenter
        )
        btn_relatorio.setFixedSize(250, 50)

        btn_sair = QPushButton("Sair")
        btn_sair.setObjectName("btn_sair")
        layout.addWidget(
            btn_sair,
            alignment=Qt.AlignmentFlag.AlignCenter
        )
        btn_sair.setFixedSize(250, 50)

        btn_zerezima.clicked.connect(self.zerezima)
        btn_votar.clicked.connect(self.votar)
        btn_relatorio.clicked.connect(self.relatorio)
        btn_sair.clicked.connect(self.sairDoSistema)

        layout.addStretch(1)

    def zerezima(self):
   
           tela_zerezima = QDialog(self)
           tela_zerezima.setFixedSize(600, 450)
           tela_zerezima.setWindowFlags(
               Qt.WindowType.FramelessWindowHint |
               Qt.WindowType.Dialog
           )
   
           caminho_estilo = os.path.join(
               os.path.dirname(__file__), "style.qss" 
           )
           if os.path.exists(caminho_estilo):
               with open(caminho_estilo, "r", encoding="utf-8") as f:
                   tela_zerezima.setStyleSheet(f.read())
   
          
           layout_principal = QVBoxLayout(tela_zerezima)
           layout_principal.setContentsMargins(50, 50, 50, 50)
           layout_principal.setSpacing(20)
   
           
           layout_principal.addStretch(1)
   
           
           lbl_titulo = QLabel("ZERÉZIMA")
           lbl_titulo.setObjectName("titulo_zerezima") 
           lbl_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
           layout_principal.addWidget(lbl_titulo)
   
           lbl_subtitulo = QLabel("Informações do Processo")
           lbl_subtitulo.setObjectName("subtitulo_zerezima")
           lbl_subtitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
           layout_principal.addWidget(lbl_subtitulo)

           icone = QLabel()
           icone.setObjectName("quadrado_icone")
           caminho_imagem = os.path.dirname(os.path.abspath(__file__))
           caminho_imagem = os.path.join(caminho_imagem,"imagens","voting-box.png")
           icone.setPixmap
           (QPixmap(caminho_imagem).scaled(150,150,Qt.AspectRatioMode.KeepAspectRatio))
           layout_principal.addSpacing(30)
   
          
           texto_informativo = (
               "A Zerézima é o procedimento que verifica se a urna está zerada,\n"
               "ou seja, sem nenhum voto registrado.\n\n"
               "Essa etapa garante a transparência\n"
               "e a segurança do processo de votação."
           )
           lbl_descricao = QLabel(texto_informativo)
           lbl_descricao.setObjectName("descricao_zerezima")
           lbl_descricao.setAlignment(Qt.AlignmentFlag.AlignCenter)
           layout_principal.addWidget(lbl_descricao)
   
           
           layout_principal.addStretch(1)
   
           
           layout_botoes = QHBoxLayout()
           layout_botoes.addStretch(1)  
   
           btn_voltar = QPushButton("Voltar")
           btn_voltar.setObjectName("btn_voltar_zerezima")
           btn_voltar.setFixedSize(150, 45)
           
          
           btn_voltar.clicked.connect(tela_zerezima.reject)
           
           layout_botoes.addWidget(btn_voltar)
           layout_principal.addLayout(layout_botoes)
   
          
           self.verificacao_zerezima = True
   
          
           tela_zerezima.exec()

    def votar(self):

        if self.verificacao_zerezima == True:
            pass  # fazer codigo para chamar a tela de votação

        elif self.verificacao_zerezima == False:
            pass  # fazer popup para fazer a zerezima primeiro

    def relatorio(self):
        pass

    def sairDoSistema(self):

        tela_sair = QDialog(self)

        tela_sair.setFixedSize(450, 280)

        tela_sair.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.Dialog
        )

        tela_alinhamento = QVBoxLayout(tela_sair)
        layout_botoes = QHBoxLayout()

        botao_fechar = QPushButton("×")
        botao_fechar.setObjectName("btn_fechar_x")
        botao_fechar.clicked.connect(tela_sair.close)

        tela_alinhamento.addWidget(
            botao_fechar,
            alignment=Qt.AlignmentFlag.AlignRight
        )

        icone = QLabel()
        icone.setObjectName("quadrado_icone")

        caminho_imagem = os.path.dirname(
            os.path.abspath(__file__)
        )

        caminho_imagem = os.path.join(
            caminho_imagem,
            "imagem",
            "imagem_sair.jpg"
        )

        icone.setPixmap(
            QPixmap(caminho_imagem).scaled(
                150,
                150,
                Qt.AspectRatioMode.KeepAspectRatio
            )
        )

        tela_alinhamento.addWidget(
            icone,
            alignment=Qt.AlignmentFlag.AlignCenter
        )

        titulo = QLabel("Sair do sistema")
        titulo.setObjectName("titulo_popup")

        subtitulo = QLabel("Tem certeza que deseja sair?")
        subtitulo.setObjectName("subtitulo_popup")

        tela_alinhamento.addWidget(
            titulo,
            alignment=Qt.AlignmentFlag.AlignCenter
        )

        tela_alinhamento.addWidget(
            subtitulo,
            alignment=Qt.AlignmentFlag.AlignCenter
        )

        botao_cancelar = QPushButton("Cancelar")
        botao_cancelar.setObjectName("btn_cancelar_dialog")
        botao_cancelar.clicked.connect(tela_sair.close)

        botao_confirmar = QPushButton("Confirmar")
        botao_confirmar.setObjectName("btn_confirmar_dialog")
        botao_confirmar.clicked.connect(QApplication.quit)

        layout_botoes.addWidget(botao_cancelar)
        layout_botoes.addWidget(botao_confirmar)

        tela_alinhamento.addLayout(layout_botoes)

        caminho_estilo = os.path.join(
            os.path.dirname(__file__),
            "estilo",
            "estilo_sair.qss"
        )

        with open(caminho_estilo,"r",encoding="utf-8") as arquivo:
            tela_sair.setStyleSheet(arquivo.read())
            tela_sair.exec()


if __name__ == "__main__":

    app = QApplication(sys.argv)

    caminho_estiloMenu = os.path.join(
        os.path.dirname(__file__),
        "estilo",
        "estilo_menu.qss"
    )

    with open(
        caminho_estiloMenu,
        "r",
        encoding="utf-8"
    ) as arquivo:
        app.setStyleSheet(arquivo.read())

    janela = MenuUrna()
    janela.show()

    sys.exit(app.exec())

      
