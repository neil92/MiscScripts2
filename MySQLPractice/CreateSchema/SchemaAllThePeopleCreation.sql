/*
Author: Neil A. Patel
Date: 2017-05-30

This was a script that was created by the using the GUI of MySQL Workbench.
Apparently the GUI to create tables, schemas, and foreign keys is pretty easy to use"

*/


-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema AllThePeople
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema AllThePeople
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `AllThePeople` DEFAULT CHARACTER SET utf8 ;
USE `AllThePeople` ;

-- -----------------------------------------------------
-- Table `AllThePeople`.`person`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `AllThePeople`.`person` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `AllThePeople`.`tissue`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `AllThePeople`.`tissue` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `location` VARCHAR(45) NULL,
  `person_id` INT NULL,
  PRIMARY KEY (`id`),
  INDEX `person_id_fk_idx` (`person_id` ASC),
  CONSTRAINT `person_id_fk`
    FOREIGN KEY (`person_id`)
    REFERENCES `AllThePeople`.`person` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
