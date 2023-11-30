-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: hms3
-- ------------------------------------------------------
-- Server version	8.0.34

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
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES ('bhoomi','abcd');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `appointment`
--

LOCK TABLES `appointment` WRITE;
/*!40000 ALTER TABLE `appointment` DISABLE KEYS */;
INSERT INTO `appointment` VALUES (1,'2023-11-14','16:30:00',13,NULL),(2,'2023-11-18','13:30:00',13,NULL),(3,'2023-11-15','03:50:00',11,NULL),(4,'2023-11-16','12:40:00',12,NULL),(5,'2023-11-17','12:40:00',14,5),(6,'2023-11-17','13:10:00',14,6),(7,'2023-11-21','14:45:00',12,9),(9,'2023-11-21','19:30:00',15,2),(10,'2023-11-22','11:00:00',13,2),(11,'2023-11-23','12:20:00',16,NULL),(12,'2023-11-22','12:15:00',12,10),(13,'2023-11-22','13:25:00',15,11),(14,'2023-11-22','12:00:00',16,12),(15,'2023-11-23','10:00:00',16,2);
/*!40000 ALTER TABLE `appointment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `appointment_status`
--

LOCK TABLES `appointment_status` WRITE;
/*!40000 ALTER TABLE `appointment_status` DISABLE KEYS */;
INSERT INTO `appointment_status` VALUES ('Cancel',1),('Confirm',3),('Cancel',2),('Cancel',4),('Confirm',5),('Confirm',6),('Confirm',7),('Confirm',9),('Confirm',10),('Cancel',11),('Cancel',12),('Cancel',13),('Confirm',14),('Confirm',15);
/*!40000 ALTER TABLE `appointment_status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `bed`
--

LOCK TABLES `bed` WRITE;
/*!40000 ALTER TABLE `bed` DISABLE KEYS */;
INSERT INTO `bed` VALUES (1),(2),(3),(4),(5),(6),(7),(8),(9),(10),(11),(12),(13),(14),(15),(16),(17),(18),(19),(20);
/*!40000 ALTER TABLE `bed` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `bed_bedcost`
--

LOCK TABLES `bed_bedcost` WRITE;
/*!40000 ALTER TABLE `bed_bedcost` DISABLE KEYS */;
INSERT INTO `bed_bedcost` VALUES (800,1),(800,20);
/*!40000 ALTER TABLE `bed_bedcost` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `bed_bedtype`
--

LOCK TABLES `bed_bedtype` WRITE;
/*!40000 ALTER TABLE `bed_bedtype` DISABLE KEYS */;
INSERT INTO `bed_bedtype` VALUES ('Single',1),('Single',20);
/*!40000 ALTER TABLE `bed_bedtype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `bill`
--

LOCK TABLES `bill` WRITE;
/*!40000 ALTER TABLE `bill` DISABLE KEYS */;
INSERT INTO `bill` VALUES (600,'bhoomi',2,2),(600,'bhoomi',2,3),(1500,'bhoomi',9,4),(1200,'bhoomi',2,5),(700,'bhoomi',10,6),(700,'bhoomi',10,7),(700,'bhoomi',10,8),(0,'bhoomi',4,10),(0,'bhoomi',4,11),(1700,'bhoomi',12,12),(900,'bhoomi',7,13),(0,'bhoomi',7,14),(2900,'bhoomi',2,15);
/*!40000 ALTER TABLE `bill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `doctor`
--

LOCK TABLES `doctor` WRITE;
/*!40000 ALTER TABLE `doctor` DISABLE KEYS */;
INSERT INTO `doctor` VALUES (11,'Raj Shekhar','Cardiologist','raj123',1000,'bhoomi'),(12,'Aravind Pai','Orthopedic','pai123',700,'bhoomi'),(13,'Ramraj PN','Oral Surgeon','ram123',600,'bhoomi'),(14,'Pranav Srikar','Gynecologist','pranav123',700,'bhoomi'),(15,'Deepak Parmar','Dermatologist','deepak123',600,'bhoomi'),(16,'Bharath Raja','ENT','b123',900,'bhoomi'),(17,'Anita Singh','Pediatrician','anita123',500,'bhoomi');
/*!40000 ALTER TABLE `doctor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `patient`
--

LOCK TABLES `patient` WRITE;
/*!40000 ALTER TABLE `patient` DISABLE KEYS */;
INSERT INTO `patient` VALUES (2,'nidhi5','Nidhi Bhat','nidhi123',15,15,20),(3,'anan9','Ananya Jha','a123',NULL,NULL,NULL),(4,'diya27','Diya Kalyanpur','diya123',4,11,NULL),(5,'pranav1','Pranav Sharma','pranav123',5,NULL,NULL),(6,'rish3','Rishika Kinger','r123',6,NULL,NULL),(7,'anna','Anna Bell','123',11,14,NULL),(9,'virat5','Virat Kohli','v123',7,4,1),(10,'arshya','Arshya Khurana','abc',12,8,NULL),(11,'megh','Meghana Goru','m123',13,9,NULL),(12,'shreya','Shreya Sridhar','s123',14,12,20);
/*!40000 ALTER TABLE `patient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `prescription`
--

LOCK TABLES `prescription` WRITE;
/*!40000 ALTER TABLE `prescription` DISABLE KEYS */;
INSERT INTO `prescription` VALUES ('fever','high temperature',101,2,11,'no'),('Joint Pain','Difficult to walk',102,4,12,'no'),('bleeding','intense',103,5,14,'no'),('Arm Fracture','Cast for two weeks',104,9,12,'yes'),('Rashes','Itching badly',106,2,15,'no'),('Root Canal','Deep Cavity',107,2,13,'no'),('Ear pain ','',108,12,16,'yes'),('Ear pain ','cant hear',110,2,16,'yes');
/*!40000 ALTER TABLE `prescription` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `prescription_medicines`
--

LOCK TABLES `prescription_medicines` WRITE;
/*!40000 ALTER TABLE `prescription_medicines` DISABLE KEYS */;
INSERT INTO `prescription_medicines` VALUES ('M1',101),('M2',101),('M3',102),('M4',102),('M5,M6',103),('M8,M9',104),('M17,M34',106),('M8,M10',107),('M5,M19',108),('M1,M6',110);
/*!40000 ALTER TABLE `prescription_medicines` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-30 18:50:21
