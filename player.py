import mysql.connector
import temporada
import partida


#cria perfil
def criar_player(idDiscord, Nome, mydb):
    cursor = mydb.cursor()
    sql = "INSERT INTO gensou.player (`idDiscord`,`Nome`)VALUES(%s,%s)"
    val = (idDiscord, Nome)
    cursor.execute(sql, val)
    mydb.commit()

#desativar player
def inativar_player(idDiscord, mydb):
    cursor = mydb.cursor()
    sql = "UPDATE `gensou`.`player` SET `Status` = 0 WHERE (`idDiscord` = %s);"
    val = (idDiscord, )
    cursor.execute(sql, val)
    mydb.commit()    
    print("inativando", idDiscord)

#ativar player
def ativar_player(idDiscord, mydb):
    cursor = mydb.cursor()
    sql = "UPDATE `gensou`.`player` SET `Status` = 1 WHERE (`idDiscord` = %s);"
    val = (idDiscord, )
    cursor.execute(sql, val)
    mydb.commit()    

#deleta player
def deletar_player(idDiscord, mydb):
    cursor = mydb.cursor()
    sql = "DELETE FROM `gensou`.`player` WHERE idDiscord = (%s);"
    val = (idDiscord, )
    cursor.execute(sql, val)
    mydb.commit()    

#Get dados player completo
def get_player(idDiscord, mydb):
    cursor = mydb.cursor()
    sql = "SELECT *  FROM gensou.player WHERE idDiscord = (%s)"
    val = (idDiscord, )
    cursor.execute(sql, val)
    idPlayerAtual = cursor.fetchone()

    if idPlayerAtual == None:
        return -1
    else:
        return idPlayerAtual
