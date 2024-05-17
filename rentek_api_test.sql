/*
 Navicat Premium Data Transfer

 Source Server         : local
 Source Server Type    : MySQL
 Source Server Version : 100422 (10.4.22-MariaDB)
 Source Host           : localhost:3306
 Source Schema         : rentek_api_test

 Target Server Type    : MySQL
 Target Server Version : 100422 (10.4.22-MariaDB)
 File Encoding         : 65001

 Date: 16/05/2024 19:27:09
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for persona
-- ----------------------------
DROP TABLE IF EXISTS `persona`;
CREATE TABLE `persona`  (
  `idpersona` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `last_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `dni` int NOT NULL,
  PRIMARY KEY (`idpersona`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 17 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of persona
-- ----------------------------
INSERT INTO `persona` VALUES (1, 'Juan', 'Jara', 32564);
INSERT INTO `persona` VALUES (2, 'luis', 'niño', 2147483647);
INSERT INTO `persona` VALUES (3, 'jota', 'jota', 489);
INSERT INTO `persona` VALUES (5, 'pepe', 'perez', 2147483647);
INSERT INTO `persona` VALUES (6, 'pepe', 'perez', 2147483647);
INSERT INTO `persona` VALUES (7, 'pepe', 'perez', 2147483647);
INSERT INTO `persona` VALUES (8, 'pepe', 'perez', 2147483647);
INSERT INTO `persona` VALUES (9, 'pepe', 'perez', 2147483647);
INSERT INTO `persona` VALUES (10, 'pepe', 'perez', 2147483647);
INSERT INTO `persona` VALUES (16, 'pepe', 'perez', 213647);

-- ----------------------------
-- Table structure for tasks
-- ----------------------------
DROP TABLE IF EXISTS `tasks`;
CREATE TABLE `tasks`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `description_task` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  `created_date` datetime NULL DEFAULT NULL,
  `due_date` date NULL DEFAULT NULL,
  `persona_id` int NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `fk_persona_id`(`persona_id` ASC) USING BTREE,
  CONSTRAINT `fk_persona_id` FOREIGN KEY (`persona_id`) REFERENCES `persona` (`idpersona`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of tasks
-- ----------------------------
INSERT INTO `tasks` VALUES (1, 'hola', '2024-05-16 19:09:00', '2024-05-20', 1);
INSERT INTO `tasks` VALUES (2, 'hola', '2024-05-16 19:09:00', '2024-05-20', 1);
INSERT INTO `tasks` VALUES (3, 'Presentar ', NULL, '2024-05-20', 1);
INSERT INTO `tasks` VALUES (4, 'Presentar ', '2024-05-16 19:14:41', '2024-05-20', 1);
INSERT INTO `tasks` VALUES (5, 'Presentar Api a camilo pinilla ', '2024-05-16 19:16:32', '2024-05-17', 1);

SET FOREIGN_KEY_CHECKS = 1;
