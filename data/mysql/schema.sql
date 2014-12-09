CREATE DATABASE bigfootgenes_development;
GRANT ALL PRIVILEGES ON bigfootgenes_development.* TO 'bigfootgenes'@'localhost' IDENTIFIED BY 'dk34DFko99FDOQ' WITH GRANT OPTION;

use bigfootgenes_development;

CREATE TABLE snps(
  `rsid` VARCHAR(45) NOT NULL,
  `genotype` VARCHAR(2) NOT NULL,
  `summary` VARCHAR(255),
  PRIMARY KEY (`rsid`, `genotype`)
);

CREATE TABLE user_snps(
  `userid` VARCHAR(45) NOT NULL,
  `rsid` VARCHAR(45) NOT NULL,
  `genotype` VARCHAR(2) NOT NULL,
  `summary` VARCHAR(255),
  PRIMARY KEY (`userid`, `rsid`)
);

