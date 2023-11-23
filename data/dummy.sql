#
# TABLE STRUCTURE FOR: books
#

DROP TABLE IF EXISTS `books`;

CREATE TABLE `books` (
  `book_id` int(11) NOT NULL,
  `title` varchar(255) DEFAULT NULL,
  `author` varchar(255) DEFAULT NULL,
  `publication_year` int(11) DEFAULT NULL,
  `isbn` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`book_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `books` (`book_id`, `title`, `author`, `publication_year`, `isbn`) VALUES (4, 'Nesciunt commodi ratione illum rerum.', 'Dr. Marques Jenkins DDS', 2018, 'smij');
INSERT INTO `books` (`book_id`, `title`, `author`, `publication_year`, `isbn`) VALUES (6, 'Maiores numquam laudantium qui soluta.', 'Vanessa Johnson', 2001, 'tsys');
INSERT INTO `books` (`book_id`, `title`, `author`, `publication_year`, `isbn`) VALUES (9, 'Sed consequatur qui est magnam sequi autem ducimus.', 'Rhianna Sipes', 2021, 'cskh');
INSERT INTO `books` (`book_id`, `title`, `author`, `publication_year`, `isbn`) VALUES (10, 'Amet laudantium repellat odit maxime molestiae nulla voluptas.', 'Drake Hagenes', 1998, 'pelb');
INSERT INTO `books` (`book_id`, `title`, `author`, `publication_year`, `isbn`) VALUES (13, 'Mollitia quia veritatis pariatur consequatur et.', 'Miss Luz Crooks', 1971, 'wcex');
INSERT INTO `books` (`book_id`, `title`, `author`, `publication_year`, `isbn`) VALUES (17, 'Est suscipit aperiam recusandae consequatur.', 'Mrs. Joanny Fahey', 2002, 'qnyy');
INSERT INTO `books` (`book_id`, `title`, `author`, `publication_year`, `isbn`) VALUES (25, 'Nesciunt ut odit cumque fugit.', 'Chris Keeling', 1987, 'nglp');
INSERT INTO `books` (`book_id`, `title`, `author`, `publication_year`, `isbn`) VALUES (29, 'Cumque dolorem distinctio ducimus iure non impedit ut.', 'Ladarius Moore', 1984, 'ctmw');
INSERT INTO `books` (`book_id`, `title`, `author`, `publication_year`, `isbn`) VALUES (48, 'Quia totam laboriosam sed ut nemo dolores laudantium.', 'Cody Hartmann DVM', 1992, 'umob');
INSERT INTO `books` (`book_id`, `title`, `author`, `publication_year`, `isbn`) VALUES (50, 'Aspernatur placeat quidem cum doloribus.', 'Lamar Feest', 2009, 'hvmq');
INSERT INTO `books` (`book_id`, `title`, `author`, `publication_year`, `isbn`) VALUES (56, 'Eveniet aliquam tenetur id laudantium at esse.', 'Ahmed Torphy', 1974, 'flgr');
INSERT INTO `books` (`book_id`, `title`, `author`, `publication_year`, `isbn`) VALUES (58, 'Quaerat quae nemo nisi.', 'Prof. Patsy Graham I', 2012, 'efjh');
INSERT INTO `books` (`book_id`, `title`, `author`, `publication_year`, `isbn`) VALUES (64, 'Sint alias consequatur accusantium repellat itaque.', 'Dr. Payton Treutel', 2017, 'vooa');
INSERT INTO `books` (`book_id`, `title`, `author`, `publication_year`, `isbn`) VALUES (69, 'Aperiam commodi voluptas eveniet soluta.', 'Mr. Mikel Kshlerin DDS', 2016, 'pntc');
INSERT INTO `books` (`book_id`, `title`, `author`, `publication_year`, `isbn`) VALUES (82, 'Facilis culpa excepturi soluta velit eligendi recusandae.', 'Micaela Pfeffer DDS', 1980, 'tfkf');
INSERT INTO `books` (`book_id`, `title`, `author`, `publication_year`, `isbn`) VALUES (84, 'Est provident ut iure ut velit.', 'Una Renner', 1970, 'lpnd');
INSERT INTO `books` (`book_id`, `title`, `author`, `publication_year`, `isbn`) VALUES (86, 'Deleniti voluptatem in numquam numquam.', 'Izaiah Hilll MD', 1980, 'ebhc');
INSERT INTO `books` (`book_id`, `title`, `author`, `publication_year`, `isbn`) VALUES (90, 'Eum architecto dignissimos et ut autem voluptas.', 'Mr. Benjamin Huel DVM', 2020, '0-1417-6042-7');
INSERT INTO `books` (`book_id`, `title`, `author`, `publication_year`, `isbn`) VALUES (96, 'Iste repellat qui dicta aliquid.', 'Dr. Dillan Lockman', 2020, '0-1384-3027-6');
INSERT INTO `books` (`book_id`, `title`, `author`, `publication_year`, `isbn`) VALUES (97, 'Aut ut iusto velit non rerum.', 'Mr. Kenneth Bashirian MD', 2020, '0-7642-8382-0');


#
# TABLE STRUCTURE FOR: borrowed_books
#

DROP TABLE IF EXISTS `borrowed_books`;

CREATE TABLE `borrowed_books` (
  `borrow_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `book_id` int(11) DEFAULT NULL,
  `borrow_date` date DEFAULT NULL,
  `return_date` date DEFAULT NULL,
  PRIMARY KEY (`borrow_id`),
  KEY `user_id` (`user_id`),
  KEY `book_id` (`book_id`),
  CONSTRAINT `borrowed_books_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`),
  CONSTRAINT `borrowed_books_ibfk_2` FOREIGN KEY (`book_id`) REFERENCES `books` (`book_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `borrowed_books` (`borrow_id`, `user_id`, `book_id`, `borrow_date`, `return_date`) VALUES (0, 4628538, 10, '2022-04-09', '2022-04-28');
INSERT INTO `borrowed_books` (`borrow_id`, `user_id`, `book_id`, `borrow_date`, `return_date`) VALUES (1, 88270203, 10, '2022-04-25', '2022-12-11');
INSERT INTO `borrowed_books` (`borrow_id`, `user_id`, `book_id`, `borrow_date`, `return_date`) VALUES (6, 88270203, 58, '2022-05-28', '2022-06-25');
INSERT INTO `borrowed_books` (`borrow_id`, `user_id`, `book_id`, `borrow_date`, `return_date`) VALUES (8, 53572776, 10, '2022-07-28', '2022-08-05');
INSERT INTO `borrowed_books` (`borrow_id`, `user_id`, `book_id`, `borrow_date`, `return_date`) VALUES (9, 2023748, 10, '2022-02-19', '2022-03-14');
INSERT INTO `borrowed_books` (`borrow_id`, `user_id`, `book_id`, `borrow_date`, `return_date`) VALUES (19, 19173054, 10, '2022-01-04', '2022-01-13');
INSERT INTO `borrowed_books` (`borrow_id`, `user_id`, `book_id`, `borrow_date`, `return_date`) VALUES (97, 88270203, 90, '2022-07-19', '2022-08-17');
INSERT INTO `borrowed_books` (`borrow_id`, `user_id`, `book_id`, `borrow_date`, `return_date`) VALUES (310, 2990996, 97, '2022-09-19', '2022-10-02');
INSERT INTO `borrowed_books` (`borrow_id`, `user_id`, `book_id`, `borrow_date`, `return_date`) VALUES (500, 38347870, 90, '2022-06-02', '2022-07-05');
INSERT INTO `borrowed_books` (`borrow_id`, `user_id`, `book_id`, `borrow_date`, `return_date`) VALUES (805, 96925225, 4, '2022-05-22', '2022-06-09');
INSERT INTO `borrowed_books` (`borrow_id`, `user_id`, `book_id`, `borrow_date`, `return_date`) VALUES (6533, 4628538, 6, '2022-08-14', '2022-09-03');
INSERT INTO `borrowed_books` (`borrow_id`, `user_id`, `book_id`, `borrow_date`, `return_date`) VALUES (8547, 40576510, 13, '2022-07-01', '2022-06-27');
INSERT INTO `borrowed_books` (`borrow_id`, `user_id`, `book_id`, `borrow_date`, `return_date`) VALUES (20877, 28691365, 90, '2022-12-04', '2022-12-21');
INSERT INTO `borrowed_books` (`borrow_id`, `user_id`, `book_id`, `borrow_date`, `return_date`) VALUES (20878, 95118284, 13, '2022-10-15', '2022-10-16');
INSERT INTO `borrowed_books` (`borrow_id`, `user_id`, `book_id`, `borrow_date`, `return_date`) VALUES (20879, 4628538, 13, '2022-10-15', NULL);
INSERT INTO `borrowed_books` (`borrow_id`, `user_id`, `book_id`, `borrow_date`, `return_date`) VALUES (20880, 96925225, 13, '2022-10-15', NULL);

#
# TABLE STRUCTURE FOR: users
#

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `registration_date` date DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `users` (`user_id`, `first_name`, `last_name`, `email`, `registration_date`) VALUES (1191769, 'Weston', 'Osinski', 'elyse00@example.com', '1999-03-17');
INSERT INTO `users` (`user_id`, `first_name`, `last_name`, `email`, `registration_date`) VALUES (2023748, 'Hudson', 'Daugherty', 'xromaguera@example.org', '1975-05-14');
INSERT INTO `users` (`user_id`, `first_name`, `last_name`, `email`, `registration_date`) VALUES (2990996, 'Bernhard', 'Corkery', 'schowalter.madalyn@example.net', '2019-04-28');
INSERT INTO `users` (`user_id`, `first_name`, `last_name`, `email`, `registration_date`) VALUES (4628538, 'Isaiah', 'Keeling', 'sonia87@example.net', '1987-10-07');
INSERT INTO `users` (`user_id`, `first_name`, `last_name`, `email`, `registration_date`) VALUES (4914839, 'Elenor', 'Erdman', 'bskiles@example.org', '1989-02-10');
INSERT INTO `users` (`user_id`, `first_name`, `last_name`, `email`, `registration_date`) VALUES (17608084, 'Freeda', 'Rosenbaum', 'abbott.francesco@example.org', '1974-11-20');
INSERT INTO `users` (`user_id`, `first_name`, `last_name`, `email`, `registration_date`) VALUES (19173054, 'Imelda', 'Moore', 'rath.roosevelt@example.net', '1982-07-01');
INSERT INTO `users` (`user_id`, `first_name`, `last_name`, `email`, `registration_date`) VALUES (21321221, 'Don', 'Willms', 'beier.jayme@example.net', '1976-05-21');
INSERT INTO `users` (`user_id`, `first_name`, `last_name`, `email`, `registration_date`) VALUES (23606005, 'Caitlyn', 'Ritchie', 'josiah54@example.com', '1978-09-07');
INSERT INTO `users` (`user_id`, `first_name`, `last_name`, `email`, `registration_date`) VALUES (28691365, 'Louisa', 'Crona', 'warren.gutkowski@example.org', '2006-08-02');
INSERT INTO `users` (`user_id`, `first_name`, `last_name`, `email`, `registration_date`) VALUES (38347870, 'Colby', 'Wisozk', 'garrick89@example.com', '2011-04-21');
INSERT INTO `users` (`user_id`, `first_name`, `last_name`, `email`, `registration_date`) VALUES (40576510, 'Nikki', 'Rosenbaum', 'kkeeling@example.org', '1971-03-19');
INSERT INTO `users` (`user_id`, `first_name`, `last_name`, `email`, `registration_date`) VALUES (43076253, 'Jerrod', 'Parker', 'ecronin@example.net', '1986-09-27');
INSERT INTO `users` (`user_id`, `first_name`, `last_name`, `email`, `registration_date`) VALUES (50522491, 'Keira', 'Wolff', 'giuseppe24@example.net', '1981-09-04');
INSERT INTO `users` (`user_id`, `first_name`, `last_name`, `email`, `registration_date`) VALUES (52207709, 'Ozella', 'Harris', 'zyundt@example.org', '2020-10-11');
INSERT INTO `users` (`user_id`, `first_name`, `last_name`, `email`, `registration_date`) VALUES (53572776, 'Rowena', 'Blanda', 'natasha11@example.org', '1976-03-28');
INSERT INTO `users` (`user_id`, `first_name`, `last_name`, `email`, `registration_date`) VALUES (88270203, 'Karley', 'Keefe', 'frances04@example.org', '2015-01-29');
INSERT INTO `users` (`user_id`, `first_name`, `last_name`, `email`, `registration_date`) VALUES (95118284, 'Zackery', 'Satterfield', 'ortiz.lance@example.com', '1974-08-01');
INSERT INTO `users` (`user_id`, `first_name`, `last_name`, `email`, `registration_date`) VALUES (96925225, 'David', 'Abernathy', 'bernier.devin@example.net', '1975-06-18');
INSERT INTO `users` (`user_id`, `first_name`, `last_name`, `email`, `registration_date`) VALUES (99324490, 'Therese', 'Schultz', 'rasheed93@example.org', '2022-08-22');