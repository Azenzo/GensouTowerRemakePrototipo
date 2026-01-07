SELECT Nome, RanquePoints, Cristais, Partidas, Vitórias, Player.Status, Nome from gensou.Player, gensou.ranque where Player_idPlayer = player.idPlayer


;
INSERT INTO `gensou`.`player` (`idDiscord`, `Nome`) VALUES (1234,"ETHARN");
UPDATE `gensou`.`player` SET 
`Cristais` = <{Cristais: 0}>,
`Partidas` = <{Partidas: 0}>, `Vitórias` = <{Vitórias: 0}>,
`Status` = <{Status: b'1'}>, `EmPartida` = <{EmPartida: b'0'}>
WHERE `idPlayer` = <{expr}>;


