import mysql.connector
import temporada
import partida
import player


def criar_ranque(idDiscord, mydb):
    cursor = mydb.cursor()
    idPlayer = player.get_player(idDiscord)
    idTemp = temporada.get_temporada_ativa()
    sql = "INSERT INTO `gensou`.`ranque` (`Temporada_idTemporada`, `Player_idPlayer`) VALUES (%s, %s)"
    val = (idTemp, idPlayer)
    cursor.execute(sql, val)
    mydb.commit()


def get_ranque(IdPlayer, idTemp, mydb):
    cursor = mydb.cursor()
    sql = "SELECT * FROM `gensou`.`ranque` WHERE (`Player_idPlayer`= %s and `Temporada_idTemporada` = %s)"
    val = (IdPlayer, idTemp, )
    cursor.execute(sql, val)
    ranque = cursor.fetchone()

    if ranque == None:
        return -1
    else:
        return ranque
    

def GetRangeMultiplier(pontos):

    if pontos >= 4000:
        return 1.8
    elif pontos >= 3000:
        return 1.6
    elif pontos >= 2000:
        return 1.2
    elif pontos >= 1000:
        return 1.25
    else:
        return 1
    

