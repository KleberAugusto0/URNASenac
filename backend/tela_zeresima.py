from pathlib import Path
from datetime import datetime
from PySide6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel, QWidget, QScrollArea, QFrame, QPushButton)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

BASE_DIR = Path(__file__).resolve().parent


class TelaZerezima(QDialog):
    def __init__(self, urna=None, titulo="ZERÉSIMA", subtitulo="Relatório Inicial", parent=None):
        super().__init__(parent)
        self.urna = urna
        self.titulo_relatorio = titulo
        self.subtitulo_relatorio = subtitulo

        self.setWindowState(Qt.WindowState.WindowFullScreen)
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint | Qt.WindowType.Dialog
        )

        self.cand_numeros = [c.numero for c in urna.candidatos] if urna else ["001", "002", "003"]
        self.cand_nomes = [c.nome for c in urna.candidatos] if urna else ["Dollynho", "Barriguinha mole", "Naruto"]
        self.cand_partidos = [c.cargo for c in urna.candidatos] if urna else ["PRESIDENTE"] * 3
        self.cand_votos = [c.votos for c in urna.candidatos] if urna else [0, 0, 0]

        self.eleitor_titulos = [e["titulo"] for e in urna.eleitores] if urna else []
        self.eleitor_nomes = [e["nome"] for e in urna.eleitores] if urna else []
        self.eleitor_votou = [e["voto_computado"] for e in urna.eleitores] if urna else []

        self.votos_brancos = urna.votos_brancos if urna else 0
        self.votos_nulos = urna.votos_nulos if urna else 0

        self.configurar_interface()
        self.carregar_estilo()

    def _label(self, texto, object_name="texto_informacao", alinhamento=Qt.AlignmentFlag.AlignLeft):
        label = QLabel(texto)
        label.setObjectName(object_name)
        label.setAlignment(alinhamento)
        return label

    def _caixa(self):
        caixa = QWidget()
        caixa.setObjectName("caixa_informacoes")
        return caixa

    def configurar_interface(self):
        layout_principal = QVBoxLayout(self)
        layout_principal.setContentsMargins(0, 0, 0, 0)
        layout_principal.setSpacing(0)

        painel_central = QWidget()
        painel_central.setObjectName("painel_central")

        layout_painel = QVBoxLayout(painel_central)
        layout_painel.setContentsMargins(80, 40, 80, 40)
        layout_painel.setSpacing(0)

        layout_topo_painel = QHBoxLayout()
        layout_topo_painel.setSpacing(35)

        icone = QLabel()
        icone.setObjectName("quadrado_icone")
        caminho_imagem = BASE_DIR / "imagens" / "voting-box.png"
        if not caminho_imagem.exists():
            caminho_imagem = BASE_DIR.parent / "imagens" / "voting-box.png"

        if caminho_imagem.exists():
            icone.setPixmap(
                QPixmap(str(caminho_imagem)).scaled(
                    100, 100,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation,
                )
            )

        layout_topo_painel.addWidget(icone)

        layout_titulos = QVBoxLayout()
        layout_titulos.setSpacing(6)
        layout_titulos.addWidget(self._label(self.titulo_relatorio, "titulo_zerezima"))
        layout_titulos.addWidget(self._label(self.subtitulo_relatorio, "subtitulo_zerezima"))
        layout_topo_painel.addLayout(layout_titulos)

        layout_topo_painel.addStretch()

        agora = datetime.now().strftime("%d/%m/%Y  %H:%M:%S")
        label_data = self._label(
            f"Emitido em: {agora}", 
            "data_emissao", 
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop
        )
        layout_topo_painel.addWidget(label_data)

        layout_painel.addLayout(layout_topo_painel)
        layout_painel.addSpacing(30)

        layout_corpo = QHBoxLayout()
        layout_corpo.setSpacing(30)

        caixa_cand = self._caixa()
        layout_cand = QVBoxLayout(caixa_cand)
        layout_cand.setContentsMargins(40, 30, 40, 30)
        layout_cand.setSpacing(14)

        layout_cand.addWidget(self._label("Candidatos", "titulo_caixa"))

        for i in range(len(self.cand_nomes)):
            texto = (
                f"{self.cand_numeros[i]} - {self.cand_nomes[i]} "
                f"({self.cand_partidos[i]}) ... {self.cand_votos[i]} votos"
            )
            layout_cand.addWidget(self._label(texto, "texto_informacao"))

        layout_cand.addSpacing(10)
        layout_cand.addWidget(self._label(f"Votos em branco ... {self.votos_brancos}", "texto_informacao"))
        layout_cand.addWidget(self._label(f"Votos nulos ... {self.votos_nulos}", "texto_informacao"))
        layout_cand.addStretch()

        caixa_eleit = self._caixa()
        layout_eleit = QVBoxLayout(caixa_eleit)
        layout_eleit.setContentsMargins(40, 30, 40, 30)
        layout_eleit.setSpacing(14)

        layout_eleit.addWidget(self._label("Eleitores aptos", "titulo_caixa"))

        area_scroll = QScrollArea()
        area_scroll.setObjectName("area_scroll_eleitores")
        area_scroll.setWidgetResizable(True)
        area_scroll.setFrameShape(QFrame.Shape.NoFrame)

        conteudo_scroll = QWidget()
        conteudo_scroll.setObjectName("conteudo_scroll")
        layout_lista = QVBoxLayout(conteudo_scroll)
        layout_lista.setContentsMargins(0, 0, 0, 0)
        layout_lista.setSpacing(10)

        for i in range(len(self.eleitor_nomes)):
            situacao = "Já votou" if self.eleitor_votou[i] else "Não votou"
            obj_status = "status_votou" if self.eleitor_votou[i] else "status_nao_votou"
            texto = f"Título {self.eleitor_titulos[i]} - {self.eleitor_nomes[i]}"
            
            linha = QHBoxLayout()
            linha.addWidget(self._label(texto, "texto_eleitor"))
            linha.addStretch()
            linha.addWidget(self._label(situacao, obj_status))
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
        botao_voltar.clicked.connect(self.close)
        layout_botoes.addWidget(botao_voltar)

        layout_painel.addSpacing(20)
        layout_painel.addLayout(layout_botoes)

        layout_principal.addWidget(painel_central)

    def carregar_estilo(self):
        caminho_estilo = BASE_DIR / "estilo" / "estilo_zeresima.qss"
        if not caminho_estilo.exists():
            caminho_estilo = BASE_DIR.parent / "estilo" / "estilo_zeresima.qss"

        if caminho_estilo.exists():
            with open(caminho_estilo, "r", encoding="utf-8") as arquivo:
                self.setStyleSheet(arquivo.read())

if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    janela = TelaZerezima()
    janela.show()
    sys.exit(app.exec())