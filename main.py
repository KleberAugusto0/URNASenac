from PySide6.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QPushButton,
    QWidget,
    QApplication,
    QDialog,
    QHBoxLayout,
    QScrollArea,
    QFrame,
)
from PySide6.QtCore import Qt,QSize
from PySide6.QtGui import QPixmap,QIcon

from datetime import datetime
import sys
import os


class MenuUrna(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(380,470)
        self.setWindowTitle("Menu")

        layout = QVBoxLayout()
        self.setLayout(layout)
        

        verificacao_zerezima = True

        self.verificacao_zerezima = False
        
        layout.addStretch(1)

        layout_horizotal = QHBoxLayout()

        icone_urna = QLabel()
        img_icone_urna = QPixmap( os.path.join(os.path.dirname(__file__), "imagens", "voting-box.png"))
        icone_urna.setPixmap(img_icone_urna)
        icone_urna.setScaledContents(True)
        icone_urna.setFixedSize(80,80)
        

        txt_urna = QLabel("Urna Eletrônica")
        layout_horizotal.addWidget(icone_urna)
        layout_horizotal.addWidget(txt_urna)
        layout.addLayout(layout_horizotal)
        txt_urna.setAlignment(Qt.AlignmentFlag.AlignCenter)

        btn_zerezima = QPushButton("Relatório inicial (Zerézima)")
        layout.addWidget(btn_zerezima, alignment=Qt.AlignmentFlag.AlignCenter)
        btn_zerezima.setFixedSize(250, 50)
        icone_zerezima = QIcon( os.path.join(os.path.dirname(__file__), "imagens", "icone_documento.png"))
        btn_zerezima.setIcon(icone_zerezima)
        btn_zerezima.setIconSize(QSize(24,24))

        btn_votar = QPushButton("Votar")
        btn_votar.clicked.connect(lambda:votar())
        btn_votar.setCursor(Qt.CursorShape.PointingHandCursor)
        layout.addWidget(btn_votar,alignment=Qt.AlignmentFlag.AlignCenter)
        btn_votar.setFixedSize(250,50)
        icone_votar = QIcon( os.path.join(os.path.dirname(__file__), "imagens", "voting-box.png"))
        btn_votar.setIcon(icone_votar)
        btn_votar.setIconSize(QSize(24,24))
    

        btn_relatorio = QPushButton("Relatório Final")
        layout.addWidget(btn_relatorio, alignment=Qt.AlignmentFlag.AlignCenter)
        btn_relatorio.setFixedSize(250, 50)
        icone_reltorio = QIcon( os.path.join(os.path.dirname(__file__), "imagens", "icone_grafico.png"))
        btn_relatorio.setIcon(icone_reltorio)
        btn_relatorio.setIconSize(QSize(24,24))

        btn_sair = QPushButton("Sair")
        btn_sair.setObjectName("btn_sair")
        layout.addWidget(btn_sair, alignment=Qt.AlignmentFlag.AlignCenter)
        btn_sair.setFixedSize(250, 50)
        icone_sair = QIcon( os.path.join(os.path.dirname(__file__), "imagens", "exit.png"))
        btn_sair.setIcon(icone_sair)
        btn_sair.setIconSize(QSize(24,24))

        btn_zerezima.clicked.connect(self.zerezima)
        btn_votar.clicked.connect(self.votar)
        btn_relatorio.clicked.connect(self.relatorio)
        btn_sair.clicked.connect(self.sairDoSistema)

        layout.addStretch(1)

    def zerezima(self):

        def _label(texto, tamanho=26, cor="white", negrito=False):
            titular = QLabel(texto)
            titular.setObjectName("texto_informacao")
            peso = "bold" if negrito else "normal"
            titular.setStyleSheet(
                f"font-size: {tamanho}px; color: {cor}; font-weight: {peso}; "
                "background: transparent; font-family: 'Segoe UI', sans-serif;"
            )
            titular.setAlignment(Qt.AlignmentFlag.AlignLeft)
            return titular

        def _caixa():
            caixa = QWidget()
            caixa.setObjectName("caixa_informacoes")
            caixa.setStyleSheet("""
                QWidget#caixa_informacoes {
                    background-color: transparent;
                    border: 1px solid #122c54;
                    border-radius: 8px;
                }
            """)
            return caixa

        tela_zerezima = QDialog(self)

        tela_zerezima.setWindowState(Qt.WindowState.WindowFullScreen)
        tela_zerezima.setWindowFlags(
            Qt.WindowType.FramelessWindowHint | Qt.WindowType.Dialog
        )

        caminho_estilo = os.path.join(
            os.path.dirname(__file__), "estilo", "estilo_zerezima.qss"
        )

    

        layout_principal = QVBoxLayout(tela_zerezima)
        layout_principal.setContentsMargins(0, 0, 0, 0)
        layout_principal.setSpacing(0)

        painel_central = QWidget()
        painel_central.setObjectName("painel_central")
        painel_central.setStyleSheet("""
            QWidget#painel_central {
                background-color: #13263C;
                border: none;
            }
        """)

        layout_painel = QVBoxLayout(painel_central)
        layout_painel.setContentsMargins(80, 40, 80, 40)
        layout_painel.setSpacing(0)

        
        layout_topo_painel = QHBoxLayout()
        layout_topo_painel.setSpacing(35)

        icone = QLabel()
        icone.setObjectName("quadrado_icone")
        caminho_imagem = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "imagens", "voting-box.png"
        )
        icone.setPixmap(
            QPixmap(caminho_imagem).scaled(
                100, 100,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )
        )



        self.cand_numeros = [10, 20, 30]
        self.cand_nomes = ["Candidato 01", "Candidato 02", "Candidato 03"]
        self.cand_partidos = ["Partido A", "Partido B", "Partido C"]
        self.cand_votos = [0, 0, 0]
        
        self.eleitor_titulos = ["1001", "1002", "1003", "1004", "1005"]
        self.eleitor_nomes = ["goku rodrigues", "guts rogerio", "naruto nicolau", "MauMauOditaddor", "EOMANAURA"]
        self.eleitor_votou = [False, False, False, False, False]

        
        self.votos_brancos = 0
        self.votos_nulos = 0

        layout_topo_painel.addWidget(icone)

        layout_titulos = QVBoxLayout()
        layout_titulos.setSpacing(6)
        layout_titulos.addWidget(_label("ZERÉSIMA", 40, "white", True))
        layout_titulos.addWidget(_label("Relatório Inicial", 24, "#8fa0b5"))
        layout_topo_painel.addLayout(layout_titulos)

        layout_topo_painel.addStretch()

        
        agora = datetime.now().strftime("%d/%m/%Y  %H:%M:%S")
        lbl_data = _label(f"Emitido em: {agora}", 24, "#8fa0b5")
        lbl_data.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop)
        layout_topo_painel.addWidget(lbl_data)

        layout_painel.addLayout(layout_topo_painel)
        layout_painel.addSpacing(30)

        
        layout_corpo = QHBoxLayout()
        layout_corpo.setSpacing(30)

      
        caixa_cand = _caixa()
        layout_cand = QVBoxLayout(caixa_cand)
        layout_cand.setContentsMargins(40, 30, 40, 30)
        layout_cand.setSpacing(14)

        layout_cand.addWidget(_label("Candidatos", 28, "#8fa0b5", True))

        for i in range(len(self.cand_nomes)):
            texto = (
                f"{self.cand_numeros[i]} - {self.cand_nomes[i]} "
                f"({self.cand_partidos[i]}) ... {self.cand_votos[i]} votos"
            )
            layout_cand.addWidget(_label(texto, 24))

        layout_cand.addSpacing(10)
        layout_cand.addWidget(_label(f"Votos em branco ... {self.votos_brancos}", 24))
        layout_cand.addWidget(_label(f"Votos nulos ... {self.votos_nulos}", 24))
        layout_cand.addStretch()

        
        caixa_eleit = _caixa()
        layout_eleit = QVBoxLayout(caixa_eleit)
        layout_eleit.setContentsMargins(40, 30, 40, 30)
        layout_eleit.setSpacing(14)

        layout_eleit.addWidget(_label("Eleitores aptos", 28, "#8fa0b5", True))

        area_scroll = QScrollArea()
        area_scroll.setWidgetResizable(True)
        area_scroll.setFrameShape(QFrame.Shape.NoFrame)
        area_scroll.setStyleSheet("background: transparent; border: none;")

        conteudo_scroll = QWidget()
        conteudo_scroll.setStyleSheet("background: transparent;")
        layout_lista = QVBoxLayout(conteudo_scroll)
        layout_lista.setContentsMargins(0, 0, 0, 0)
        layout_lista.setSpacing(10)

        for i in range(len(self.eleitor_nomes)):
            situacao = "Já votou" if self.eleitor_votou[i] else "Não votou"
            cor = "#ff5c5c" if self.eleitor_votou[i] else "#4cd964"
            texto = f"Título {self.eleitor_titulos[i]} - {self.eleitor_nomes[i]}"
            linha = QHBoxLayout()
            linha.addWidget(_label(texto, 22))
            linha.addStretch()
            linha.addWidget(_label(situacao, 22, cor, True))
            layout_lista.addLayout(linha)

        layout_lista.addStretch()
        area_scroll.setWidget(conteudo_scroll)
        layout_eleit.addWidget(area_scroll)

        layout_corpo.addWidget(caixa_cand, 1)
        layout_corpo.addWidget(caixa_eleit, 1)
        layout_painel.addLayout(layout_corpo, 1)

        
        layout_botoes = QHBoxLayout()
        layout_botoes.addStretch()

        botao_voltar = QPushButton("Voltar")
        botao_voltar.setObjectName("btn_voltar_zerezima")
        botao_voltar.setFixedSize(260, 70)
        botao_voltar.setStyleSheet("""
            QPushButton#btn_voltar_zerezima {
                background-color: #0066ff;
                color: white;
                font-size: 26px;
                font-weight: bold;
                border: none;
                border-radius: 8px;
            }
            QPushButton#btn_voltar_zerezima:hover {
                background-color: #4B6685cc;
            }
        """)
        botao_voltar.clicked.connect(tela_zerezima.close)
        layout_botoes.addWidget(botao_voltar)

        layout_painel.addSpacing(20)
        layout_painel.addLayout(layout_botoes)

        layout_principal.addWidget(painel_central)

        if os.path.exists(caminho_estilo):
            with open("estilo/estilo_zeresimo.qss", "r", encoding="utf-8") as arquivo:tela_zerezima.setStyleSheet(arquivo.read())

        
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

        tela_sair.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Dialog)

        tela_alinhamento = QVBoxLayout(tela_sair)
        layout_botoes = QHBoxLayout()

        botao_fechar = QPushButton("×")
        botao_fechar.setObjectName("btn_fechar_x")
        botao_fechar.clicked.connect(tela_sair.close)

        tela_alinhamento.addWidget(botao_fechar, alignment=Qt.AlignmentFlag.AlignRight)

        icone = QLabel()
        icone.setObjectName("quadrado_icone")

        caminho_imagem = os.path.dirname(os.path.abspath(__file__))
        caminho_imagem = os.path.join(caminho_imagem, "imagens", "exit.png")

        icone.setPixmap(QPixmap(caminho_imagem).scaled(78, 78, Qt.AspectRatioMode.KeepAspectRatio))

        tela_alinhamento.addWidget(icone, alignment=Qt.AlignmentFlag.AlignCenter)
        titulo = QLabel("Sair do sistema")
        titulo.setObjectName("titulo_popup")

        subtitulo = QLabel("Tem certeza que deseja sair?")
        subtitulo.setObjectName("subtitulo_popup")

        tela_alinhamento.addWidget(titulo, alignment=Qt.AlignmentFlag.AlignCenter)
        tela_alinhamento.addWidget(subtitulo, alignment=Qt.AlignmentFlag.AlignCenter)

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
            os.path.dirname(__file__), "estilo", "estilo_sair.qss"
        )

        with open(caminho_estilo, "r", encoding="utf-8") as arquivo:
            tela_sair.setStyleSheet(arquivo.read())

        tela_sair.exec()


if __name__ == "__main__":

    app = QApplication(sys.argv)

    caminho_estiloMenu = os.path.join(os.path.dirname(__file__), "estilo", "estilo_menu.qss")

    with open(caminho_estiloMenu, "r", encoding="utf-8") as arquivo:
        app.setStyleSheet(arquivo.read())

    janela = MenuUrna()
    janela.show()

    sys.exit(app.exec())
