CREATE DATABASE bigfootgenes_development;

CREATE TABLE snps(
  `rsid` VARCHAR(45) NOT NULL,
  `genotype` VARCHAR(2) NOT NULL,
  `summary` VARCHAR(255),
  PRIMARY KEY (`rsid`, `genotype`)
);

GRANT ALL PRIVILEGES ON bigfootgenes_development.* TO 'bigfootgenes'@'localhost' IDENTIFIED BY 'dk34DFko99FDOQ' WITH GRANT OPTION;

