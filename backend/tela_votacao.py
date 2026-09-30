import sys
from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from tela_confirmacao_voto import TelaConfirmacaoVoto
from candidatos import candidatos_cadastrados


class TelaDeVotacao(QMainWindow):

    VALOR_PADRAO = "00000"

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tela de Votação")
        self.setFixedSize(380, 470)

        janela_central = QWidget()
        self.setCentralWidget(janela_central)
        layout_principal = QVBoxLayout(janela_central)
        layout_principal.setContentsMargins(20, 20, 20, 20)
        layout_principal.setSpacing(16)

        layout_cabecalho = QHBoxLayout()
        layout_cabecalho.setContentsMargins(4, 0, 0, 0)
        layout_cabecalho.setSpacing(14)

        self.label_icone = QLabel()
        self.label_icone.setObjectName("iconeVotacao")
        self.label_icone.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        
        caminho_icone = Path(__file__).resolve().parent.parent / "imagens" / "voting-box.png"
        if not caminho_icone.exists():
            caminho_icone = Path(__file__).resolve().parent / "voting-box.png"

        if caminho_icone.exists():
            pixmap = QPixmap(str(caminho_icone)).scaled(
                44, 44, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation
            )
            self.label_icone.setPixmap(pixmap)

        layout_cabecalho.addWidget(self.label_icone)

        layout_textos = QVBoxLayout()
        layout_textos.setSpacing(1)
        layout_textos.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        label_titulo = QLabel("VOTAR")
        label_titulo.setObjectName("tituloVotar")

        label_subtitulo = QLabel("Digite o número do candidato")
        label_subtitulo.setObjectName("subtituloVotar")

        layout_textos.addWidget(label_titulo)
        layout_textos.addWidget(label_subtitulo)

        layout_cabecalho.addLayout(layout_textos)
        layout_cabecalho.addStretch()

        layout_principal.addLayout(layout_cabecalho)

        painel_teclado = QFrame()
        painel_teclado.setObjectName("painelTeclado")
        layout_painel = QVBoxLayout(painel_teclado)
        layout_painel.setContentsMargins(18, 18, 18, 18)
        layout_painel.setSpacing(14)

        self.visor = QLineEdit()
        self.visor.setObjectName("visor")
        self.visor.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.visor.setReadOnly(True)
        self.visor.setFixedHeight(58)

        self.digitos_digitados = ""

        layout_painel.addWidget(self.visor)

        layout_grade = QGridLayout()
        layout_grade.setSpacing(10)

        botoes_numericos = [
            ("1", 0, 0),
            ("2", 0, 1),
            ("3", 0, 2),
            ("4", 1, 0),
            ("5", 1, 1),
            ("6", 1, 2),
            ("7", 2, 0),
            ("8", 2, 1),
            ("9", 2, 2),
        ]

        for texto, linha, coluna in botoes_numericos:
            botao = QPushButton(texto)
            botao.setProperty("class", "botaoNumerico")
            botao.setFixedHeight(50)
            botao.clicked.connect(lambda _, t=texto: self.adicionar_digito(t))
            layout_grade.addWidget(botao, linha, coluna)

        botao_limpar = QPushButton("Limpar")
        botao_limpar.setObjectName("botaoLimpar")
        botao_limpar.setFixedHeight(50)
        botao_limpar.clicked.connect(self.limpar_visor)
        layout_grade.addWidget(botao_limpar, 3, 0)

        botao_zero = QPushButton("0")
        botao_zero.setProperty("class", "botaoNumerico")
        botao_zero.setFixedHeight(50)
        botao_zero.clicked.connect(lambda: self.adicionar_digito("0"))
        layout_grade.addWidget(botao_zero, 3, 1)

        botao_confirmar = QPushButton("Confirmar")
        botao_confirmar.setObjectName("botaoConfirmar")
        botao_confirmar.setFixedHeight(50)
        botao_confirmar.clicked.connect(lambda:self.autenticador())
        layout_grade.addWidget(botao_confirmar, 3, 2)

        layout_painel.addLayout(layout_grade)
        layout_principal.addWidget(painel_teclado)

        self.carregar_estilo()
        self.atualizar_visor()

    def carregar_estilo(self) -> None:
        caminho_estilo = Path(__file__).resolve().parent.parent / "estilo" / "estilo_tela_votacao.qss"

        if caminho_estilo.exists():
            with open(caminho_estilo, "r", encoding="utf-8") as arquivo:
                self.setStyleSheet(arquivo.read())
        else:
            print(f"Aviso: Arquivo de estilo não encontrado em {caminho_estilo}")
        

    def adicionar_digito(self, digito: str) -> None:
        if len(self.digitos_digitados) < 5:
            self.digitos_digitados += digito
            self.atualizar_visor()

    def limpar_visor(self) -> None:
        self.digitos_digitados = ""
        self.atualizar_visor()

    def atualizar_visor(self) -> None:
        if not self.digitos_digitados:
            self.visor.setText(self.VALOR_PADRAO)
            self.visor.setProperty("inativo", "true")
        else:
            self.visor.setText(self.digitos_digitados)
            self.visor.setProperty("inativo", "false")
        self.visor.style().unpolish(self.visor)
        self.visor.style().polish(self.visor)

    def autenticador(self):
        for candidado in candidatos_cadastrados:
            if candidado.numero == str(self.visor.text()):
                self.voto_confirmado()
            else:
                pass

    def voto_confirmado(self):
        TelaConfirmacaoVoto().exec()
         

    def voto_nulo(self):
        pass



if __name__ == "__main__":
    aplicacao = QApplication(sys.argv)
    janela = TelaDeVotacao()
    janela.show()
    sys.exit(aplicacao.exec())