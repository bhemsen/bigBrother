CREATE USER 'webadmin'@'%' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'webadmin'@'%';

CREATE DATABASE sensoro;
USE sensoro;

CREATE TABLE `temperature` (
  `ID` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `day` date NOT NULL,
  `time` time NOT NULL,
  `temperature` float,
  `humidity` float
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `sensoro`.`securitylevel` ( 
  `ID` INT NOT NULL ,
  `name` VARCHAR(16) NOT NULL , 
  PRIMARY KEY (`ID`)) ENGINE = InnoDB;

INSERT INTO `securitylevel` (`ID`, `name`) 
VALUES ('1', 'Employee'), ('2', 'Boss');


CREATE TABLE `sensoro`.`rfid` ( 
  `ID` INT NOT NULL AUTO_INCREMENT ,
  `name` VARCHAR(32) NOT NULL , 
  `securityLevel` INT NOT NULL , 
  `rfid` JSON NOT NULL , 
  PRIMARY KEY (`ID`)) ENGINE = InnoDB;

ALTER TABLE `rfid` ADD FOREIGN KEY (`securityLevel`) 
REFERENCES `securitylevel`(`ID`) 
ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE `rfid` ADD UNIQUE( `rfid`);

CREATE TABLE `sensoro`.`entrylog` ( 
  `ID` INT NOT NULL AUTO_INCREMENT , 
  `time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP , 
  `name` VARCHAR(32) NOT NULL, 
  `rfid` VARCHAR(255) NOT NULL , 
  `access` VARCHAR(32) NOT NULL , 
  PRIMARY KEY (`ID`)) ENGINE = InnoDB;