eleitores = [
    {"nome" : "Mateus" , "titulo": "001" ,"situacao_voto": False}, 
    {"nome" : "Kleber" , "titulo": "002" ,"situacao_voto": False}, 
    {"nome" : "Lucas"  , "titulo": "003" ,"situacao_voto": False}, 
    {"nome" : "Alanys" , "titulo": "004" ,"situacao_voto": False}, 
]

# for e in eleitores:
#      print(e)

nao_votaram = [ e for e in eleitores if not e["situacao_voto"]]

for n in nao_votaram:
    print(n)

    