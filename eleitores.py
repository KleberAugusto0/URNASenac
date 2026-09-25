# class Eleitor():
#     def __init__(self , nome , titulo_eleitor, situacao_voto):

#         self.nome = nome
#         self.titulo_eleitor = titulo_eleitor
#         self.situacao_voto = situacao_voto

#         self.situacao_voto = False



# eleitor1 = Eleitor("Mateus" , "001")


# eleitor1.registrar_voto()


# print(f"{eleitor1} já votou? {eleitor1.situacao_voto}")



#Fazer um vetor para os eleitores.


eleitores = [
    {"nome" : "Mateus" , "titulo": "001" ,"situacao_voto": False}, 
    {"nome" : "Kleber" , "titulo": "002" ,"situacao_voto": False}, 
    {"nome" : "Lucas"  , "titulo": "003" ,"situacao_voto": False}, 
    {"nome" : "Alanys" , "titulo": "004" ,"situacao_voto": False}, 
]

# for e in eleitores:
#     print(e)

def registrar_voto(self):
      self.situacao_voto = True

eleitores[0] = registrar_voto()
for e in eleitores:
     print(e)
nao_votaram = [ e for e in eleitores if not e["situacao_voto"]]
# print(nao_votaram , sep="\n")

for n in nao_votaram:
    print(n)

    