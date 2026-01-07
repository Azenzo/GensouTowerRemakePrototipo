CREATE TABLE IF NOT EXISTS `Gensou`.`Player` (
  `idPlayer` INT NOT NULL AUTO_INCREMENT,
  `idDiscord` INT NULL,
  `Nome` VARCHAR(45) NULL,
  `Cristais` INT NULL DEFAULT 0,
  `Partidas` INT NULL DEFAULT 0,
  `Vitórias` INT NULL DEFAULT 0,
  `Status` BIT NULL DEFAULT 1,
  `EmPartida` BIT NULL DEFAULT 0,
  PRIMARY KEY (`idPlayer`),
  UNIQUE INDEX `idPlayer_UNIQUE` (`idPlayer` ASC) VISIBLE)
ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS `Gensou`.`Temporada` (
  `idTemporada` INT NOT NULL,
  `Ativa` BIT NULL DEFAULT 1,
  `Nome` VARCHAR(45) NULL,
  `Player_idCelestial` INT NOT NULL,
  PRIMARY KEY (`idTemporada`, `Player_idCelestial`),
  INDEX `fk_Temporada_Player1_idx` (`Player_idCelestial` ASC) VISIBLE,
  CONSTRAINT `fk_Temporada_Player1`
    FOREIGN KEY (`Player_idCelestial`)
    REFERENCES `Gensou`.`Player` (`idPlayer`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS `Gensou`.`Ranque` (
  `Temporada_idTemporada` INT NOT NULL,
  `Player_idPlayer` INT NOT NULL,
  `Celestial` BIT NULL,
  `RanquePoints` BIT NULL DEFAULT 0,
  `VidasCel` INT NULL DEFAULT 5,
  PRIMARY KEY (`Temporada_idTemporada`, `Player_idPlayer`),
  INDEX `fk_Temporada_has_Player_Player1_idx` (`Player_idPlayer` ASC) VISIBLE,
  INDEX `fk_Temporada_has_Player_Temporada1_idx` (`Temporada_idTemporada` ASC) VISIBLE,
  CONSTRAINT `fk_Temporada_has_Player_Temporada1`
    FOREIGN KEY (`Temporada_idTemporada`)
    REFERENCES `Gensou`.`Temporada` (`idTemporada`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Temporada_has_Player_Player1`
    FOREIGN KEY (`Player_idPlayer`)
    REFERENCES `Gensou`.`Player` (`idPlayer`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS `Gensou`.`Partida` (
  `idPartida` INT NOT NULL,
  `Temporada_idTemporada` INT NOT NULL,
  `Player_idDesafiante` INT NOT NULL,
  `Player_idDesafiado` INT NOT NULL,
  `PontosDesafiante` INT ZEROFILL NULL,
  `PontosDesafiado` INT ZEROFILL NULL,
  `RanqueDesafiante` INT NULL,
  `RanqueDesafiado` INT NULL,
  `VariaçãoRanqueDesafiante` TINYINT ZEROFILL NULL,
  `VariaçãoRanqueDesafiado` TINYINT ZEROFILL NULL,
  `DataCriada` TIMESTAMP NULL,
  `DataExpirada` TIMESTAMP NULL,
  `DataFinalizada` TIMESTAMP NULL,
  `Status` BIT NULL,
  PRIMARY KEY (`idPartida`, `Temporada_idTemporada`, `Player_idDesafiante`, `Player_idDesafiado`),
  INDEX `fk_Partida_Player_idx` (`Player_idDesafiante` ASC) VISIBLE,
  INDEX `fk_Partida_Player1_idx` (`Player_idDesafiado` ASC) VISIBLE,
  INDEX `fk_Partida_Temporada1_idx` (`Temporada_idTemporada` ASC) VISIBLE,
  CONSTRAINT `fk_Partida_Player`
    FOREIGN KEY (`Player_idDesafiante`)
    REFERENCES `Gensou`.`Player` (`idPlayer`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Partida_Player1`
    FOREIGN KEY (`Player_idDesafiado`)
    REFERENCES `Gensou`.`Player` (`idPlayer`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Partida_Temporada1`
    FOREIGN KEY (`Temporada_idTemporada`)
    REFERENCES `Gensou`.`Temporada` (`idTemporada`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB