import player
import temporada
import ranque
import partida
import mysql.connector
#id player com ranque = 2 e 7
mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="(senha)",
      database="gensou"
    )

def comando_criarPlayer(IdDiscord, nome, mydb):
    #checa se está registrado, se não, se sim, cancela
    IdPlayer = player.get_playerID(IdDiscord, mydb)
    if IdPlayer == -1:
        player.criar_player(IdDiscord,nome,mydb)
        print("Player ", nome,  " criado")
    else:
        print("IDDISCORD ", IdDiscord, " JÁ ESTÁ SENDO USADO!")

def comando_criarRanque(IdDiscord, mydb):
    TempAtivaID = temporada.get_temporada_ativa(mydb)
    if TempAtivaID == -1:
      retorno = "Sem temporada ativa"
      return retorno
    
    Player = player.get_player(IdDiscord,mydb)
    IdPlayer = Player[0]
    if IdPlayer == -1:
        retorno = "Player " + IdPlayer + " não está no sistema"
        return retorno
    
    print("Temporada: ", TempAtivaID, "|| Player: ", IdPlayer)

    ranquecheck = ranque.get_ranque(IdPlayer,TempAtivaID,mydb)
    if ranquecheck != -1:
        print(ranquecheck)
        return "Player já está na temporada"
    
    #ranque.criar_ranque(IdDiscord, mydb)


def comando_desafio(IdDiscordDesafiante, IdDiscordDesafiado, mydb):
    #checks:
    #Temporada ativa?
    #Jogadores no Sistema?
    #Jogadores Em Partida?
    #Jogadores Tem Ranque?


    print("desafio!!!")
    TempAtivaID = temporada.get_temporada_ativa(mydb)
    if TempAtivaID == -1:
      retorno = "Sem temporada ativa"
      return retorno
    
    Desafiante = player.get_player(IdDiscordDesafiante, mydb)
    IdDesafiante = Desafiante[0]
    if IdDesafiante == -1:
        retorno = "Player " + str(IdDiscordDesafiante) + " não está no sistema"
        return retorno
    
    Desafiado = player.get_player(IdDiscordDesafiado, mydb)
    IdDesafiado = Desafiado[0]
    if IdDesafiado == -1:
        retorno = "Player " + str(IdDiscordDesafiado) + " não está no sistema"
        return retorno
    
    if Desafiante[6] == 0:
      retorno = "Player " + Desafiante[2] + " está inativo"
      return retorno
    if Desafiado[6] == 0:
      retorno = "Player " + Desafiado[2] + " está inativo"
      return retorno   

    if Desafiante[7] == 1:
      retorno = "Player " + Desafiante[2] + " está em partida"
      return retorno
    if Desafiado[7] == 1:
      retorno = "Player " + Desafiado[2] + " está em partida"
      return retorno    
    
    RanqueDesafiante = ranque.get_ranque(IdDesafiante, TempAtivaID, mydb)
    if RanqueDesafiante == -1:
      retorno = "Player " + Desafiante[2] + " não está na temporada"
      return retorno
      
    RanqueDesafiado = ranque.get_ranque(IdDesafiado,TempAtivaID, mydb)
    if RanqueDesafiado == -1:
      retorno = "Player " + str(IdDiscordDesafiado) + " não está na temporada"
      return retorno
    
    print("ID Desafiado: ", IdDesafiado, "ID Desafiante: ", IdDesafiante)
    return "CHEGOU NO FINAL!?"

print(comando_desafio(3, 7, mydb))
#temporada.desativar_temporada(mydb)


#playerAti = player.get_playerID(2, mydb)
#playerID = playerAti
#temporada.desativar_temporada(mydb)
#tempAti = temporada.get_temporada_ativa(mydb)
#ranqueAti = ranque.get_ranque(playerID, tempAti, mydb)

#print("Dados Player:" , playerAti)
#print("Temporada Ativa: ",tempAti)
#print("Dados Ranque Player: ",ranqueAti)

#PartidaAti = partida.achar_partida_ativa(playerID, mydb)

#print("Dados Partida ", PartidaAti)

