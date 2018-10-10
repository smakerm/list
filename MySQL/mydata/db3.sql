-- MySQL dump 10.14  Distrib 5.5.56-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: db3
-- ------------------------------------------------------
-- Server version	5.5.56-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bjtab`
--

DROP TABLE IF EXISTS `bjtab`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bjtab` (
  `stu_id` int(11) DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL,
  `money` int(11) DEFAULT NULL,
  KEY `stu_id` (`stu_id`),
  CONSTRAINT `bjtab_ibfk_1` FOREIGN KEY (`stu_id`) REFERENCES `jftab` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bjtab`
--

LOCK TABLES `bjtab` WRITE;
/*!40000 ALTER TABLE `bjtab` DISABLE KEYS */;
INSERT INTO `bjtab` VALUES (1,'唐伯虎',28000);
/*!40000 ALTER TABLE `bjtab` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `city`
--

DROP TABLE IF EXISTS `city`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `city` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `C_ID` int(11) DEFAULT NULL,
  `C_name` varchar(15) DEFAULT NULL,
  `CFather_ID` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `city`
--

LOCK TABLES `city` WRITE;
/*!40000 ALTER TABLE `city` DISABLE KEYS */;
INSERT INTO `city` VALUES (1,131100,'石家庄市',130000),(2,131101,'沧州市',130000),(3,131102,'廊坊市',130000),(4,131103,'衡水市',130000),(5,131104,'太原市',140000),(6,131105,'呼和浩特市',150000),(7,131106,'包头市',150000),(8,131107,'沈阳市',160000),(9,131108,'大连市',160000),(10,131109,'无锡市',320000),(11,131110,'徐州市',320000),(12,131111,'常州市',320000);
/*!40000 ALTER TABLE `city` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jftab`
--

DROP TABLE IF EXISTS `jftab`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jftab` (
  `id` int(11) NOT NULL,
  `name` char(20) DEFAULT NULL,
  `class` char(7) DEFAULT NULL,
  `money` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jftab`
--

LOCK TABLES `jftab` WRITE;
/*!40000 ALTER TABLE `jftab` DISABLE KEYS */;
INSERT INTO `jftab` VALUES (1,'唐伯虎','AID1712',28000),(3,'祝枝山','AID1712',25000);
/*!40000 ALTER TABLE `jftab` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sheng`
--

DROP TABLE IF EXISTS `sheng`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sheng` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `S_ID` int(11) DEFAULT NULL,
  `S_name` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sheng`
--

LOCK TABLES `sheng` WRITE;
/*!40000 ALTER TABLE `sheng` DISABLE KEYS */;
INSERT INTO `sheng` VALUES (1,130000,'河北省'),(2,140000,'山西省'),(3,150000,'内蒙古自治区'),(4,160000,'辽宁省'),(5,170000,'黑龙江省');
/*!40000 ALTER TABLE `sheng` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t1`
--

DROP TABLE IF EXISTS `t1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t1` (
  `id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `sex` enum('boy','girl') DEFAULT 'boy',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t1`
--

LOCK TABLES `t1` WRITE;
/*!40000 ALTER TABLE `t1` DISABLE KEYS */;
INSERT INTO `t1` VALUES (1,'zhang','boy');
/*!40000 ALTER TABLE `t1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t2`
--

DROP TABLE IF EXISTS `t2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t2` (
  `id` int(11) NOT NULL DEFAULT '0',
  `name` char(20) DEFAULT NULL,
  `likes` set('boy','girl','study') DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t2`
--

LOCK TABLES `t2` WRITE;
/*!40000 ALTER TABLE `t2` DISABLE KEYS */;
/*!40000 ALTER TABLE `t2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t3`
--

DROP TABLE IF EXISTS `t3`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t3` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` char(15) DEFAULT NULL,
  `age` tinyint(3) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t3`
--

LOCK TABLES `t3` WRITE;
/*!40000 ALTER TABLE `t3` DISABLE KEYS */;
INSERT INTO `t3` VALUES (1,'xuina',30),(2,'xuid',30),(4,'xfdahf',25);
/*!40000 ALTER TABLE `t3` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tt1`
--

DROP TABLE IF EXISTS `tt1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tt1` (
  `username` char(20) DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  `shell` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tt1`
--

LOCK TABLES `tt1` WRITE;
/*!40000 ALTER TABLE `tt1` DISABLE KEYS */;
INSERT INTO `tt1` VALUES ('root',0,'/bin/bash'),('bin',1,'/sbin/nologin');
/*!40000 ALTER TABLE `tt1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tt2`
--

DROP TABLE IF EXISTS `tt2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tt2` (
  `username` char(20) DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  `gid` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tt2`
--

LOCK TABLES `tt2` WRITE;
/*!40000 ALTER TABLE `tt2` DISABLE KEYS */;
INSERT INTO `tt2` VALUES ('root',0,0),('bin',1,1),('daemon',2,2);
/*!40000 ALTER TABLE `tt2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userinfo`
--

DROP TABLE IF EXISTS `userinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userinfo` (
  `username` char(20) DEFAULT NULL,
  `password` char(1) DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  `gid` int(11) DEFAULT NULL,
  `comment` varchar(50) DEFAULT NULL,
  `homedir` varchar(50) DEFAULT NULL,
  `shell` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userinfo`
--

LOCK TABLES `userinfo` WRITE;
/*!40000 ALTER TABLE `userinfo` DISABLE KEYS */;
INSERT INTO `userinfo` VALUES ('root','x',0,0,'root','/root','/bin/bash'),('bin','x',1,1,'bin','/bin','/sbin/nologin'),('daemon','x',2,2,'daemon','/sbin','/sbin/nologin'),('adm','x',3,4,'adm','/var/adm','/sbin/nologin'),('lp','x',4,7,'lp','/var/spool/lpd','/sbin/nologin'),('sync','x',5,0,'sync','/sbin','/bin/sync'),('shutdown','x',6,0,'shutdown','/sbin','/sbin/shutdown'),('halt','x',7,0,'halt','/sbin','/sbin/halt'),('mail','x',8,12,'mail','/var/spool/mail','/sbin/nologin'),('operator','x',11,0,'operator','/root','/sbin/nologin'),('games','x',12,100,'games','/usr/games','/sbin/nologin'),('ftp','x',14,50,'FTP User','/var/ftp','/sbin/nologin'),('nobody','x',99,99,'Nobody','/','/sbin/nologin'),('systemd-network','x',192,192,'systemd Network Management','/','/sbin/nologin'),('dbus','x',81,81,'System message bus','/','/sbin/nologin'),('polkitd','x',999,997,'User for polkitd','/','/sbin/nologin'),('abrt','x',173,173,'','/etc/abrt','/sbin/nologin'),('libstoragemgmt','x',998,996,'daemon account for libstoragemgmt','/var/run/lsm','/sbin/nologin'),('rpc','x',32,32,'Rpcbind Daemon','/var/lib/rpcbind','/sbin/nologin'),('colord','x',997,995,'User for colord','/var/lib/colord','/sbin/nologin'),('unbound','x',996,993,'Unbound DNS resolver','/etc/unbound','/sbin/nologin'),('saslauth','x',995,76,'Saslauthd user','/run/saslauthd','/sbin/nologin'),('setroubleshoot','x',994,992,'','/var/lib/setroubleshoot','/sbin/nologin'),('rtkit','x',172,172,'RealtimeKit','/proc','/sbin/nologin'),('chrony','x',993,991,'','/var/lib/chrony','/sbin/nologin'),('tss','x',59,59,'Account used by the trousers package to sandbox th','/dev/null','/sbin/nologin'),('usbmuxd','x',113,113,'usbmuxd user','/','/sbin/nologin'),('geoclue','x',992,989,'User for geoclue','/var/lib/geoclue','/sbin/nologin'),('qemu','x',107,107,'qemu user','/','/sbin/nologin'),('rpcuser','x',29,29,'RPC Service User','/var/lib/nfs','/sbin/nologin'),('nfsnobody','x',65534,65534,'Anonymous NFS User','/var/lib/nfs','/sbin/nologin'),('radvd','x',75,75,'radvd user','/','/sbin/nologin'),('pulse','x',171,171,'PulseAudio System Daemon','/var/run/pulse','/sbin/nologin'),('gdm','x',42,42,'','/var/lib/gdm','/sbin/nologin'),('gnome-initial-setup','x',991,986,'','/run/gnome-initial-setup/','/sbin/nologin'),('avahi','x',70,70,'Avahi mDNS/DNS-SD Stack','/var/run/avahi-daemon','/sbin/nologin'),('postfix','x',89,89,'','/var/spool/postfix','/sbin/nologin'),('ntp','x',38,38,'','/etc/ntp','/sbin/nologin'),('sshd','x',74,74,'Privilege-separated SSH','/var/empty/sshd','/sbin/nologin'),('tcpdump','x',72,72,'','/','/sbin/nologin'),('Student','x',1000,1000,'','/home/Student','/bin/bash'),('apache','x',48,48,'Apache','/usr/share/httpd','/sbin/nologin'),('mysql','x',27,27,'MariaDB Server','/var/lib/mysql','/sbin/nologin');
/*!40000 ALTER TABLE `userinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userinfo2`
--

DROP TABLE IF EXISTS `userinfo2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userinfo2` (
  `username` char(20) DEFAULT NULL,
  `password` char(1) DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  `gid` int(11) DEFAULT NULL,
  `comment` varchar(50) DEFAULT NULL,
  `homedir` varchar(50) DEFAULT NULL,
  `shell` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userinfo2`
--

LOCK TABLES `userinfo2` WRITE;
/*!40000 ALTER TABLE `userinfo2` DISABLE KEYS */;
INSERT INTO `userinfo2` VALUES ('root','x',0,0,'root','/root','/bin/bash'),('bin','x',1,1,'bin','/bin','/sbin/nologin'),('daemon','x',2,2,'daemon','/sbin','/sbin/nologin'),('adm','x',3,4,'adm','/var/adm','/sbin/nologin'),('lp','x',4,7,'lp','/var/spool/lpd','/sbin/nologin'),('sync','x',5,0,'sync','/sbin','/bin/sync'),('shutdown','x',6,0,'shutdown','/sbin','/sbin/shutdown'),('halt','x',7,0,'halt','/sbin','/sbin/halt'),('mail','x',8,12,'mail','/var/spool/mail','/sbin/nologin'),('operator','x',11,0,'operator','/root','/sbin/nologin'),('games','x',12,100,'games','/usr/games','/sbin/nologin'),('ftp','x',14,50,'FTP User','/var/ftp','/sbin/nologin'),('nobody','x',99,99,'Nobody','/','/sbin/nologin'),('systemd-network','x',192,192,'systemd Network Management','/','/sbin/nologin'),('dbus','x',81,81,'System message bus','/','/sbin/nologin'),('polkitd','x',999,997,'User for polkitd','/','/sbin/nologin'),('abrt','x',173,173,'','/etc/abrt','/sbin/nologin'),('libstoragemgmt','x',998,996,'daemon account for libstoragemgmt','/var/run/lsm','/sbin/nologin'),('rpc','x',32,32,'Rpcbind Daemon','/var/lib/rpcbind','/sbin/nologin'),('colord','x',997,995,'User for colord','/var/lib/colord','/sbin/nologin'),('unbound','x',996,993,'Unbound DNS resolver','/etc/unbound','/sbin/nologin'),('saslauth','x',995,76,'Saslauthd user','/run/saslauthd','/sbin/nologin'),('setroubleshoot','x',994,992,'','/var/lib/setroubleshoot','/sbin/nologin'),('rtkit','x',172,172,'RealtimeKit','/proc','/sbin/nologin'),('chrony','x',993,991,'','/var/lib/chrony','/sbin/nologin'),('tss','x',59,59,'Account used by the trousers package to sandbox th','/dev/null','/sbin/nologin'),('usbmuxd','x',113,113,'usbmuxd user','/','/sbin/nologin'),('geoclue','x',992,989,'User for geoclue','/var/lib/geoclue','/sbin/nologin'),('qemu','x',107,107,'qemu user','/','/sbin/nologin'),('rpcuser','x',29,29,'RPC Service User','/var/lib/nfs','/sbin/nologin'),('nfsnobody','x',65534,65534,'Anonymous NFS User','/var/lib/nfs','/sbin/nologin'),('radvd','x',75,75,'radvd user','/','/sbin/nologin'),('pulse','x',171,171,'PulseAudio System Daemon','/var/run/pulse','/sbin/nologin'),('gdm','x',42,42,'','/var/lib/gdm','/sbin/nologin'),('gnome-initial-setup','x',991,986,'','/run/gnome-initial-setup/','/sbin/nologin'),('avahi','x',70,70,'Avahi mDNS/DNS-SD Stack','/var/run/avahi-daemon','/sbin/nologin'),('postfix','x',89,89,'','/var/spool/postfix','/sbin/nologin'),('ntp','x',38,38,'','/etc/ntp','/sbin/nologin'),('sshd','x',74,74,'Privilege-separated SSH','/var/empty/sshd','/sbin/nologin'),('tcpdump','x',72,72,'','/','/sbin/nologin'),('Student','x',1000,1000,'','/home/Student','/bin/bash'),('apache','x',48,48,'Apache','/usr/share/httpd','/sbin/nologin'),('mysql','x',27,27,'MariaDB Server','/var/lib/mysql','/sbin/nologin');
/*!40000 ALTER TABLE `userinfo2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userinfo3`
--

DROP TABLE IF EXISTS `userinfo3`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userinfo3` (
  `username` char(20) DEFAULT NULL,
  `password` char(1) DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  `gid` int(11) DEFAULT NULL,
  `comment` varchar(50) DEFAULT NULL,
  `homedir` varchar(50) DEFAULT NULL,
  `shell` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userinfo3`
--

LOCK TABLES `userinfo3` WRITE;
/*!40000 ALTER TABLE `userinfo3` DISABLE KEYS */;
INSERT INTO `userinfo3` VALUES ('root','x',0,0,'root','/root','/bin/bash'),('bin','x',1,1,'bin','/bin','/sbin/nologin'),('daemon','x',2,2,'daemon','/sbin','/sbin/nologin'),('adm','x',3,4,'adm','/var/adm','/sbin/nologin'),('lp','x',4,7,'lp','/var/spool/lpd','/sbin/nologin'),('sync','x',5,0,'sync','/sbin','/bin/sync'),('shutdown','x',6,0,'shutdown','/sbin','/sbin/shutdown'),('halt','x',7,0,'halt','/sbin','/sbin/halt'),('mail','x',8,12,'mail','/var/spool/mail','/sbin/nologin'),('operator','x',11,0,'operator','/root','/sbin/nologin');
/*!40000 ALTER TABLE `userinfo3` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userinfo4`
--

DROP TABLE IF EXISTS `userinfo4`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userinfo4` (
  `username` char(20) DEFAULT NULL,
  `password` char(1) DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  `gid` int(11) DEFAULT NULL,
  `comment` varchar(50) DEFAULT NULL,
  `homedir` varchar(50) DEFAULT NULL,
  `shell` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userinfo4`
--

LOCK TABLES `userinfo4` WRITE;
/*!40000 ALTER TABLE `userinfo4` DISABLE KEYS */;
/*!40000 ALTER TABLE `userinfo4` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `xian`
--

DROP TABLE IF EXISTS `xian`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `xian` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `X_ID` int(11) DEFAULT NULL,
  `X_name` varchar(15) DEFAULT NULL,
  `XFather_ID` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `xian`
--

LOCK TABLES `xian` WRITE;
/*!40000 ALTER TABLE `xian` DISABLE KEYS */;
INSERT INTO `xian` VALUES (1,132100,'河东区',131100),(2,132101,'正定县',131100),(3,132102,'固安县',131102),(4,132102,'香河县',131102),(5,132103,'哈哈',131112);
/*!40000 ALTER TABLE `xian` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-09-13 14:46:43
