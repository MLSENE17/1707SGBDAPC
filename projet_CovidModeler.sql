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
  CONSTRAINT `cas_localite_ibfk_1` FOREIGN KEY (`commune_id`) REFERENCES `commune` (`commune_id`),
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
  `commune_id` int NOT NULL AUTO_INCREMENT,
  `nom_localite` varchar(70) NOT NULL,
  `depart_id` int NOT NULL,
  PRIMARY KEY (`commune_id`),
  KEY `fk_depart_id` (`depart_id`),
  CONSTRAINT `fk_depart_id` FOREIGN KEY (`depart_id`) REFERENCES `departement` (`depart_id`)
) ENGINE=InnoDB AUTO_INCREMENT=177 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `commune`
--

LOCK TABLES `commune` WRITE;
/*!40000 ALTER TABLE `commune` DISABLE KEYS */;
INSERT INTO `commune` VALUES (4,'Kiniéba',36),(5,'Moudéri',36),(6,'Bellé',36),(7,'lambaye',5),(8,'ngoye',5),(9,'baba garage',5),(10,'kataba1',43),(11,'tangori',43),(12,'tendouk',43),(13,'sindian',43),(14,'mabo',11),(15,'keur mboucki',11),(16,'bona',33),(17,'bogal',33),(18,'diaroume',33),(19,'ndiaye',30),(20,'mbane',30),(21,'ndoulo',6),(22,'ndindy',6),(23,'diakhao',8),(24,'fimla',8),(25,'tataguine',8),(26,'niakhar',8),(27,'djilor',10),(28,'toubacouta',10),(29,'niodior',10),(30,'ouadiour',9),(31,'dianke mankan',37),(32,'koulor',37),(33,'bala',37),(34,'bouinguel bamba',37),(35,'simbandi brassou',34),(36,'djibanar',34),(37,'karantaba',34),(38,'mbadakhoune',46),(39,'nguelou',46),(40,'gniby',16),(41,'katakel',16),(42,'sinthiou',28),(43,'orkadiere',28),(44,'sibassor/ngothie',15),(45,'koumbal',15),(46,'ndiedieng',15),(47,'ndande',26),(48,'sagatta gueth',26),(49,'bandafassi',18),(50,'fongolemi',18),(51,'mampatim',21),(52,'sare bidji',21),(53,'dioulakolon',21),(54,'koutiaba wolof',38),(55,'bamba tialene',38),(56,'missira wadene',13),(57,'ida mouride',13),(58,'lour escale',13),(59,'yang yang ',25),(60,'sagata wolof',25),(61,'barkedji',25),(62,'dodji',25),(63,'koki',24),(64,'mbediene',24),(65,'sakal',24),(66,'darou minam 2',14),(67,'sagna',14),(68,'ogo',27),(69,'agname civol',27),(70,'ndame',7),(71,'taif',7),(72,'kael',7),(73,'fissel',40),(74,'sessene',40),(75,'sindia',40),(76,'ndoma',22),(77,'nianing',22),(78,'fafacourou',22),(79,'paoscoto',17),(80,'wak ngouna',17),(81,'medina sabakh',17),(82,'loudi wolof',44),(83,'cabrousse',44),(84,'niayes',2),(85,'thiaroye',2),(86,'pikine dagoudane',2),(87,'gamadji sarre',31),(88,'thille boubacar',31),(89,'salde',31),(90,'cas-cas',31),(91,'rao',32),(92,'dar salam',19),(93,'daketeli',19),(94,'sabadola',20),(95,'bembou',20),(96,'diende',35),(97,'djibabouya',35),(98,'djiredji',35),(99,'missira',39),(100,'makacoulibantang',39),(101,'koussanar',39),(102,'keur moussa',41),(103,'thienaba',41),(104,'noto',41),(105,'niakhene',42),(106,'pambal',42),(107,'meouane',42),(108,'merina dakhar',42),(109,'bonconto',23),(110,'pakour',23),(111,'sare coly sarre',23),(112,'niaguis',45),(113,'niassia',45),(114,'YEUMBEUL',2),(115,'PATTE D\'OIE',1),(116,'TOUBA',7),(117,'MEDINA',1),(118,'KEUR MASSAR',2),(119,'DIEUPPEUL DERKLE',1),(120,'GRAND DAKAR',1),(121,'POUT',41),(122,'GUEULE-TAPEE_FASS_COLOBANE',1),(123,'MBAO',2),(124,'PARCELLES ASSAINIES',1),(125,'PLATEAU',1),(126,'SANGALKAM',3),(127,'HANN BEL AIR',1),(128,'YOFF',1),(129,'DIAMNIADIO',3),(130,'GRAND YOFF',1),(131,'SICAP LIBERTE',1),(132,'FANN_POINT-E_AMITIE',1),(133,'MERMOZ_SACRE-COEUR',1),(134,'OUAKAM',1),(135,'DALIFORD',2),(136,'CAMBERENE',1),(137,'HLM',1),(138,'NGOR',1),(139,'DIAMAGUENE_SICAP-MBAO',2),(140,'THIADIAYE',40),(141,'GOLF SUD',4),(142,'MALIKA',2),(143,'BARGNY',3),(144,'THIAROYE SUR MER',2),(145,'RICHARD TOLL',30),(146,'MEKHE',42),(147,'SEBIKOTANE',3),(148,'DAROU MOUSTY',26),(149,'TIVAOUANE PEULH',3),(150,'SALY',40),(151,'DIASS',40),(152,'NGAPAROU',40),(153,'SINDIA',40),(154,'PIKINE SUD',2),(155,'PIKINE OUEST',2),(156,'RUFISQUE CENTRE',3),(157,'RUFISQUE OUEST',3),(158,'TIVAOUANE DIACKSAO',2),(159,'MEDINA GOUNASS',23),(160,'PIKINE EST',2),(161,'RUFISQUE EST',3),(162,'GOREE',1),(163,'KHOMBOLE',41);
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
INSERT INTO `departement` VALUES (1,'dakar',1),(2,'pikine',1),(3,'rufisque',1),(4,'guediawaye',1),(5,'bambeye',2),(6,'diourbel',2),(7,'mbacke',2),(8,'fatick',3),(9,'gossas',3),(10,'foundiougne',3),(11,'birkelane',4),(12,'kaffrine',4),(13,'koungheul',4),(14,'malem hodar',4),(15,'kaolack',5),(16,'kaffrine',5),(17,'nioro du rip',5),(18,'kedougou',6),(19,'salemata',6),(20,'saraya',6),(21,'kolda',7),(22,'medina yoro foulah',7),(23,'velingara',7),(24,'louga',8),(25,'linguere',8),(26,'kebemer',8),(27,'matam',9),(28,'kanel',9),(29,'ranerou ferlo',9),(30,'dagana',10),(31,'podor',10),(32,'saint-louis',10),(33,'bounkiling',11),(34,'goudomp',11),(35,'sedhiou',11),(36,'bakel',12),(37,'goudiry',12),(38,'koumpentoum',12),(39,'tambacounda',12),(40,'mbour',13),(41,'thies',13),(42,'tivaouane',13),(43,'bignona',14),(44,'oussouye',14),(45,'ziguinchor',14),(46,'guinguineo',5);
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

-- Dump completed on 2021-05-02 19:06:15
