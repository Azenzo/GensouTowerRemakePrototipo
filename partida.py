import mysql.connector
import player
import temporada
import ranque
from datetime import time, timedelta, date



def criar_desafio(idDiscDesafiante, idDiscDesafiado, mydb):
    cursor = mydb.cursor()
    idTempAtual = temporada.get_temporada_ativa()
    print("Temporada Atual: ", idTempAtual)

    idDesafiado = player.get_playerID(idDiscDesafiado)
    print(idDesafiado)
    RanqueDesafiado = ranque.get_Pontosranque(idDesafiado,idTempAtual)

    print("IdPlayer", idDesafiado,  "Pontos", RanqueDesafiado)

    idDesafiante = player.get_playerID(idDiscDesafiante)
    RanqueDesafiante = ranque.get_Pontosranque(idDesafiante,idTempAtual)
    print("IdPlayer", idDesafiante,"Pontos",RanqueDesafiante)

    data_agora = date.today()
    data_1semana = data_agora + timedelta(days = 3)
    print( data_agora, data_1semana)
    sql = "INSERT INTO `gensou`.`partida` (`Temporada_idTemporada`, `Player_idDesafiante`,`Player_idDesafiado`,`RanqueDesafiante`,`RanqueDesafiado`,`DataCriada`,`DataExpirada`,`Status`)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (idTempAtual,  idDesafiante, idDesafiado, RanqueDesafiante, RanqueDesafiado, data_agora, data_1semana, 0)

    cursor.execute(sql, val)
    mydb.commit()    

    print("foda")


def aceitar_desafio():
    #ou começar partida
    print("aceito miseravi")


def recusar_desafio():
    print("rejeitou miseravi")

def cancelar_desafio():
    print("Cancelado!!!")


def timeout_desafio():
    print("Timeout!!")


def Reportar_partida(idDiscord, pontosDesafiante, pontosDesafiado, mydb):
    cursor = mydb.cursor()
    partida = achar_partida_ativa(idDiscord)
    idPartida = partida[0]
    print(partida)
    idDesafiante = partida[2]
    idDesafiado = partida[3]
    RanqueDesafiante = partida[6]
    RanqueDesafiado = partida[7]
    data_finalizada  = date.today()
    multDesafiante = ranque.GetRangeMultiplier(RanqueDesafiante)
    multDesafiado = ranque.GetRangeMultiplier(RanqueDesafiado)

    print(data_finalizada)
    print("idDesafiante: " ,idDesafiante, "|| idDesafiado: ", idDesafiado)
    print("PontosDesafiante: " ,pontosDesafiante, "|| PontosDesafiado: ", pontosDesafiado)
    print("MultDesafiante: " ,multDesafiante, "|| MultDesafiado: ", multDesafiado)
    print("RanqueDesafi: " , RanqueDesafiante, "|| RanqueDesafiado: ", RanqueDesafiado)
    
    vitoria = "hehe"

    #Se Desafiante Ganhar
    if(pontosDesafiante == 5):
        varDesafiante = ((multDesafiante - multDesafiado) +1) * 60 + (10 * (pontosDesafiante - pontosDesafiado))
        varDesafiado  = (((multDesafiante - multDesafiado) * 2 + 1) * 60 + (10 * (pontosDesafiante - pontosDesafiado))) * -0.9
        print("VarDesafi: " , varDesafiante, "|| VarDesafiado: ", varDesafiado)
        vitoria = "DESAFIANTE ganhou"
        RanqueFinalDesafiado = RanqueDesafiado + varDesafiado
        RanqueFinalDesafiante = RanqueDesafiante + varDesafiante
        sql = "UPDATE `gensou`.`partida` SET `PontosDesafiante` = %s, `PontosDesafiado` = %s, `VariaçãoRanqueDesafiante` = %s,`VariaçãoRanqueDesafiado` = %s,`DataFinalizada` = %s, `Status` = %s , QmGanhou = 0 WHERE idPartida = %s"
   
    
    else:
        #Se Desafiante Perder
        varDesafiado = ((multDesafiado - multDesafiante) +1) * 60 + (10 * (pontosDesafiado - pontosDesafiante))
        varDesafiante = (((multDesafiado - multDesafiante) * 2 +1) * 60 + (10 * (pontosDesafiado - pontosDesafiante))) * -0.9
        print("VarDesafi: " , varDesafiante, "|| VarDesafiado: ", varDesafiado)
   
        RanqueFinalDesafiado = RanqueDesafiado + varDesafiado
        RanqueFinalDesafiante = RanqueDesafiante + varDesafiante 
        vitoria = "DESAFIADO ganhou"
        sql = "UPDATE `gensou`.`partida` SET `PontosDesafiante` = %s, `PontosDesafiado` = %s, `VariaçãoRanqueDesafiante` = %s,`VariaçãoRanqueDesafiado` = %s,`DataFinalizada` = %s, `Status` = %s , QmGanhou = 1 WHERE idPartida = %s"
   
    print("Quem ganhou? " + vitoria)
        

    val = (pontosDesafiante, pontosDesafiado,varDesafiante,varDesafiado,data_finalizada,0,idPartida)
    cursor.execute(sql,val)
    #atualizando Ranque
    #desafiante
    #sql = 

    mydb.commit()  


def achar_partida_ativa(idPlayer, mydb):
    cursor = mydb.cursor()
    sql = "SELECT * FROM `gensou`.`partida` WHERE partida.Status = 1 AND (partida.Player_idDesafiado = %s OR partida.Player_idDesafiante = %s)"
    val = (idPlayer, idPlayer, )
    cursor.execute(sql, val)
    partida = cursor.fetchall()

    if len(partida) == 0:
        print(idPlayer, "não tem partida ativa")
        return -1
    else:
        return partida


    return cursor.fetchall()[0]

def achar_partidas(idPlayer, mydb):
    cursor = mydb.cursor()
    sql = "SELECT * FROM `gensou`.`partida` WHERE (partida.Player_idDesafiado = %s OR partida.Player_idDesafiante = %s)"
    val = (idPlayer, idPlayer, )
    print(idPlayer)
    cursor.execute(sql, val)
    return cursor.fetchall()