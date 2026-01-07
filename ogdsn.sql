select * from gensou.ranque;
select * from gensou.player WHERE idPlayer = 4;
select * from gensou.partida;
select * from gensou.temporada WHERE idTemporada = 9;

SELECT `RanquePoints`,`Temporada_idTemporada`,`Player_idPlayer` FROM `gensou`.`ranque` WHERE (`Temporada_idTemporada` = 9 and `Player_idPlayer`= 4)


