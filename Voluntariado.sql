-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Voluntariado
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Voluntariado
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Voluntariado` DEFAULT CHARACTER SET utf8 ;
USE `Voluntariado` ;

-- -----------------------------------------------------
-- Table `Voluntariado`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Voluntariado`.`usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(255) NULL,
  `apellido` VARCHAR(255) NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Voluntariado`.`misiones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Voluntariado`.`misiones` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(255) NULL,
  `fecha` DATE NULL,
  `voluntariados_necesarios` INT NULL,
  `descripcion` TEXT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `usuarios_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_misiones_usuarios_idx` (`usuarios_id` ASC) VISIBLE,
  CONSTRAINT `fk_misiones_usuarios`
    FOREIGN KEY (`usuarios_id`)
    REFERENCES `Voluntariado`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Voluntariado`.`usuarios_has_misiones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Voluntariado`.`usuarios_has_misiones` (
  `usuario_id` INT NOT NULL,
  `mision_id` INT NOT NULL,
  PRIMARY KEY (`usuario_id`, `mision_id`),
  INDEX `fk_usuarios_has_misiones_misiones1_idx` (`mision_id` ASC) VISIBLE,
  INDEX `fk_usuarios_has_misiones_usuarios1_idx` (`usuario_id` ASC) VISIBLE,
  CONSTRAINT `fk_usuarios_has_misiones_usuarios1`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `Voluntariado`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_usuarios_has_misiones_misiones1`
    FOREIGN KEY (`mision_id`)
    REFERENCES `Voluntariado`.`misiones` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
