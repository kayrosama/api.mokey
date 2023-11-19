# ksmflypkg
Courier - inventario de cajas y paquetes

#---------#---------#---------#---------#---------#---------#---------#---------#

El proyecto consiste en crear un API para insertar registros en una base de datos estructurada (MariaDB).
El API tendra los metodos necesarios para realizar un CRUD.

#---------#---------#---------#---------#---------#---------#---------#---------#

Database - MariaDB 10.11.2-MariaDB
Driver - MariaDB Connector/J 3.0.7
Free Universal Database Tool - DBeaver Community - Version 23.1.2.202307091549

#---------#---------#---------#---------#---------#---------#---------#---------#

use mysql ;
select host, user, password, plugin, authentication_string 
  from mysql.user where user in ('kohana','root') ;

flush privileges;
create user 'kohana'@'localhost' identified by 'asteriscos';
create user 'kohana'@'%' identified by 'asteriscos';
flush privileges;
SET PASSWORD FOR 'kohana'@'localhost' = PASSWORD('asteriscos');
SET PASSWORD FOR 'kohana'@'%' = PASSWORD('asteriscos  ');
flush privileges;
grant all privileges on *.* to 'kohana'@'localhost';
grant all privileges on *.* to 'kohana'@'%';
flush privileges;
commit ;
exit;

#---------#---------#---------#---------#---------#---------#---------#---------#

CREATE DATABASE kdb ;
use kdb ;
CREATE TABLE `reg_guia` (
  `idreg` int(11) NOT NULL AUTO_INCREMENT,
  `fecreg` timestamp NOT NULL DEFAULT current_timestamp(),
  `fecmod` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `streg` tinyint(4) NOT NULL DEFAULT 1,
  `stsrc` tinyint(4) NOT NULL DEFAULT 1,
  `stpkg` tinyint(4) NOT NULL DEFAULT 0,
  `stbox` tinyint(4) NOT NULL DEFAULT 0,
  `idgui` bigint(20) NOT NULL DEFAULT uuid_short(),
  `idemp` bigint(20) NOT NULL,
  `emp_razon` varchar(100) DEFAULT NULL,
  `fecguia` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `guia` int(11) NOT NULL,
  `snombres` varchar(50) NOT NULL,
  `sapeuno` varchar(20) NOT NULL,
  `sapedos` varchar(20) NOT NULL,
  `sapetres` varchar(20) NOT NULL,
  `spais` smallint(6) NOT NULL,
  `steluno` bigint(20) NOT NULL,
  `steldos` bigint(20) DEFAULT NULL,
  `dnombres` varchar(50) NOT NULL,
  `dapeuno` varchar(20) NOT NULL,
  `dapedos` varchar(20) NOT NULL,
  `dapetres` varchar(20) NOT NULL,
  `dpais` smallint(6) NOT NULL,
  `dteluno` bigint(20) NOT NULL,
  `dteldos` bigint(20) DEFAULT NULL,
  `ddiruno` varchar(40) DEFAULT NULL,
  `ddirdos` varchar(40) DEFAULT NULL,
  `destado` varchar(5) DEFAULT NULL,
  `dciudad` varchar(30) DEFAULT NULL,
  `dzipcode` int(11) DEFAULT NULL,
  `idgrupo` tinyint(4) DEFAULT NULL,
  `idregion` tinyint(4) DEFAULT NULL,
  `monto` float(10,2) NOT NULL,
  `peso` float(5,2) NOT NULL,
  `productos` varchar(255) NOT NULL,
  `observaciones` varchar(255) NOT NULL,
  PRIMARY KEY (`idreg`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

#---------#---------#---------#---------#---------#---------#---------#---------#

