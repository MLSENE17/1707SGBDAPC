-- MySQL dump 10.13  Distrib 8.0.23, for Linux (x86_64)
--
-- Host: localhost    Database: covidModeler
-- ------------------------------------------------------
-- Server version	8.0.23-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cas_localite`
--

DROP TABLE IF EXISTS `cas_localite`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cas_localite` (
  `id` int NOT NULL AUTO_INCREMENT,
  `depart_id` int NOT NULL,
  `commune_id` int DEFAULT NULL,
  `nbre_cas` int NOT NULL,
  `date_communique` date NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `date_communique` (`date_communique`,`depart_id`,`commune_id`),
  KEY `fk_depart_id_communique` (`depart_id`),
  KEY `fk_commune_id_communique` (`commune_id`),
  CONSTRAINT `fk_commune_id_communique` FOREIGN KEY (`commune_id`) REFERENCES `commune` (`commune_id`),
  CONSTRAINT `fk_date_communique` FOREIGN KEY (`date_communique`) REFERENCES `communique` (`date_communique`),
  CONSTRAINT `fk_depart_id_communique` FOREIGN KEY (`depart_id`) REFERENCES `departement` (`depart_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cas_localite`
--

LOCK TABLES `cas_localite` WRITE;
/*!40000 ALTER TABLE `cas_localite` DISABLE KEYS */;
/*!40000 ALTER TABLE `cas_localite` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `commune`
--

DROP TABLE IF EXISTS `commune`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `commune` (
  `commune_id` int NOT NULL,
  `nom_localite` varchar(70) NOT NULL,
  `depart_id` int NOT NULL,
  PRIMARY KEY (`commune_id`),
  KEY `fk_depart_id` (`depart_id`),
  CONSTRAINT `fk_depart_id` FOREIGN KEY (`depart_id`) REFERENCES `departement` (`depart_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `commune`
--

LOCK TABLES `commune` WRITE;
/*!40000 ALTER TABLE `commune` DISABLE KEYS */;
/*!40000 ALTER TABLE `commune` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `communique`
--

DROP TABLE IF EXISTS `communique`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `communique` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nbre_test` int NOT NULL,
  `nbre_nouveaux_cas` int NOT NULL,
  `nbre_cas_contact` int DEFAULT NULL,
  `nbre_cas_communautaires` int DEFAULT NULL,
  `nbre_gueris` int DEFAULT NULL,
  `nbre_deces` int DEFAULT NULL,
  `nbre_cas_importes` int DEFAULT NULL,
  `nbre_cas_graves` int DEFAULT NULL,
  `nom_fichier_source` varchar(70) NOT NULL,
  `date_heure_extraction` datetime NOT NULL,
  `date_communique` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `date_communique` (`date_communique`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `communique`
--

LOCK TABLES `communique` WRITE;
/*!40000 ALTER TABLE `communique` DISABLE KEYS */;
/*!40000 ALTER TABLE `communique` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `departement`
--

DROP TABLE IF EXISTS `departement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `departement` (
  `depart_id` int NOT NULL,
  `nom_localite` varchar(70) NOT NULL,
  `region_id` int NOT NULL,
  PRIMARY KEY (`depart_id`),
  KEY `fk_region_id` (`region_id`),
  CONSTRAINT `fk_region_id` FOREIGN KEY (`region_id`) REFERENCES `region` (`region_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `departement`
--

LOCK TABLES `departement` WRITE;
/*!40000 ALTER TABLE `departement` DISABLE KEYS */;
INSERT INTO `departement` VALUES (1,'dakar',1),(2,'pikine',1),(3,'rufisque',1),(4,'guediawaye',1),(5,'bambeye',2),(6,'diourbel',2),(7,'mbacke',2),(8,'fatick',3),(9,'gossas',3),(10,'foundiougne',3),(11,'birkelane',4),(12,'kaffrine',4),(13,'koungheul',4),(14,'malem-hodar',4),(15,'kaolack',5),(16,'kaffrine',5),(17,'nioro du rip',5),(18,'kedougou',6),(19,'salemata',6),(20,'saraya',6),(21,'kolda',7),(22,'medina yoro foulah',7),(23,'velingara',7),(24,'louga',8),(25,'linguere',8),(26,'kebemer',8),(27,'matam',9),(28,'kanel',9),(29,'ranerou-ferlo',9),(30,'dagana',10),(31,'podor',10),(32,'saint-louis',10),(33,'bounkiling',11),(34,'goudomp',11),(35,'sedhiou',11),(36,'bakel',12),(37,'goudiry',12),(38,'koumpentoum',12),(39,'tambacounda',12),(40,'mbour',13),(41,'thies',13),(42,'tivaoune',13),(43,'bignona',14),(44,'oussouye',14),(45,'ziguinchor',14),(46,'guinguineo',5);
/*!40000 ALTER TABLE `departement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `region`
--

DROP TABLE IF EXISTS `region`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `region` (
  `region_id` int NOT NULL AUTO_INCREMENT,
  `nom_localite` varchar(70) NOT NULL,
  PRIMARY KEY (`region_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `region`
--

LOCK TABLES `region` WRITE;
/*!40000 ALTER TABLE `region` DISABLE KEYS */;
INSERT INTO `region` VALUES (1,'dakar'),(2,'diourbel'),(3,'fatick'),(4,'kaffrine'),(5,'kaolack'),(6,'kedougou'),(7,'kolda'),(8,'louga'),(9,'matam'),(10,'saint-louis'),(11,'sedhiou'),(12,'tambacounda'),(13,'thies'),(14,'ziguinchor');
/*!40000 ALTER TABLE `region` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `user_id` int NOT NULL,
  `username` varchar(70) NOT NULL,
  `password` varchar(70) NOT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-02  6:13:03
