-- phpMyAdmin SQL Dump
-- version 4.0.8
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Dec 05, 2017 at 09:21 AM
-- Server version: 5.7.14-log
-- PHP Version: 5.4.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `0207002620_vef_lokaverkefni`
--

-- --------------------------------------------------------

--
-- Table structure for table `notendur`
--

CREATE TABLE IF NOT EXISTS `notendur` (
  `nafn` varchar(200) DEFAULT NULL,
  `lykilord` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `notendur`
--

INSERT INTO `notendur` (`nafn`, `lykilord`) VALUES
('Bjarki', 'password123'),
('asdasdasd', 'asdasd'),
('asdasd', 'asdasd'),
('bjarki', '1234'),
('kennari', 'kennari');

-- --------------------------------------------------------

--
-- Table structure for table `vorur`
--

CREATE TABLE IF NOT EXISTS `vorur` (
  `nafn` varchar(200) DEFAULT NULL,
  `verd` int(8) DEFAULT NULL,
  `hopur` varchar(200) DEFAULT NULL,
  `lysing` varchar(400) DEFAULT NULL,
  `mynd` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `vorur`
--

INSERT INTO `vorur` (`nafn`, `verd`, `hopur`, `lysing`, `mynd`) VALUES
('Asus GeForce GTX 1050 2GB', 20001, 'skjakort', 'Lítið og nett', 'ASUS-GTX-1050-2GB.jpg'),
('Asus AMD Strix RX 580 OC 8GB', 45674, 'skjakort', 'ASUS AMD er með marga hluti sem AMD er venjulega með.', 'ASU-STRIX-RX-580-8GB.png'),
('Asus STRIX GTX1080 Ti OC 11GB', 134001, 'skjakort', 'ASUS STRIX GTX 1080 er óþarfi fyrir flesta og frekar dýrt', 'ASU-STRIX-GTX-1080Ti-OC-11GB.png'),
('Cooler Master Elite 430', 14995, 'turnkassar', 'þetta hér er kassi og er frá Cooler Master heitir lika Elite 430', 'COOLER-MASTER-ELITE-430.jpg'),
('Corsair Graphite 760T', 47007, 'turnkassar', 'Þessi er frá Corsair og er frekar þykkur, kostar mikið líka.', 'CORSAIR-760T.png'),
('Intel Core i7 7700K', 40000, 'orgjorvi', 'auj hve nett er þessi', 'ITL-I77700K.png'),
('Intel Core i5 8600K', 40002, 'orgjorvi', 'já takk', 'ITL-I58600K.png'),
('Asus Z370F ROG Strix', 35001, 'modurbord', 'litur breytist og blikkar sma', 'ASU-Z370F.jpg');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
