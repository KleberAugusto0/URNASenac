from .candidatos import Candidato, candidatos_cadastrados, buscar_candidato
from .eleitores import TituloEleitorBackEnd


class Urna:
    def __init__(self):
        self.zeresima_emitida = False
        self.urna_encerrada = False
        self.votos_brancos = 0
        self.votos_nulos = 0
        self.eleitores_backend = TituloEleitorBackEnd()
        self.eleitores_backend.zeresima_emitida = False
        self.candidatos = candidatos_cadastrados

    @property
    def eleitores(self):
        return self.eleitores_backend.eleitores

    def emitir_zeresima(self) -> bool:
        if self.urna_encerrada:
            return False

        self.zeresima_emitida = True
        self.eleitores_backend.zeresima_emitida = True
        return True

    def encerrar_urna(self) -> None:
        self.urna_encerrada = True
        self.eleitores_backend.urna_encerrada = True

    def validar_eleitor(self, titulo: str) -> tuple[bool, str]:
        self.eleitores_backend.zeresima_emitida = self.zeresima_emitida
        self.eleitores_backend.urna_encerrada = self.urna_encerrada
        return self.eleitores_backend.validar_eleitor(titulo)

    def buscar_candidato(self, numero: str) -> Candidato | None:
        return buscar_candidato(self.candidatos, "PRESIDENTE", numero)

    def registrar_voto_candidato(self, titulo: str, candidato: Candidato) -> None:
        candidato.votos += 1
        self.eleitores_backend.marcar_voto(titulo)

    def registrar_voto_nulo(self, titulo: str) -> None:
        self.votos_nulos += 1
        self.eleitores_backend.marcar_voto(titulo)

    def registrar_voto_branco(self, titulo: str) -> None:
        self.votos_brancos += 1
        self.eleitores_backend.marcar_voto(titulo)