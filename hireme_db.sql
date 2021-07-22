CREATE TABLE `hireme_emp` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `skill` varchar(255) NOT NULL,
  `experience` varchar(255) DEFAULT NULL,
  `gender` varchar(26) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) DEFAULT NULL
  `phone` varchar(16) DEFAULT NULL,
  `address` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

ALTER TABLE `hireme_emp`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `hireme_emp`
 MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;