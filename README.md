# api.mokey
Courier - inventario de cajas y paquetes

#---------#---------#---------#---------#---------#---------#---------#---------#

El proyecto consiste en crear un API para insertar registros en una base de datos estructurada (MariaDB).
El API tendra los metodos necesarios para realizar un CRUD.

#---------#---------#---------#---------#---------#---------#---------#---------#

Database - MariaDB 10.11.2-MariaDB\n
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
CREATE TABLE `base_guia` (
  `regid` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` timestamp NOT NULL DEFAULT current_timestamp(),
  `fechamod` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `streg` tinyint(4) NOT NULL DEFAULT 1,
  `stsrc` tinyint(4) NOT NULL DEFAULT 1,
  `stpkg` tinyint(4) NOT NULL DEFAULT 0,
  `guiuuid` bigint(20) NOT NULL DEFAULT uuid_short(),
  `empresa` tinyint(4) NOT NULL,
  `fecha_guia` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `guia` int(11) NOT NULL,
  `src_nombres` varchar(50) NOT NULL,
  `src_apelluno` varchar(20) NOT NULL,
  `src_apelldos` varchar(20) NOT NULL,
  `src_pais` smallint(6) NOT NULL,
  `src_movil` bigint(20) NOT NULL,
  `dst_nombres` varchar(50) NOT NULL,
  `dst_apelluno` varchar(20) NOT NULL,
  `dst_apelldos` varchar(20) NOT NULL,
  `dst_pais` smallint(6) NOT NULL,
  `dst_movil` bigint(20) NOT NULL,
  `dst_diruno` varchar(40) NOT NULL,
  `dst_dirdos` varchar(40) NOT NULL,
  `dst_ciudad` varchar(5) NOT NULL,
  `dst_zipcode` int(11) NOT NULL,
  `monto` float(10,2) NOT NULL,
  `peso` smallint(6) NOT NULL,
  `productos` varchar(255) NOT NULL,
  `observaciones` varchar(255) NOT NULL,
  PRIMARY KEY (`regid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

#---------#---------#---------#---------#---------#---------#---------#---------#

