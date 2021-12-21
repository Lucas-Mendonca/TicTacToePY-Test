# Função para indicar algum vencedor
def vitoria(player):
    print("vitoria do jogador ("+player+")!!!!!")
def winC(playerI,v1,v2,v3,v4,v5,v6,v7,v8,v9):
    if (v1 == v2 != " " and v2 == v3 != " ") or (v4 == v5 != " " and v5 == v6 != " ") or (v7 == v8 != " " and v8 == v9 != " "):
        vitoria(playerI)
        return True
    if (v1 == v4 != " " and v4 == v7 != " ") or (v2 == v5 != " " and v5 == v8 != " ") or (v3 == v6 != " " and v6 == v9 != " "):
        vitoria(playerI)
        return True
    if (v1 == v5 != " " and v5 == v9 != " ") or (v7 == v5 != " " and v5 == v3 != " "):
        vitoria(playerI)
        return True