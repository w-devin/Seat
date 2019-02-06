/*
Navicat MySQL Data Transfer

Source Server         : idevin
Source Server Version : 50723
Source Host           : idevin.cn:3306
Source Database       : Seats

Target Server Type    : MYSQL
Target Server Version : 50723
File Encoding         : 65001

Date: 2018-09-11 19:35:12
*/

SET FOREIGN_KEY_CHECKS=0;
-- ---------------------------
-- Table structure for `tasks`
-- ----------------------------
DROP TABLE IF EXISTS `tasks`;
CREATE TABLE `tasks` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `start` varchar(255) DEFAULT NULL,
  `end` varchar(255) DEFAULT NULL,
  `seat` int(11) DEFAULT NULL,
  `remark` text,
  `creator_id` int(11) DEFAULT NULL,
  `auto_checkin` int(2) DEFAULT '1',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=141 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;
