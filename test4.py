
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

        # Ativa o modo de tela cheia real no monitor
        tela_zerezima.setWindowState(Qt.WindowState.WindowFullScreen)

        tela_zerezima.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.Dialog
        )

        caminho_estilo = os.path.join(
            os.path.dirname(__file__),
            "estilo",
            "estilo_zerezima.qss"
        )
        
        # Layout Principal da Janela - Margens zeradas para cobrir o monitor inteiro
        layout_principal = QVBoxLayout(tela_zerezima)
        layout_principal.setContentsMargins(0, 0, 0, 0)
        layout_principal.setSpacing(0)

        # 1. Painel Central Escuro - O fundo total da tela cheia
        painel_central = QWidget()
        painel_central.setObjectName("painel_central")
        painel_central.setStyleSheet("""
            QWidget#painel_central {
                background-color: #061122; 
                border: none;
            }
        """)
        
        layout_painel = QVBoxLayout(painel_central)
        layout_painel.setContentsMargins(80, 60, 80, 60)
        layout_painel.setSpacing(0)

        # Título Externo no topo esquerdo do monitor
        titulo_externo = QLabel("3. Tela Zeressima - informações")
        titulo_externo.setObjectName("titulo_externo")
        titulo_externo.setStyleSheet("font-size: 34px; font-weight: bold; color: white; background: transparent; margin-bottom: 30px;")
        titulo_externo.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout_painel.addWidget(titulo_externo)

        # Cabeçalho Interno (Ícone + Títulos)
        layout_topo_painel = QHBoxLayout()
        layout_topo_painel.setSpacing(35)
        layout_topo_painel.setAlignment(Qt.AlignmentFlag.AlignLeft)

        icone = QLabel()
        icone.setObjectName("quadrado_icone")
        caminho_imagem = os.path.dirname(os.path.abspath(__file__))
        caminho_imagem = os.path.join(caminho_imagem, "imagens", "voting-box.png")
        icone.setPixmap(QPixmap(caminho_imagem).scaled(120, 120, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        layout_topo_painel.addWidget(icone)

        layout_titulos = QVBoxLayout()
        layout_titulos.setSpacing(6)
        
        subtitulo = QLabel("ZERESSIMA")
        subtitulo.setObjectName("subtitulo_zerezima")
        subtitulo.setStyleSheet("font-size: 42px; font-weight: bold; color: white; background: transparent;")
        
        status = QLabel("Informações do Processo")
        status.setObjectName("status_zerezima")
        status.setStyleSheet("font-size: 26px; color: #8fa0b5; background: transparent;")
        
        layout_titulos.addWidget(subtitulo)
        layout_titulos.addWidget(status)
        layout_topo_painel.addLayout(layout_titulos)
        
        layout_painel.addLayout(layout_topo_painel)
        layout_painel.addSpacing(45)

        # 2. Caixa de Informações - Agora contendo a listagem de candidatos e votos
        caixa_informacoes = QWidget()
        caixa_informacoes.setObjectName("caixa_informacoes")
        caixa_informacoes.setStyleSheet("""
            QWidget#caixa_informacoes {
                background-color: transparent; 
                border: 1px solid #122c54; 
                border-radius: 8px;
            }
        """)
        
        layout_caixa = QVBoxLayout(caixa_informacoes)
        layout_caixa.setContentsMargins(50, 50, 50, 50)
        layout_caixa.setSpacing(20)

        # Adiciona dinamicamente os Candidatos com 0 votos
        candidatos = ["Candidato 01", "Candidato 02", "Candidato 03"]
        for candidato in candidatos:
            label_candidato = QLabel(f"{candidato} ...0 votos")
            label_candidato.setObjectName("texto_informacao")
            label_candidato.setStyleSheet("font-size: 32px; color: white; background: transparent; font-family: 'Segoe UI', sans-serif;")
            label_candidato.setAlignment(Qt.AlignmentFlag.AlignLeft)
            layout_caixa.addWidget(label_candidato)

        # Adiciona Votos Brancos
        votos_brancos = QLabel("Votos brancos ... 0")
        votos_brancos.setObjectName("texto_informacao")
        votos_brancos.setStyleSheet("font-size: 32px; color: white; background: transparent; font-family: 'Segoe UI', sans-serif; margin-top: 10px;")
        votos_brancos.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout_caixa.addWidget(votos_brancos)

        # Adiciona Votos Nulos
        votos_nulos = QLabel("Votos nulos ... 0")
        votos_nulos.setObjectName("texto_informacao")
        votos_nulos.setStyleSheet("font-size: 32px; color: white; background: transparent; font-family: 'Segoe UI', sans-serif;")
        votos_nulos.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout_caixa.addWidget(votos_nulos)

        layout_painel.addWidget(caixa_informacoes)
        
        # Mola elástica para empurrar o botão de voltar ao rodapé do monitor
        layout_painel.addStretch()

        # 3. Rodapé (Botão "Voltar" no canto inferior direito)
        layout_botoes = QHBoxLayout()
        layout_botoes.addStretch()

        botao_voltar = QPushButton("Voltar")
        botao_voltar.setObjectName("btn_voltar_zerezima")
        botao_voltar.setFixedSize(260, 75)
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
                background-color: #0052cc;
            }
        """)
        botao_voltar.clicked.connect(tela_zerezima.close)

        layout_botoes.addWidget(botao_voltar)
        layout_painel.addLayout(layout_botoes)

        layout_principal.addWidget(painel_central)

        # Aplica a folha de estilo externa (.qss) se existir
        if os.path.exists(caminho_estilo):
            with open(caminho_estilo, "r", encoding="utf-8") as arquivo:
                tela_zerezima.setStyleSheet(arquivo.read())

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

        tela_sair.setWindowFlags(Qt.WindowType.FramelessWindowHint|Qt.WindowType.Dialog)

        tela_alinhamento = QVBoxLayout(tela_sair)
        layout_botoes = QHBoxLayout()

        botao_fechar = QPushButton("×")
        botao_fechar.setObjectName("btn_fechar_x")
        botao_fechar.clicked.connect(tela_sair.close)

        tela_alinhamento.addWidget(botao_fechar,alignment=Qt.AlignmentFlag.AlignRight)

        icone = QLabel()
        icone.setObjectName("quadrado_icone")

        caminho_imagem = os.path.dirname(os.path.abspath(__file__))

        caminho_imagem = os.path.join(caminho_imagem,"imagens","exit.png")

        icone.setPixmap(QPixmap(caminho_imagem).scaled(78,78,Qt.AspectRatioMode.KeepAspectRatio))
        
        tela_alinhamento.addWidget(icone,alignment=Qt.AlignmentFlag.AlignCenter)
        titulo = QLabel("Sair do sistema")
        titulo.setObjectName("titulo_popup")
        
        subtitulo = QLabel("Tem certeza que deseja sair?")
        subtitulo.setObjectName("subtitulo_popup")
        
        tela_alinhamento.addWidget(titulo,alignment=Qt.AlignmentFlag.AlignCenter)
        tela_alinhamento.addWidget(subtitulo,alignment=Qt.AlignmentFlag.AlignCenter)

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

        with open(
            caminho_estilo,
            "r",
            encoding="utf-8"
        ) as arquivo:
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

   

















































