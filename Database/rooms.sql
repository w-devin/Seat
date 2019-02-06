/*
 Navicat MySQL Data Transfer

 Source Server         : idevin
 Source Server Type    : MySQL
 Source Server Version : 50723
 Source Host           : idevin.cn:3306
 Source Schema         : Seats

 Target Server Type    : MySQL
 Target Server Version : 50723
 File Encoding         : 65001

 Date: 10/09/2018 22:47:12
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for rooms
-- ----------------------------
DROP TABLE IF EXISTS `rooms`;
CREATE TABLE `rooms`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `campus` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `floor` int(11) NULL DEFAULT NULL,
  `seat_counts` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 63 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of rooms
-- ----------------------------
INSERT INTO `rooms` VALUES (8, '第五阅览室北区', '济南大学西校区', 6, 59);
INSERT INTO `rooms` VALUES (9, '第八阅览室北区', '济南大学西校区', 6, 204);
INSERT INTO `rooms` VALUES (11, '第二阅览室北区', '济南大学西校区', 3, 196);
INSERT INTO `rooms` VALUES (12, '第二阅览室中区', '济南大学西校区', 3, 48);
INSERT INTO `rooms` VALUES (13, '第二阅览室南区', '济南大学西校区', 3, 172);
INSERT INTO `rooms` VALUES (14, '第十一阅览室北区', '济南大学西校区', 3, 188);
INSERT INTO `rooms` VALUES (15, '第十一阅览室中区', '济南大学西校区', 3, 48);
INSERT INTO `rooms` VALUES (16, '第十一阅览室南区', '济南大学西校区', 3, 156);
INSERT INTO `rooms` VALUES (17, '第三阅览室北区', '济南大学西校区', 4, 148);
INSERT INTO `rooms` VALUES (18, '第三阅览室中区', '济南大学西校区', 4, 48);
INSERT INTO `rooms` VALUES (19, '第三阅览室南区', '济南大学西校区', 4, 120);
INSERT INTO `rooms` VALUES (21, '第十阅览室中区', '济南大学西校区', 4, 48);
INSERT INTO `rooms` VALUES (22, '第十阅览室南区', '济南大学西校区', 4, 164);
INSERT INTO `rooms` VALUES (23, '第六阅览室北区', '济南大学西校区', 7, 132);
INSERT INTO `rooms` VALUES (24, '第六阅览室中区', '济南大学西校区', 7, 48);
INSERT INTO `rooms` VALUES (25, '第六阅览室南区', '济南大学西校区', 7, 108);
INSERT INTO `rooms` VALUES (27, '第七阅览室中区', '济南大学西校区', 7, 48);
INSERT INTO `rooms` VALUES (28, '第七阅览室南区', '济南大学西校区', 7, 108);
INSERT INTO `rooms` VALUES (31, '第四阅览室北区', '济南大学西校区', 5, 148);
INSERT INTO `rooms` VALUES (32, '第四阅览室中区', '济南大学西校区', 5, 48);
INSERT INTO `rooms` VALUES (33, '第四阅览室南区', '济南大学西校区', 5, 164);
INSERT INTO `rooms` VALUES (34, '第九阅览室北区', '济南大学西校区', 5, 195);
INSERT INTO `rooms` VALUES (35, '第九阅览室中区', '济南大学西校区', 5, 48);
INSERT INTO `rooms` VALUES (36, '第九阅览室南区', '济南大学西校区', 5, 172);
INSERT INTO `rooms` VALUES (37, '第五阅览室南区', '济南大学西校区', 6, 173);
INSERT INTO `rooms` VALUES (38, '第五阅览室中区', '济南大学西校区', 6, 48);
INSERT INTO `rooms` VALUES (40, '第八阅览室南区', '济南大学西校区', 6, 176);
INSERT INTO `rooms` VALUES (41, '第一阅览室', '济南大学西校区', 2, 136);
INSERT INTO `rooms` VALUES (46, '第七阅览室北区', '济南大学西校区', 7, 132);
INSERT INTO `rooms` VALUES (47, '第八阅览室中区', '济南大学西校区', 6, 48);
INSERT INTO `rooms` VALUES (49, '商科特色阅览室（诺奖图书 五楼南）', '济南大学东校区', 5, 212);
INSERT INTO `rooms` VALUES (51, '第一期刊阅览室（现刊 四楼北）', '济南大学东校区', 4, 195);
INSERT INTO `rooms` VALUES (52, '商科专业书库（二楼南）', '济南大学东校区', 2, 60);
INSERT INTO `rooms` VALUES (53, '外文、工具书库（二楼北）', '济南大学东校区', 2, 73);
INSERT INTO `rooms` VALUES (54, '二楼大厅', '济南大学东校区', 2, 29);
INSERT INTO `rooms` VALUES (55, '人文书库（三楼南）', '济南大学东校区', 3, 57);
INSERT INTO `rooms` VALUES (56, '综合书库（三楼北）', '济南大学东校区', 3, 101);
INSERT INTO `rooms` VALUES (57, '第二期刊阅览室（过刊 四楼南）', '济南大学东校区', 4, 194);
INSERT INTO `rooms` VALUES (58, '第三期刊阅览室（赠刊 五楼北）', '济南大学东校区', 5, 104);
INSERT INTO `rooms` VALUES (59, '五楼走廊', '济南大学东校区', 5, 34);
INSERT INTO `rooms` VALUES (60, '信息共享空间（一楼南）', '济南大学东校区', 1, 85);
INSERT INTO `rooms` VALUES (62, '文化展厅（一楼北）', '济南大学东校区', 1, 200);

SET FOREIGN_KEY_CHECKS = 1;
