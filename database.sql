-- MySQL dump 10.13  Distrib 8.0.29, for Linux (x86_64)
--
-- Host: std-mysql    Database: std_1611_exam
-- ------------------------------------------------------
-- Server version	5.7.26-0ubuntu0.16.04.1

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
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('a475e5cfb9f5');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `books` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `desc` text NOT NULL,
  `year` year(4) NOT NULL,
  `publisher` varchar(200) NOT NULL,
  `author` varchar(200) NOT NULL,
  `volume` int(11) NOT NULL,
  `rating_sum` int(11) NOT NULL,
  `rating_num` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_books_name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES (16,'Война и мир','«Война́ и мир» (рус. дореф. «Война и миръ») — роман-эпопея Льва Николаевича Толстого, описывающий русское общество в эпоху войн против Наполеона в 1805—1812 годах. Эпилог романа доводит повествование до 1820 года.',1901,'Русский вестник','Лев Толстой',5202,5,1),(17,'Преступление и наказание','Книга из школьной программы, которую трудно понять в нежном подростковом возрасте. Писатель показал двойственность человеческой души, когда черное переплетается с белым. История о Раскольникове, который переживает',2008,'Pocket Book','Федор Михайлович Достоевский',680,0,0),(18,'Луна — суровая хозяйка','На Луне в искусственно созданных городах, которые находятся под поверхностью, живут правонарушители с Земли (Терры), сосланные за уголовные и политические преступления. Их потомки навсегда остаются «лунарями»: в результате физиологических изменений в организме под воздействием низкой гравитации через несколько месяцев пребывания на Луне возврат на Землю становится невозможным — человек не может больше жить в условиях высокой гравитации.\n\nВ тяжелейших условиях физического выживания в отсутствие каких-либо писаных законов на Луне исторически сложились своеобразные традиции. Например, попытка туриста с Земли поцеловать девушку без её разрешения чуть не окончилась для него самосудом. При этом никаких моральных ограничений на любые виды добровольных сексуальных отношений не существует.\n\nЛуна фактически является колонией Земли. Лунная администрация, которая подчиняется Федерации Наций с Земли, по монопольно заниженным ценам покупает у лунарей зерно и продаёт им товары, доставляемые с планеты. С каждым годом разница цен ухудшает положение лунарей — они всё больше залезают в долги.\n\nБольшинство лунарей негативно относятся к колониальной политике земной Федерации Наций по отношению к Луне и Лунной Администрации, как ее представителя. Лунари по возможности избегают сотрудничества с Администрацией, но активно и добровольно сотрудничают между собой. Главным принципом отношений между лунарями является принцип «дарзанебы» (дармовой закуски не бывает). ',2006,'Эксмо','Роберт Хайнлайн',448,4,1),(19,'Пост','Опустошительная война превратила некогда огромную Российскую Федерацию в обитель теней былого могущества, имя которой отныне – Московская империя. Во время гражданской войны за Волгой поднялось восстание против столицы, повлекшее за собой еще больше разрушений и заражение великой реки, где теперь проходят восточные границы угасающей империи.\n\nГраница и железнодорожный мост через Волгу охраняются Ярославским постом. Но от кого необходимо защищаться? Старожилы этих мест уверены: за рекой давно не осталось никого и ничего живого, а мост ведет в никуда. Да если б кто там и был… Как перейти реку, чьи воды превратились в кислоту, от которой не спасает даже противогаз?\n\nИ все же однажды кое-кто сумел это сделать. Он пришел из-за Волги, пересек границу, отделяющую мир мертвых от мира живых. Но… зачем? А главный вопрос: что последует за таинственным пришельцем с той стороны моста?',2020,'StorySide AB','Дмитрий Глуховский',280,0,0),(20,'Билли Саммерс','Билли Саммерс – профессиональный киллер с жестким моральным кодексом: он принимает заказы только на действительно «плохих парней». Но ему, бывшему морпеху, это занятие не по душе, и однажды он решает отойти от дел, чтобы начать новую жизнь. Перед этим Билли предстоит выполнить еще один заказ, который обеспечит ему безбедное существование.\n\nЕго чутье и опыт подсказывают: в этом деле что-то не так и оно не такое простое, как кажется на первый взгляд.\n\nОднако на кону стоят слишком большие деньги.\n\nИ Билли отправляется в тихий провинциальный городок Ред-Блафф и начинает тщательную подготовку к своему последнему выстрелу.\n\nПоследнему ли?..',2021,'АСТ','Стивен Кинг',560,0,0),(21,'Лето волонтёра','Это четвертая часть трилогии про «Измененных». Да, так случается. Мир и персонажи меня не отпустили. История Максима, Дарины и Миланы продолжается.',2022,'Литрес','Сергей Лукьяненко',270,0,0);
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `books_genres`
--

DROP TABLE IF EXISTS `books_genres`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `books_genres` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `book_id` int(11) NOT NULL,
  `genre_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_books_genres_book_id_books` (`book_id`),
  KEY `fk_books_genres_genre_id_genres` (`genre_id`),
  CONSTRAINT `fk_books_genres_book_id_books` FOREIGN KEY (`book_id`) REFERENCES `books` (`id`),
  CONSTRAINT `fk_books_genres_genre_id_genres` FOREIGN KEY (`genre_id`) REFERENCES `genres` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books_genres`
--

LOCK TABLES `books_genres` WRITE;
/*!40000 ALTER TABLE `books_genres` DISABLE KEYS */;
INSERT INTO `books_genres` VALUES (26,16,9),(27,16,5),(28,17,1),(29,17,9),(30,17,8),(31,18,3),(32,19,3),(33,20,10),(34,21,3);
/*!40000 ALTER TABLE `books_genres` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `genres`
--

DROP TABLE IF EXISTS `genres`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `genres` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_genres_name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `genres`
--

LOCK TABLES `genres` WRITE;
/*!40000 ALTER TABLE `genres` DISABLE KEYS */;
INSERT INTO `genres` VALUES (1,'Детектив'),(9,'Драма'),(7,'Комедия'),(6,'Повесть'),(4,'Приключение'),(5,'Роман'),(8,'Трагедия'),(10,'Триллер'),(3,'Фантастика'),(2,'Фэнтэзи');
/*!40000 ALTER TABLE `genres` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `image`
--

DROP TABLE IF EXISTS `image`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `image` (
  `id` varchar(100) NOT NULL,
  `file_name` varchar(100) NOT NULL,
  `mime_type` varchar(100) NOT NULL,
  `md5_hash` varchar(100) NOT NULL,
  `book_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_image_md5_hash` (`md5_hash`),
  KEY `fk_image_book_id_books` (`book_id`),
  CONSTRAINT `fk_image_book_id_books` FOREIGN KEY (`book_id`) REFERENCES `books` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `image`
--

LOCK TABLES `image` WRITE;
/*!40000 ALTER TABLE `image` DISABLE KEYS */;
INSERT INTO `image` VALUES ('26702479-3106-4ebc-be4b-0e2a287a8e94','67385403-sergey-lukyanenko-leto-volontera.jpg','image/jpeg','5f235e85cc47228ea419f5c7b7479ae4',21),('2a154fd3-9ad5-4ba9-a8e4-de0d14f41c89','Prestuplenie-i-nakazanie-kniga-658x1024-3305006557.jpg','image/jpeg','b0da45feaefd0e07240082f6790ad089',17),('3590ac38-94ca-4269-8afe-7d0e4d5116eb','67303161-stiven-king-billi-sammers.jpg','image/jpeg','2ef3d90cf3a24f25b98c349657f6bfe8',20),('3a685573-ea76-408d-a060-6ae1deab8e9d','800px-_._._-___._._._4._.18681-_.jpg','image/jpeg','cb1cb019be711899710143c09876606e',16),('49959ba9-b108-4234-90df-f8c835129a7f','63510758-dmitriy-gluhovskiy-post.jpg','image/jpeg','848a244345f26f6483c13ea08d990013',19),('5f5eed35-2d5f-4b2e-ad68-a14b9b03fefc','b1054dc78fb6d4091a4f7be0b1503c88-quality_70Xresize_1Xallow_enlarge_0Xw_700Xh_0-1771052494.jpg','image/jpeg','61da400aa194fdae53fecd5fe16b4d0a',18);
/*!40000 ALTER TABLE `image` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reviews`
--

DROP TABLE IF EXISTS `reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reviews` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `book_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `rating` int(11) NOT NULL,
  `text` text NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `status_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_reviews_book_id_books` (`book_id`),
  KEY `fk_reviews_user_id_users` (`user_id`),
  KEY `fk_reviews_status_id_statuses` (`status_id`),
  CONSTRAINT `fk_reviews_book_id_books` FOREIGN KEY (`book_id`) REFERENCES `books` (`id`),
  CONSTRAINT `fk_reviews_status_id_statuses` FOREIGN KEY (`status_id`) REFERENCES `statuses` (`id`),
  CONSTRAINT `fk_reviews_user_id_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reviews`
--

LOCK TABLES `reviews` WRITE;
/*!40000 ALTER TABLE `reviews` DISABLE KEYS */;
INSERT INTO `reviews` VALUES (3,16,1,5,'# Отличная книга\nОчень интересно!','2022-06-22 17:22:04',2),(4,18,1,4,'Хорошая фантастика','2022-06-22 18:04:31',2);
/*!40000 ALTER TABLE `reviews` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `desc` text NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_roles_name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` VALUES (1,'user','Common user role'),(2,'admin','Administrator role'),(3,'moder','Moderator role');
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `statuses`
--

DROP TABLE IF EXISTS `statuses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `statuses` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_statuses_name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `statuses`
--

LOCK TABLES `statuses` WRITE;
/*!40000 ALTER TABLE `statuses` DISABLE KEYS */;
INSERT INTO `statuses` VALUES (1,'На рассмотрении'),(2,'Одобрена'),(3,'Отклонена');
/*!40000 ALTER TABLE `statuses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `login` varchar(100) NOT NULL,
  `password_hash` varchar(256) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `middle_name` varchar(100) DEFAULT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `role_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_users_login` (`login`),
  KEY `fk_users_role_id_roles` (`role_id`),
  CONSTRAINT `fk_users_role_id_roles` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'user','pbkdf2:sha256:260000$uTsM3md8Nqq9eD6p$d819b14c28a1eb9012cb81432eb19ca05141d764bce3c5337e71801fe921681b','Иванов','Иван',NULL,'2022-06-16 13:28:16',1),(2,'admin','pbkdf2:sha256:260000$CoqXPxQ8n0wKeKvR$002c84cd0675e3c0d236250d1d6182b27cc9deff6ac370908752b061fd77a48c','Иванов','Сергей',NULL,'2022-06-16 13:30:40',2),(3,'moder','pbkdf2:sha256:260000$4xiv3Xf3c3YMzAMG$137ec0b5f8ecd546d78d95ec79ad717618986212ffa2621a35daf7fb6af10787','Иванов','Георгий',NULL,'2022-06-16 13:31:32',3);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-24 18:17:28
