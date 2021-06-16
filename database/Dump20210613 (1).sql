-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: localhost    Database: chitra_gupta
-- ------------------------------------------------------
-- Server version	8.0.23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `all_donations`
--

DROP TABLE IF EXISTS `all_donations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `all_donations` (
  `id_donations` int NOT NULL AUTO_INCREMENT,
  `id_donor` int DEFAULT NULL,
  `date_of_donation` datetime DEFAULT NULL,
  `donation_date` datetime DEFAULT NULL,
  `donation_in_name` varchar(45) DEFAULT NULL,
  `master_registration_number` int DEFAULT NULL,
  `reciept_number` int DEFAULT NULL,
  `payment_mode` varchar(45) DEFAULT NULL,
  `payment_description` varchar(100) DEFAULT NULL,
  `Ocassion` varchar(45) DEFAULT NULL,
  `remarks` varchar(200) DEFAULT NULL,
  `category` int DEFAULT NULL,
  `id_student` int DEFAULT NULL,
  `amount` int DEFAULT NULL,
  `remind_date` date DEFAULT NULL,
  `reminded` int DEFAULT '0',
  `master_id` int DEFAULT NULL,
  `checked` int DEFAULT '0',
  `date_show` date DEFAULT NULL,
  PRIMARY KEY (`id_donations`),
  UNIQUE KEY `master_registration_number_UNIQUE` (`master_registration_number`),
  KEY `id_donor_idx` (`id_donor`),
  KEY `category_idx` (`category`),
  CONSTRAINT `category` FOREIGN KEY (`category`) REFERENCES `schemes` (`idschemes`),
  CONSTRAINT `id_donor` FOREIGN KEY (`id_donor`) REFERENCES `all_donors` (`donor_id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `all_donations`
--
-- ORDER BY:  `id_donations`

LOCK TABLES `all_donations` WRITE;
/*!40000 ALTER TABLE `all_donations` DISABLE KEYS */;
INSERT INTO `all_donations` VALUES (10,1,'2021-05-18 11:37:32','2021-05-18 00:00:00','sid',10,1,'Cash','cash paid','B.D','birthday',1,0,400,NULL,0,2,1,'2022-06-12'),(11,1,'2021-05-18 11:41:41','2021-05-18 00:00:00','tarun',2,2,'Cash','Description','B.D','Description & Remarks',1,0,300,'2022-05-13',0,2,1,'2022-06-11'),(12,1,'2021-05-18 19:02:01','2021-05-18 00:00:00','tarun',9,2,'Cash','Description','B.D','Description & Remarks',4,0,500,NULL,0,2,1,'2021-05-18'),(13,1,'2021-05-18 19:02:01','2021-05-18 00:00:00','vinay',1,2,'Cash','Description','B.D','Description & Remarks',7,0,1000,NULL,0,2,1,'2021-05-18'),(14,1,'2021-05-18 19:02:01','2021-05-18 00:00:00','sid',3,2,'Cash','Description','B.D','Description & Remarks',1,0,1500,NULL,0,2,1,'2021-05-18'),(15,1,'2021-05-18 19:02:01','2021-05-18 00:00:00','sid',4,2,'Cash','Description','B.D','Description & Remarks',2,0,1500,NULL,0,2,1,'2021-05-18'),(16,1,'2021-05-18 19:02:01','2021-05-18 00:00:00','kvs',5,2,'Cash','Description','B.D','Description & Remarks',7,0,1500,NULL,0,2,1,'2021-05-18'),(17,1,'2021-05-17 19:17:25','2021-05-18 00:00:00','kvs',6,5,'Cash','Description','B.D','Description & Remarks',1,0,500,NULL,0,2,1,NULL),(18,1,'2021-05-19 19:17:25','2021-05-18 00:00:00','kvs',7,5,'Cash','Description','B.D','Description & Remarks',1,0,500,NULL,0,2,1,NULL),(19,NULL,'2021-05-19 02:58:28','2021-05-19 00:00:00','subaramanyam',8,5,'Cash','cash paid','B.D','killer puttina roju',1,0,1000,NULL,0,2,1,NULL),(20,1,'2021-05-20 10:36:30','2021-05-20 00:00:00','Name',234,2443,'Cash','Description','S.D','Description & Remarks',5,0,500,NULL,0,2,1,NULL),(22,1,'2021-05-21 00:52:19','2020-05-21 00:00:00','subbu',35,436,'Cash','cash paid','B.D','birthday',1,0,1000,'2021-05-16',1,2,1,NULL),(23,1,'2021-06-12 19:40:31','2021-06-12 00:00:00','Anirudh',123,21,'Cash','cash paid','B.D','birthday',1,0,500,'2022-06-07',0,2,1,'2022-06-12'),(24,1,'2021-06-09 00:04:16','2021-06-09 00:00:00','subbu',23,35,'Cash','Description','B.D','Description & Remarks',1,0,100,'2022-06-04',0,2,1,NULL),(25,1,'2021-06-11 00:04:16','2021-06-11 00:00:00','subbu',24,37,'Cheque','Description','B.D','Description & Remarks',1,0,1000,'2022-06-04',0,2,1,NULL),(26,1,'2021-06-12 00:17:36','2021-06-12 00:00:00','T K subramanyam',4247,25,'Cash','cash paid','B.D','42nd birthday',1,0,1500,'2022-06-07',0,2,1,'2022-06-12'),(27,1,'2021-06-12 00:22:41','2021-06-12 00:00:00','vinay shankar',60,59,'Cash','cash paid','Others','secret donation',1,0,500,'2022-06-07',0,2,1,'2022-06-12'),(28,1,'2021-06-12 11:45:28','2021-06-12 00:00:00','kgahdf',111,11,'Cheque','cheque given','B.D','birthday',1,0,100,'2022-06-07',0,2,1,'2022-06-12'),(29,1,'2021-06-12 19:49:34','2021-06-12 00:00:00','Anirudh',10999,12,'Cash','cash paid','B.D','birthday',1,0,1500,'2022-06-07',0,2,1,'2022-06-12');
/*!40000 ALTER TABLE `all_donations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `all_donors`
--

DROP TABLE IF EXISTS `all_donors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `all_donors` (
  `donor_id` int NOT NULL AUTO_INCREMENT,
  `f_name` varchar(45) DEFAULT NULL,
  `l_name` varchar(45) DEFAULT NULL,
  `address` varchar(150) DEFAULT NULL,
  `phone` varchar(10) NOT NULL,
  `email` varchar(45) DEFAULT NULL,
  `adhar_id` varchar(45) DEFAULT NULL,
  `pan_id` varchar(45) DEFAULT NULL,
  `number_of_times_donated` int DEFAULT NULL,
  PRIMARY KEY (`donor_id`),
  UNIQUE KEY `phone_UNIQUE` (`phone`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `all_donors`
--
-- ORDER BY:  `donor_id`

LOCK TABLES `all_donors` WRITE;
/*!40000 ALTER TABLE `all_donors` DISABLE KEYS */;
INSERT INTO `all_donors` VALUES (1,'chebolu','anirudh','badangpet','7032221136','ani1005sai@gmail.com','2142-35-2353-2','1234567890',18),(11,'vinnu','topper','lb nagar','1234567890','vinnu@gmail.com','123456789012','1234567890',NULL);
/*!40000 ALTER TABLE `all_donors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bank_statement`
--

DROP TABLE IF EXISTS `bank_statement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bank_statement` (
  `transaction_id` int NOT NULL AUTO_INCREMENT,
  `bank_name` varchar(45) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `withdrawal` double DEFAULT NULL,
  `deposits` double DEFAULT NULL,
  `balance` double DEFAULT NULL,
  PRIMARY KEY (`transaction_id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bank_statement`
--
-- ORDER BY:  `transaction_id`

LOCK TABLES `bank_statement` WRITE;
/*!40000 ALTER TABLE `bank_statement` DISABLE KEYS */;
INSERT INTO `bank_statement` VALUES (1,'sbi','2021-06-05','vinnu',100,NULL,500),(2,'canara','2021-06-05','topr',NULL,300,200),(3,'sbi','2021-06-10','Deposition of donations with master registration numbers 24, ',NULL,1000,1500),(4,'sbi','2021-06-10','Deposition of donations with master registration numbers 25, ',NULL,1000,2500),(7,'sbi','2021-06-10','educational expences',1000,NULL,1500),(8,'canara','2021-06-11','Deposition of donations with master registration numbers 3, 4, 5, 6, ',NULL,5000,5200),(9,'sbi','2021-06-11','Deposition of donations with master registration numbers 10, 2, 9, 1, 7, 8, 234, ',NULL,4200,5700),(10,'sbi','2021-06-11','Deposition of donations with master registration numbers 35, 123, 23, 24, ',NULL,3100,8800),(11,'sbi','2021-06-12','Deposition of donations with master registration numbers 4247, ',NULL,1500,10300),(12,'sbi','2021-06-12','Deposition of donations with master registration numbers ',NULL,0,10300),(13,'sbi','2021-06-12','subbu tution fees',1000,NULL,9300),(14,'icici','2021-06-12','intrest gained',NULL,1000,1000),(15,'icici','2021-06-12','Deposition of donations with master registration numbers 111, ',NULL,100,1100),(16,'sbi','2021-06-12','Deposition of donations with master registration numbers 10999, ',NULL,1500,10800),(17,'canara','2021-06-12','opening balance',NULL,2000,7200),(18,'sbi','2021-06-12','weekly expences',2000,NULL,8800),(19,'sbi','2021-06-13','Deposition of donations with master registration numbers ',NULL,0,8800),(20,'sbi','2021-06-13','Deposition of donations with master registration numbers ',NULL,0,8800),(21,'sbi','2021-06-13','Deposition of donations with master registration numbers ',NULL,0,8800),(22,'sbi','2021-06-13','Deposition of donations with master registration numbers ',NULL,0,8800),(23,'sbi','2021-06-13','Deposition of donations with master registration numbers ',NULL,0,8800),(24,'sbi','2021-06-13','Deposition of donations with master registration numbers ',NULL,0,8800),(25,'canara','2021-06-13','Deposition of donations with master registration numbers ',NULL,0,7200),(26,'icici','2021-06-13','Deposition of donations with master registration numbers ',NULL,0,1100),(27,'sbi','2021-06-13','Deposition of donations with master registration numbers ',NULL,0,8800),(28,'icici','2021-06-13','Deposition of donations with master registration numbers ',NULL,0,1100);
/*!40000 ALTER TABLE `bank_statement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `banks`
--

DROP TABLE IF EXISTS `banks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `banks` (
  `bankid` int NOT NULL AUTO_INCREMENT,
  `bank_name` varchar(45) DEFAULT NULL,
  `bank_details` varchar(100) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`bankid`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `banks`
--
-- ORDER BY:  `bankid`

LOCK TABLES `banks` WRITE;
/*!40000 ALTER TABLE `banks` DISABLE KEYS */;
INSERT INTO `banks` VALUES (1,'sbi',NULL,NULL),(2,'canara',NULL,NULL),(3,'icici',NULL,NULL);
/*!40000 ALTER TABLE `banks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `donations`
--

DROP TABLE IF EXISTS `donations`;
/*!50001 DROP VIEW IF EXISTS `donations`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `donations` AS SELECT 
 1 AS `id_donations`,
 1 AS `id_donor`,
 1 AS `date_of_donation`,
 1 AS `donation_date`,
 1 AS `donation_in_name`,
 1 AS `master_registration_number`,
 1 AS `reciept_number`,
 1 AS `payment_mode`,
 1 AS `payment_description`,
 1 AS `Ocassion`,
 1 AS `remarks`,
 1 AS `category`,
 1 AS `id_student`,
 1 AS `amount`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `log`
--

DROP TABLE IF EXISTS `log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `log` (
  `id` int DEFAULT NULL,
  `type` varchar(45) DEFAULT NULL,
  `loginid` int NOT NULL AUTO_INCREMENT,
  `fname` varchar(45) DEFAULT NULL,
  `lname` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`loginid`)
) ENGINE=InnoDB AUTO_INCREMENT=540 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `log`
--
-- ORDER BY:  `loginid`

LOCK TABLES `log` WRITE;
/*!40000 ALTER TABLE `log` DISABLE KEYS */;
INSERT INTO `log` VALUES (1,'normal',1,NULL,NULL),(2,'master',2,NULL,NULL),(1,'normal',3,NULL,NULL),(1,'normal',4,NULL,NULL),(2,'master',5,NULL,NULL),(1,'normal',6,NULL,NULL),(1,'normal',7,NULL,NULL),(1,'normal',8,NULL,NULL),(1,'normal',9,NULL,NULL),(1,'normal',10,NULL,NULL),(1,'normal',11,NULL,NULL),(1,'normal',12,NULL,NULL),(1,'normal',13,NULL,NULL),(1,'normal',14,NULL,NULL),(1,'normal',15,NULL,NULL),(1,'normal',16,NULL,NULL),(1,'normal',17,NULL,NULL),(1,'normal',18,NULL,NULL),(1,'normal',19,NULL,NULL),(1,'normal',20,NULL,NULL),(1,'normal',21,NULL,NULL),(1,'normal',22,NULL,NULL),(1,'normal',23,NULL,NULL),(1,'normal',24,NULL,NULL),(2,'master',25,NULL,NULL),(1,'normal',26,NULL,NULL),(1,'normal',27,NULL,NULL),(1,'normal',28,NULL,NULL),(1,'normal',29,NULL,NULL),(1,'normal',30,NULL,NULL),(1,'normal',31,NULL,NULL),(1,'normal',32,NULL,NULL),(1,'normal',33,NULL,NULL),(1,'normal',34,NULL,NULL),(1,'normal',35,NULL,NULL),(1,'normal',36,NULL,NULL),(1,'normal',37,NULL,NULL),(1,'normal',38,NULL,NULL),(1,'normal',39,NULL,NULL),(2,'master',40,NULL,NULL),(1,'normal',41,NULL,NULL),(1,'normal',42,NULL,NULL),(1,'normal',43,NULL,NULL),(1,'normal',44,NULL,NULL),(1,'normal',45,NULL,NULL),(1,'normal',46,NULL,NULL),(1,'normal',47,NULL,NULL),(1,'normal',48,NULL,NULL),(1,'normal',49,NULL,NULL),(1,'normal',50,NULL,NULL),(1,'normal',51,NULL,NULL),(1,'normal',52,NULL,NULL),(1,'normal',53,NULL,NULL),(1,'normal',54,NULL,NULL),(1,'normal',55,NULL,NULL),(1,'normal',56,NULL,NULL),(1,'normal',57,NULL,NULL),(1,'normal',58,NULL,NULL),(1,'normal',59,NULL,NULL),(1,'normal',60,NULL,NULL),(1,'normal',61,NULL,NULL),(1,'normal',62,NULL,NULL),(1,'normal',63,NULL,NULL),(1,'normal',64,NULL,NULL),(1,'normal',65,NULL,NULL),(1,'normal',66,NULL,NULL),(1,'normal',67,'kvs','ani'),(1,'normal',68,'chebolu','anirudh'),(1,'normal',69,'chebolu','anirudh'),(1,'normal',70,'chebolu','anirudh'),(1,'normal',71,'chebolu','anirudh'),(1,'normal',72,'chebolu','anirudh'),(1,'normal',73,'chebolu','anirudh'),(1,'normal',74,'chebolu','anirudh'),(1,'normal',75,'chebolu','anirudh'),(1,'normal',76,'chebolu','anirudh'),(1,'normal',77,'chebolu','anirudh'),(1,'normal',78,'chebolu','anirudh'),(1,'normal',79,'chebolu','anirudh'),(1,'normal',80,'chebolu','anirudh'),(1,'normal',81,'chebolu','anirudh'),(1,'normal',82,'chebolu','anirudh'),(1,'normal',83,'chebolu','anirudh'),(1,'normal',84,'chebolu','anirudh'),(1,'normal',85,'chebolu','anirudh'),(1,'normal',86,'chebolu','anirudh'),(1,'normal',87,'chebolu','anirudh'),(1,'normal',88,'chebolu','anirudh'),(1,'normal',89,'chebolu','anirudh'),(1,'normal',90,'chebolu','anirudh'),(1,'normal',91,'chebolu','anirudh'),(1,'normal',92,'chebolu','anirudh'),(1,'normal',93,'chebolu','anirudh'),(1,'normal',94,'chebolu','anirudh'),(1,'normal',95,'chebolu','anirudh'),(1,'normal',96,'chebolu','anirudh'),(1,'normal',97,'chebolu','anirudh'),(1,'normal',98,'chebolu','anirudh'),(2,'master',99,'Chebolu','Anirudh'),(2,'master',100,'Chebolu','Anirudh'),(2,'master',101,'Chebolu','Anirudh'),(2,'master',102,'Chebolu','Anirudh'),(2,'master',103,'Chebolu','Anirudh'),(2,'master',104,'Chebolu','Anirudh'),(2,'master',105,'Chebolu','Anirudh'),(2,'master',106,'Chebolu','Anirudh'),(2,'master',107,'Chebolu','Anirudh'),(2,'master',108,'Chebolu','Anirudh'),(2,'master',109,'Chebolu','Anirudh'),(1,'normal',110,'chebolu','anirudh'),(1,'normal',111,'chebolu','anirudh'),(1,'normal',112,'chebolu','anirudh'),(1,'normal',113,'chebolu','anirudh'),(1,'normal',114,'chebolu','anirudh'),(1,'normal',115,'chebolu','anirudh'),(1,'normal',116,'chebolu','anirudh'),(1,'normal',117,'chebolu','anirudh'),(1,'normal',118,'chebolu','anirudh'),(1,'normal',119,'chebolu','anirudh'),(1,'normal',120,'chebolu','anirudh'),(1,'normal',121,'chebolu','anirudh'),(1,'normal',122,'chebolu','anirudh'),(1,'normal',123,'chebolu','anirudh'),(1,'normal',124,'chebolu','anirudh'),(1,'normal',125,'chebolu','anirudh'),(1,'normal',126,'chebolu','anirudh'),(1,'normal',127,'chebolu','anirudh'),(1,'normal',128,'chebolu','anirudh'),(1,'normal',129,'chebolu','anirudh'),(1,'normal',130,'chebolu','anirudh'),(1,'normal',131,'chebolu','anirudh'),(1,'normal',132,'chebolu','anirudh'),(1,'normal',133,'chebolu','anirudh'),(1,'normal',134,'chebolu','anirudh'),(1,'normal',135,'chebolu','anirudh'),(1,'normal',136,'chebolu','anirudh'),(1,'normal',137,'chebolu','anirudh'),(1,'normal',138,'chebolu','anirudh'),(1,'normal',139,'chebolu','anirudh'),(1,'normal',140,'chebolu','anirudh'),(1,'normal',141,'chebolu','anirudh'),(1,'normal',142,'chebolu','anirudh'),(1,'normal',143,'chebolu','anirudh'),(1,'normal',144,'chebolu','anirudh'),(1,'normal',145,'chebolu','anirudh'),(1,'normal',146,'chebolu','anirudh'),(1,'normal',147,'chebolu','anirudh'),(1,'normal',148,'chebolu','anirudh'),(1,'normal',149,'chebolu','anirudh'),(1,'normal',150,'chebolu','anirudh'),(1,'normal',151,'chebolu','anirudh'),(1,'normal',152,'chebolu','anirudh'),(1,'normal',153,'chebolu','anirudh'),(1,'normal',154,'chebolu','anirudh'),(1,'normal',155,'chebolu','anirudh'),(1,'normal',156,'chebolu','anirudh'),(1,'normal',157,'chebolu','anirudh'),(1,'normal',158,'chebolu','anirudh'),(1,'normal',159,'chebolu','anirudh'),(1,'normal',160,'chebolu','anirudh'),(1,'normal',161,'chebolu','anirudh'),(1,'normal',162,'chebolu','anirudh'),(1,'normal',163,'chebolu','anirudh'),(1,'normal',164,'chebolu','anirudh'),(1,'normal',165,'chebolu','anirudh'),(1,'normal',166,'chebolu','anirudh'),(1,'normal',167,'chebolu','anirudh'),(1,'normal',168,'chebolu','anirudh'),(1,'normal',169,'chebolu','anirudh'),(1,'normal',170,'chebolu','anirudh'),(1,'normal',171,'chebolu','anirudh'),(1,'normal',172,'chebolu','anirudh'),(1,'normal',173,'chebolu','anirudh'),(2,'master',174,'Chebolu','Anirudh'),(2,'master',175,'Chebolu','Anirudh'),(2,'master',176,'Chebolu','Anirudh'),(2,'master',177,'Chebolu','Anirudh'),(2,'master',178,'Chebolu','Anirudh'),(1,'normal',179,'chebolu','anirudh'),(2,'master',180,'Chebolu','Anirudh'),(2,'master',181,'Chebolu','Anirudh'),(2,'master',182,'Chebolu','Anirudh'),(2,'master',183,'Chebolu','Anirudh'),(2,'master',184,'Chebolu','Anirudh'),(2,'master',185,'Chebolu','Anirudh'),(2,'master',186,'Chebolu','Anirudh'),(2,'master',187,'Chebolu','Anirudh'),(2,'master',188,'Chebolu','Anirudh'),(1,'normal',189,'chebolu','anirudh'),(1,'normal',190,'chebolu','anirudh'),(1,'normal',191,'chebolu','anirudh'),(1,'normal',192,'chebolu','anirudh'),(1,'normal',193,'chebolu','anirudh'),(1,'normal',194,'chebolu','anirudh'),(1,'normal',195,'chebolu','anirudh'),(1,'normal',196,'chebolu','anirudh'),(1,'normal',197,'chebolu','anirudh'),(1,'normal',198,'chebolu','anirudh'),(1,'normal',199,'chebolu','anirudh'),(1,'normal',200,'chebolu','anirudh'),(1,'normal',201,'chebolu','anirudh'),(1,'normal',202,'chebolu','anirudh'),(2,'master',203,'Chebolu','Anirudh'),(2,'master',204,'Chebolu','Anirudh'),(1,'normal',205,'chebolu','anirudh'),(1,'normal',206,'chebolu','anirudh'),(2,'master',207,'Chebolu','Anirudh'),(2,'master',208,'Chebolu','Anirudh'),(1,'normal',209,'chebolu','anirudh'),(2,'master',210,'Chebolu','Anirudh'),(2,'master',211,'Chebolu','Anirudh'),(2,'master',212,'Chebolu','Anirudh'),(2,'master',213,'Chebolu','Anirudh'),(2,'master',214,'Chebolu','Anirudh'),(2,'master',215,'Chebolu','Anirudh'),(2,'master',216,'Chebolu','Anirudh'),(2,'master',217,'Chebolu','Anirudh'),(2,'master',218,'Chebolu','Anirudh'),(2,'master',219,'Chebolu','Anirudh'),(2,'master',220,'Chebolu','Anirudh'),(2,'master',221,'Chebolu','Anirudh'),(2,'master',222,'Chebolu','Anirudh'),(1,'normal',223,'chebolu','anirudh'),(1,'normal',224,'chebolu','anirudh'),(1,'normal',225,'chebolu','anirudh'),(1,'normal',226,'chebolu','anirudh'),(1,'normal',227,'chebolu','anirudh'),(1,'normal',228,'chebolu','anirudh'),(1,'normal',229,'chebolu','anirudh'),(1,'normal',230,'chebolu','anirudh'),(1,'normal',231,'chebolu','anirudh'),(2,'master',232,'Chebolu','Anirudh'),(2,'master',233,'Chebolu','Anirudh'),(2,'master',234,'Chebolu','Anirudh'),(2,'master',235,'Chebolu','Anirudh'),(1,'normal',236,'chebolu','anirudh'),(1,'normal',237,'chebolu','anirudh'),(1,'normal',238,'chebolu','anirudh'),(1,'normal',239,'chebolu','anirudh'),(1,'normal',240,'chebolu','anirudh'),(1,'normal',241,'chebolu','anirudh'),(1,'normal',242,'chebolu','anirudh'),(1,'normal',243,'chebolu','anirudh'),(1,'normal',244,'chebolu','anirudh'),(1,'normal',245,'chebolu','anirudh'),(1,'normal',246,'chebolu','anirudh'),(1,'normal',247,'chebolu','anirudh'),(1,'normal',248,'chebolu','anirudh'),(1,'normal',249,'chebolu','anirudh'),(1,'normal',250,'chebolu','anirudh'),(1,'normal',251,'chebolu','anirudh'),(1,'normal',252,'chebolu','anirudh'),(1,'normal',253,'chebolu','anirudh'),(2,'master',254,'Chebolu','Anirudh'),(1,'normal',255,'chebolu','anirudh'),(1,'normal',256,'chebolu','anirudh'),(1,'normal',257,'chebolu','anirudh'),(1,'normal',258,'chebolu','anirudh'),(1,'normal',259,'chebolu','anirudh'),(1,'normal',260,'chebolu','anirudh'),(1,'normal',261,'chebolu','anirudh'),(1,'normal',262,'chebolu','anirudh'),(1,'normal',263,'chebolu','anirudh'),(2,'master',264,'Chebolu','Anirudh'),(2,'master',265,'Chebolu','Anirudh'),(2,'master',266,'Chebolu','Anirudh'),(2,'master',267,'Chebolu','Anirudh'),(2,'master',268,'Chebolu','Anirudh'),(2,'master',269,'Chebolu','Anirudh'),(1,'normal',270,'chebolu','anirudh'),(1,'normal',271,'chebolu','anirudh'),(1,'normal',272,'chebolu','anirudh'),(1,'normal',273,'chebolu','anirudh'),(1,'normal',274,'chebolu','anirudh'),(1,'normal',275,'chebolu','anirudh'),(1,'normal',276,'chebolu','anirudh'),(1,'normal',277,'chebolu','anirudh'),(1,'normal',278,'chebolu','anirudh'),(1,'normal',279,'chebolu','anirudh'),(1,'normal',280,'chebolu','anirudh'),(1,'normal',281,'chebolu','anirudh'),(1,'normal',282,'chebolu','anirudh'),(1,'normal',283,'chebolu','anirudh'),(1,'normal',284,'chebolu','anirudh'),(2,'master',285,'Chebolu','Anirudh'),(3,'master',286,'Vinay','Topper'),(1,'normal',287,'chebolu','anirudh'),(1,'normal',288,'chebolu','anirudh'),(1,'normal',289,'chebolu','anirudh'),(1,'normal',290,'chebolu','anirudh'),(1,'normal',291,'chebolu','anirudh'),(1,'normal',292,'chebolu','anirudh'),(2,'master',293,'Chebolu','Anirudh'),(1,'normal',294,'chebolu','anirudh'),(1,'normal',295,'chebolu','anirudh'),(1,'normal',296,'chebolu','anirudh'),(1,'normal',297,'chebolu','anirudh'),(2,'master',298,'Chebolu','Anirudh'),(1,'normal',299,'chebolu','anirudh'),(2,'master',300,'Chebolu','Anirudh'),(2,'master',301,'Chebolu','Anirudh'),(2,'master',302,'Chebolu','Anirudh'),(2,'master',303,'Chebolu','Anirudh'),(2,'master',304,'Chebolu','Anirudh'),(2,'master',305,'Chebolu','Anirudh'),(2,'master',306,'Chebolu','Anirudh'),(1,'normal',307,'chebolu','anirudh'),(1,'normal',308,'chebolu','anirudh'),(1,'normal',309,'chebolu','anirudh'),(1,'normal',310,'chebolu','anirudh'),(1,'normal',311,'chebolu','anirudh'),(1,'normal',312,'chebolu','anirudh'),(1,'normal',313,'chebolu','anirudh'),(1,'normal',314,'chebolu','anirudh'),(1,'normal',315,'chebolu','anirudh'),(1,'normal',316,'chebolu','anirudh'),(1,'normal',317,'chebolu','anirudh'),(1,'normal',318,'chebolu','anirudh'),(1,'normal',319,'chebolu','anirudh'),(1,'normal',320,'chebolu','anirudh'),(1,'normal',321,'chebolu','anirudh'),(1,'normal',322,'chebolu','anirudh'),(1,'normal',323,'chebolu','anirudh'),(1,'normal',324,'chebolu','anirudh'),(1,'normal',325,'chebolu','anirudh'),(1,'normal',326,'chebolu','anirudh'),(1,'normal',327,'chebolu','anirudh'),(1,'normal',328,'chebolu','anirudh'),(1,'normal',329,'chebolu','anirudh'),(1,'normal',330,'chebolu','anirudh'),(1,'normal',331,'chebolu','anirudh'),(1,'normal',332,'chebolu','anirudh'),(1,'normal',333,'chebolu','anirudh'),(1,'normal',334,'chebolu','anirudh'),(1,'normal',335,'chebolu','anirudh'),(1,'normal',336,'chebolu','anirudh'),(1,'normal',337,'chebolu','anirudh'),(1,'normal',338,'chebolu','anirudh'),(1,'normal',339,'chebolu','anirudh'),(1,'normal',340,'chebolu','anirudh'),(1,'normal',341,'chebolu','anirudh'),(1,'normal',342,'chebolu','anirudh'),(1,'normal',343,'chebolu','anirudh'),(1,'normal',344,'chebolu','anirudh'),(1,'normal',345,'chebolu','anirudh'),(1,'normal',346,'chebolu','anirudh'),(1,'normal',347,'chebolu','anirudh'),(1,'normal',348,'chebolu','anirudh'),(1,'normal',349,'chebolu','anirudh'),(1,'normal',350,'chebolu','anirudh'),(1,'normal',351,'chebolu','anirudh'),(1,'normal',352,'chebolu','anirudh'),(1,'normal',353,'chebolu','anirudh'),(1,'normal',354,'chebolu','anirudh'),(1,'normal',355,'chebolu','anirudh'),(1,'normal',356,'chebolu','anirudh'),(1,'normal',357,'chebolu','anirudh'),(1,'normal',358,'chebolu','anirudh'),(1,'normal',359,'chebolu','anirudh'),(1,'normal',360,'chebolu','anirudh'),(1,'normal',361,'chebolu','anirudh'),(1,'normal',362,'chebolu','anirudh'),(1,'normal',363,'chebolu','anirudh'),(1,'normal',364,'chebolu','anirudh'),(1,'normal',365,'chebolu','anirudh'),(1,'normal',366,'chebolu','anirudh'),(1,'normal',367,'chebolu','anirudh'),(1,'normal',368,'chebolu','anirudh'),(1,'normal',369,'chebolu','anirudh'),(1,'normal',370,'chebolu','anirudh'),(1,'normal',371,'chebolu','anirudh'),(1,'normal',372,'chebolu','anirudh'),(1,'normal',373,'chebolu','anirudh'),(1,'normal',374,'chebolu','anirudh'),(1,'normal',375,'chebolu','anirudh'),(1,'normal',376,'chebolu','anirudh'),(1,'normal',377,'chebolu','anirudh'),(1,'normal',378,'chebolu','anirudh'),(1,'normal',379,'chebolu','anirudh'),(1,'normal',380,'chebolu','anirudh'),(1,'normal',381,'chebolu','anirudh'),(1,'normal',382,'chebolu','anirudh'),(1,'normal',383,'chebolu','anirudh'),(1,'normal',384,'chebolu','anirudh'),(1,'normal',385,'chebolu','anirudh'),(1,'normal',386,'chebolu','anirudh'),(1,'normal',387,'chebolu','anirudh'),(1,'normal',388,'chebolu','anirudh'),(1,'normal',389,'chebolu','anirudh'),(1,'normal',390,'chebolu','anirudh'),(1,'normal',391,'chebolu','anirudh'),(1,'normal',392,'chebolu','anirudh'),(1,'normal',393,'chebolu','anirudh'),(1,'normal',394,'chebolu','anirudh'),(1,'normal',395,'chebolu','anirudh'),(1,'normal',396,'chebolu','anirudh'),(1,'normal',397,'chebolu','anirudh'),(1,'normal',398,'chebolu','anirudh'),(1,'normal',399,'chebolu','anirudh'),(1,'normal',400,'chebolu','anirudh'),(1,'normal',401,'chebolu','anirudh'),(1,'normal',402,'chebolu','anirudh'),(1,'normal',403,'chebolu','anirudh'),(1,'normal',404,'chebolu','anirudh'),(1,'normal',405,'chebolu','anirudh'),(1,'normal',406,'chebolu','anirudh'),(1,'normal',407,'chebolu','anirudh'),(1,'normal',408,'chebolu','anirudh'),(1,'normal',409,'chebolu','anirudh'),(1,'normal',410,'chebolu','anirudh'),(1,'normal',411,'chebolu','anirudh'),(1,'normal',412,'chebolu','anirudh'),(1,'normal',413,'chebolu','anirudh'),(1,'normal',414,'chebolu','anirudh'),(1,'normal',415,'chebolu','anirudh'),(1,'normal',416,'chebolu','anirudh'),(1,'normal',417,'chebolu','anirudh'),(1,'normal',418,'chebolu','anirudh'),(1,'normal',419,'chebolu','anirudh'),(1,'normal',420,'chebolu','anirudh'),(1,'normal',421,'chebolu','anirudh'),(1,'normal',422,'chebolu','anirudh'),(2,'master',423,'Chebolu','Anirudh'),(2,'master',424,'Chebolu','Anirudh'),(1,'normal',425,'chebolu','anirudh'),(2,'master',426,'Chebolu','Anirudh'),(1,'normal',427,'chebolu','anirudh'),(2,'master',428,'Chebolu','Anirudh'),(1,'normal',429,'chebolu','anirudh'),(2,'master',430,'Chebolu','Anirudh'),(2,'master',431,'Chebolu','Anirudh'),(2,'master',432,'Chebolu','Anirudh'),(2,'master',433,'Chebolu','Anirudh'),(2,'master',434,'Chebolu','Anirudh'),(2,'master',435,'Chebolu','Anirudh'),(2,'master',436,'Chebolu','Anirudh'),(2,'master',437,'Chebolu','Anirudh'),(2,'master',438,'Chebolu','Anirudh'),(2,'master',439,'Chebolu','Anirudh'),(2,'master',440,'Chebolu','Anirudh'),(2,'master',441,'Chebolu','Anirudh'),(2,'master',442,'Chebolu','Anirudh'),(2,'master',443,'Chebolu','Anirudh'),(2,'master',444,'Chebolu','Anirudh'),(2,'master',445,'Chebolu','Anirudh'),(2,'master',446,'Chebolu','Anirudh'),(2,'master',447,'Chebolu','Anirudh'),(2,'master',448,'Chebolu','Anirudh'),(2,'master',449,'Chebolu','Anirudh'),(2,'master',450,'Chebolu','Anirudh'),(2,'master',451,'Chebolu','Anirudh'),(2,'master',452,'Chebolu','Anirudh'),(2,'master',453,'Chebolu','Anirudh'),(2,'master',454,'Chebolu','Anirudh'),(2,'master',455,'Chebolu','Anirudh'),(2,'master',456,'Chebolu','Anirudh'),(2,'master',457,'Chebolu','Anirudh'),(1,'normal',458,'chebolu','anirudh'),(2,'master',459,'Chebolu','Anirudh'),(1,'normal',460,'chebolu','anirudh'),(2,'master',461,'Chebolu','Anirudh'),(2,'master',462,'Chebolu','Anirudh'),(2,'master',463,'Chebolu','Anirudh'),(2,'master',464,'Chebolu','Anirudh'),(2,'master',465,'Chebolu','Anirudh'),(2,'master',466,'Chebolu','Anirudh'),(2,'master',467,'Chebolu','Anirudh'),(2,'master',468,'Chebolu','Anirudh'),(2,'master',469,'Chebolu','Anirudh'),(2,'master',470,'Chebolu','Anirudh'),(2,'master',471,'Chebolu','Anirudh'),(2,'master',472,'Chebolu','Anirudh'),(2,'master',473,'Chebolu','Anirudh'),(2,'master',474,'Chebolu','Anirudh'),(2,'master',475,'Chebolu','Anirudh'),(1,'normal',476,'chebolu','anirudh'),(2,'master',477,'Chebolu','Anirudh'),(2,'master',478,'Chebolu','Anirudh'),(2,'master',479,'Chebolu','Anirudh'),(2,'master',480,'Chebolu','Anirudh'),(2,'master',481,'Chebolu','Anirudh'),(2,'master',482,'Chebolu','Anirudh'),(1,'normal',483,'chebolu','anirudh'),(2,'master',484,'Chebolu','Anirudh'),(1,'normal',485,'chebolu','anirudh'),(1,'normal',486,'chebolu','anirudh'),(1,'normal',487,'chebolu','anirudh'),(1,'normal',488,'chebolu','anirudh'),(1,'normal',489,'chebolu','anirudh'),(1,'normal',490,'chebolu','anirudh'),(1,'normal',491,'chebolu','anirudh'),(1,'normal',492,'chebolu','anirudh'),(1,'normal',493,'chebolu','anirudh'),(1,'normal',494,'chebolu','anirudh'),(1,'normal',495,'chebolu','anirudh'),(1,'normal',496,'chebolu','anirudh'),(1,'normal',497,'chebolu','anirudh'),(1,'normal',498,'chebolu','anirudh'),(1,'normal',499,'chebolu','anirudh'),(1,'normal',500,'chebolu','anirudh'),(2,'master',501,'Chebolu','Anirudh'),(2,'master',502,'Chebolu','Anirudh'),(1,'normal',503,'chebolu','anirudh'),(2,'master',504,'Chebolu','Anirudh'),(2,'master',505,'Chebolu','Anirudh'),(1,'normal',506,'chebolu','anirudh'),(1,'normal',507,'chebolu','anirudh'),(1,'normal',508,'chebolu','anirudh'),(1,'normal',509,'chebolu','anirudh'),(2,'master',510,'Chebolu','Anirudh'),(2,'master',511,'Chebolu','Anirudh'),(2,'master',512,'Chebolu','Anirudh'),(2,'master',513,'Chebolu','Anirudh'),(2,'master',514,'Chebolu','Anirudh'),(1,'normal',515,'chebolu','anirudh'),(1,'normal',516,'chebolu','anirudh'),(1,'normal',517,'chebolu','anirudh'),(1,'normal',518,'chebolu','anirudh'),(1,'normal',519,'chebolu','anirudh'),(1,'normal',520,'chebolu','anirudh'),(1,'normal',521,'chebolu','anirudh'),(1,'normal',522,'chebolu','anirudh'),(1,'normal',523,'chebolu','anirudh'),(1,'normal',524,'chebolu','anirudh'),(1,'normal',525,'chebolu','anirudh'),(1,'normal',526,'chebolu','anirudh'),(1,'normal',527,'chebolu','anirudh'),(1,'normal',528,'chebolu','anirudh'),(2,'master',529,'Chebolu','Anirudh'),(2,'master',530,'Chebolu','Anirudh'),(1,'normal',531,'chebolu','anirudh'),(2,'master',532,'Chebolu','Anirudh'),(1,'normal',533,'chebolu','anirudh'),(2,'master',534,'Chebolu','Anirudh'),(1,'normal',535,'chebolu','anirudh'),(1,'normal',536,'chebolu','anirudh'),(1,'normal',537,'chebolu','anirudh'),(1,'normal',538,'chebolu','anirudh'),(1,'normal',539,'chebolu','anirudh');
/*!40000 ALTER TABLE `log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login`
--

DROP TABLE IF EXISTS `login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `login` (
  `idlogin` int NOT NULL AUTO_INCREMENT,
  `username` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  `login_type` varchar(45) DEFAULT NULL,
  `fname` varchar(45) DEFAULT NULL,
  `lname` varchar(45) DEFAULT NULL,
  `designation` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idlogin`),
  UNIQUE KEY `username_UNIQUE` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login`
--
-- ORDER BY:  `idlogin`

LOCK TABLES `login` WRITE;
/*!40000 ALTER TABLE `login` DISABLE KEYS */;
INSERT INTO `login` VALUES (1,'kvs','ani','normal','chebolu','anirudh','-'),(2,'chvsanirudh','ani','master','Chebolu','Anirudh','-'),(3,'vinay','subbubugga','master','Vinay','Topper','1st class');
/*!40000 ALTER TABLE `login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_cashbook`
--

DROP TABLE IF EXISTS `main_cashbook`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `main_cashbook` (
  `transaction_id` int NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `name` varchar(200) DEFAULT NULL,
  `master_registration_number` int DEFAULT NULL,
  `reciept_number` int DEFAULT NULL,
  `category` varchar(45) DEFAULT NULL,
  `debit` int DEFAULT '0',
  `credit` int DEFAULT '0',
  `balance` int DEFAULT NULL,
  `deposited` int DEFAULT '0',
  PRIMARY KEY (`transaction_id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_cashbook`
--
-- ORDER BY:  `transaction_id`

LOCK TABLES `main_cashbook` WRITE;
/*!40000 ALTER TABLE `main_cashbook` DISABLE KEYS */;
INSERT INTO `main_cashbook` VALUES (9,'2021-05-18','sid',10,1,'1',400,0,400,1),(10,'2021-05-18','tarun',2,2,'1',300,0,700,1),(11,'2021-05-18','tarun',9,2,'4',500,0,1200,1),(12,'2021-05-18','vinay',1,2,'7',1000,0,2200,1),(13,'2021-05-18','sid',3,2,'1',1500,0,3700,1),(14,'2021-05-18','sid',4,2,'2',1500,0,5200,1),(15,'2021-05-18','kvs',5,2,'7',1500,0,6700,1),(16,'2021-05-17','kvs',6,5,'1',500,0,7200,1),(17,'2021-05-19','kvs',7,5,'1',500,0,7700,1),(18,'2021-05-19','subaramanyam',8,5,'1',1000,0,8700,1),(19,'2021-05-20','Name',234,2443,'5',500,0,9200,1),(20,'2021-05-21','subbu',35,436,'1',1000,0,10200,1),(21,'2021-05-21','subbu',123,123,'1',1000,0,11200,1),(22,'2021-06-09','subbu',23,35,'1',100,0,11300,1),(23,'2021-06-09','subbu',24,37,'1',1000,0,12300,1),(24,'2021-06-11','Deposition of donations with master registration numbers 3, 4, 5, 6, ',NULL,NULL,NULL,0,5000,7300,1),(25,'2021-06-11','Deposition of donations with master registration numbers 10, 2, 9, 1, 7, 8, 234, ',NULL,NULL,NULL,0,4200,3100,1),(26,'2021-06-11','Deposition of donations with master registration numbers 35, 123, 23, 24, ',NULL,NULL,NULL,0,3100,0,1),(27,'2021-06-12','T K subramanyam',4247,25,'1',1500,0,1500,1),(28,'2021-06-12','Deposition of donations with master registration numbers 4247, ',NULL,NULL,NULL,0,1500,0,1),(29,'2021-06-12','vinay shankar',60,59,'1',500,0,500,1),(30,'2021-06-12','Deposition of donations with master registration numbers 60, ',NULL,NULL,NULL,0,500,0,1),(31,'2021-06-12','Deposition of donations with master registration numbers 60, ',NULL,NULL,NULL,0,500,-500,1),(32,'2021-06-12','Deposition of donations with master registration numbers 60, ',NULL,NULL,NULL,0,500,-1000,1),(33,'2021-06-12','Deposition of donations with master registration numbers ',NULL,NULL,NULL,0,0,-1000,1),(34,'2021-06-12','kgahdf',111,11,'1',100,0,-900,1),(35,'2021-06-12','Deposition of donations with master registration numbers 111, ',NULL,NULL,NULL,0,100,-1000,1),(36,'2021-06-12','Anirudh',10999,12,'1',1500,0,500,1),(37,'2021-06-12','Deposition of donations with master registration numbers 10999, ',NULL,NULL,NULL,0,1500,-1000,1),(38,'2021-06-13','Deposition of donations with master registration numbers ',NULL,NULL,NULL,0,0,-1000,1),(39,'2021-06-13','Deposition of donations with master registration numbers ',NULL,NULL,NULL,0,0,-1000,1),(40,'2021-06-13','Deposition of donations with master registration numbers ',NULL,NULL,NULL,0,0,-1000,1),(41,'2021-06-13','Deposition of donations with master registration numbers ',NULL,NULL,NULL,0,0,-1000,1),(42,'2021-06-13','Deposition of donations with master registration numbers ',NULL,NULL,NULL,0,0,-1000,1),(43,'2021-06-13','Deposition of donations with master registration numbers ',NULL,NULL,NULL,0,0,-1000,1),(44,'2021-06-13','Deposition of donations with master registration numbers ',NULL,NULL,NULL,0,0,-1000,1),(45,'2021-06-13','Deposition of donations with master registration numbers ',NULL,NULL,NULL,0,0,-1000,1),(46,'2021-06-13','Deposition of donations with master registration numbers ',NULL,NULL,NULL,0,0,-1000,1),(47,'2021-06-13','Deposition of donations with master registration numbers ',NULL,NULL,NULL,0,0,-1000,1),(48,'2021-06-13','Deposition of donations with master registration numbers ',NULL,NULL,NULL,0,0,-1000,1);
/*!40000 ALTER TABLE `main_cashbook` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `petty_cashbook`
--

DROP TABLE IF EXISTS `petty_cashbook`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `petty_cashbook` (
  `transaction_id` int NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `name` varchar(45) DEFAULT NULL,
  `reciept_number` varchar(200) DEFAULT NULL,
  `category` varchar(45) DEFAULT NULL,
  `debit` int DEFAULT '0',
  `credit` int DEFAULT '0',
  `balance` int DEFAULT '0',
  PRIMARY KEY (`transaction_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `petty_cashbook`
--
-- ORDER BY:  `transaction_id`

LOCK TABLES `petty_cashbook` WRITE;
/*!40000 ALTER TABLE `petty_cashbook` DISABLE KEYS */;
INSERT INTO `petty_cashbook` VALUES (6,'2021-06-09','tution fee','30','12 salaries tutors',0,1000,-1000),(7,'2021-06-09','training','42','44 educational expences / training programs',0,1000,-2000),(8,'2021-06-09','petrol','59','32 administration expences / petrol',0,1000,-3000),(9,'2021-06-12',NULL,'subbu tution fees','Withdrawal from bank',1000,0,-2000),(10,'2021-06-12',NULL,'weekly expences','Withdrawal from bank',2000,0,0);
/*!40000 ALTER TABLE `petty_cashbook` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pettycashbook`
--

DROP TABLE IF EXISTS `pettycashbook`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pettycashbook` (
  `id` int NOT NULL AUTO_INCREMENT,
  `voucherid` int NOT NULL,
  `paidto` varchar(45) DEFAULT NULL,
  `voucherdate` date DEFAULT NULL,
  `amount` int NOT NULL,
  `type` varchar(45) DEFAULT NULL,
  `payment_mode` varchar(45) DEFAULT NULL,
  `check_dated` date DEFAULT NULL,
  `towards` varchar(45) DEFAULT NULL,
  `drawn_on` date DEFAULT NULL,
  `masterid` int DEFAULT NULL,
  `checked` int DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `voucherid_UNIQUE` (`voucherid`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pettycashbook`
--
-- ORDER BY:  `id`

LOCK TABLES `pettycashbook` WRITE;
/*!40000 ALTER TABLE `pettycashbook` DISABLE KEYS */;
INSERT INTO `pettycashbook` VALUES (1,2,'killer','2021-05-19',500,'10 salaries warden and clerk','cash','2021-05-19','salary','2021-05-19',2,1),(3,4,'vinnu','2021-05-19',1000,'12 salaries tutors','cash','2021-05-19','salary','2021-05-19',2,1),(6,5,'kaushal','2021-05-20',500,'22 mess expences/ milk','cash','2021-05-20','milk','2021-05-20',2,1),(7,6,'tarun','2021-05-20',100,'32 administration expences / petrol','cash','2021-05-20','petrol','2021-05-20',2,1),(8,30,'subbu','2021-06-09',1000,'12 salaries tutors','cash','2021-06-09','tution fee','2021-06-09',2,1),(9,42,'subbu','2021-06-09',1000,'44 educational expences / training programs','cash','2021-06-09','training','2021-06-09',2,1),(10,59,'vinay','2021-06-09',1000,'32 administration expences / petrol','cash','2021-06-09','petrol','2021-06-09',2,1);
/*!40000 ALTER TABLE `pettycashbook` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schemes`
--

DROP TABLE IF EXISTS `schemes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `schemes` (
  `idschemes` int NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `validity` int DEFAULT NULL,
  `remainder` int DEFAULT NULL,
  PRIMARY KEY (`idschemes`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schemes`
--
-- ORDER BY:  `idschemes`

LOCK TABLES `schemes` WRITE;
/*!40000 ALTER TABLE `schemes` DISABLE KEYS */;
INSERT INTO `schemes` VALUES (1,'Nitya Annadhana Nidhi',360,2),(2,'Shaswitha Annadhana Nidhi',NULL,NULL),(3,'Smruthi Nidhi',NULL,NULL),(4,'Vidyarthi Poshaka Nidhi',NULL,NULL),(5,'Vidyarthi Patashala Rusumu Nidhi',NULL,NULL),(6,'Vidyarthi Samraksha Nidhi',NULL,NULL),(7,'Patron',NULL,NULL),(8,'General Donation',NULL,NULL);
/*!40000 ALTER TABLE `schemes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `idstudent` int NOT NULL AUTO_INCREMENT,
  `ashramam_id` int NOT NULL,
  `fname` varchar(45) DEFAULT NULL,
  `lname` varchar(45) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `student_details` varchar(1000) DEFAULT NULL,
  `school_name` varchar(45) DEFAULT NULL,
  `school_address` varchar(200) DEFAULT NULL,
  `studying` varchar(45) DEFAULT NULL,
  `academic_year` varchar(20) DEFAULT NULL,
  `annualfeel` int DEFAULT NULL,
  `feepaid` int DEFAULT NULL,
  `adharnumber` int DEFAULT NULL,
  PRIMARY KEY (`idstudent`),
  UNIQUE KEY `idstudent_UNIQUE` (`idstudent`),
  UNIQUE KEY `ashramam_id_UNIQUE` (`ashramam_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--
-- ORDER BY:  `idstudent`

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (1,1,'balayya','Last name','2000-01-01','he is a intelligent kid.','chaina','narsinghi','11','2018-19',100000,2000,1234567890);
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `type_expenditure`
--

DROP TABLE IF EXISTS `type_expenditure`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `type_expenditure` (
  `code` int NOT NULL,
  `code_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `type_expenditure`
--
-- ORDER BY:  `code`

LOCK TABLES `type_expenditure` WRITE;
/*!40000 ALTER TABLE `type_expenditure` DISABLE KEYS */;
INSERT INTO `type_expenditure` VALUES (10,'10 salaries warden and clerk'),(11,'11 salaries cook'),(12,'12 salaries tutors'),(20,'20 mess expences / vegetables'),(21,'21 mess expences/ LPG'),(22,'22 mess expences/ milk'),(23,'23 mess expences/ kirana items'),(30,'30 administration expences / electricity bills'),(31,'31 administration expences / repairs & maintenance'),(32,'32 administration expences / petrol'),(33,'33 administration expences / conveyance'),(34,'34 administration expences / postage,mobile,telephonebills,internet,cable charges'),(35,'35 administration expences / printing bulletings'),(36,'36 administration expences / printing general'),(37,'37 administration expences / stationary items for office'),(38,'38 administration expences / bank charges'),(39,'39 administration expences / meetings'),(40,'40 educational expences / school and college fees'),(41,'41 educational expences / bus passes'),(42,'42 educational expences / exam fees'),(43,'43 educational expences / books,stationary items for students'),(44,'44 educational expences / training programs'),(45,'45 educational expences '),(50,'50 medical expences'),(51,'51 major building renovation or repairs'),(90,'90 miscellaneous / general'),(99,'99 FDS');
/*!40000 ALTER TABLE `type_expenditure` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `donations`
--

/*!50001 DROP VIEW IF EXISTS `donations`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `donations` AS select `all_donations`.`id_donations` AS `id_donations`,`all_donations`.`id_donor` AS `id_donor`,`all_donations`.`date_of_donation` AS `date_of_donation`,`all_donations`.`donation_date` AS `donation_date`,`all_donations`.`donation_in_name` AS `donation_in_name`,`all_donations`.`master_registration_number` AS `master_registration_number`,`all_donations`.`reciept_number` AS `reciept_number`,`all_donations`.`payment_mode` AS `payment_mode`,`all_donations`.`payment_description` AS `payment_description`,`all_donations`.`Ocassion` AS `Ocassion`,`all_donations`.`remarks` AS `remarks`,`all_donations`.`category` AS `category`,`all_donations`.`id_student` AS `id_student`,`all_donations`.`amount` AS `amount` from `all_donations` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-13 17:37:02
