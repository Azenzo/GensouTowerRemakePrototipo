import mysql.connector

def criar_temporada(nome, mydb):
    mycursor = mydb.cursor()
    print("teste")
    sql = "INSERT INTO gensou.temporada (`Nome`)VALUES(%s)"
    val = (nome,)
    mycursor.execute(sql, val)
    print("temporada criada")

def get_temporada_ativa(mydb):
    mycursor = mydb.cursor()
    sql = "SELECT idTemporada from gensou.temporada WHERE Ativa = 1"
    mycursor.execute(sql)
    temporadaAtual = mycursor.fetchone()

    if temporadaAtual == None:
        return -1
    else:
        return temporadaAtual[0]


def desativar_temporada(mydb):
    mycursor = mydb.cursor()
    tempId = get_temporada_ativa(mydb)
    sql = "UPDATE `gensou`.`temporada` SET`Ativa` = b'0' WHERE `idTemporada` = %s;"
    val = (tempId, )
    print("desativando temporada ", tempId)
    mycursor.execute(sql, val)

#temporada_ativa()
#mydb.commit()
