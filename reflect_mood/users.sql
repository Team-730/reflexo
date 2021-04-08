--
-- Файл сгенерирован с помощью SQLiteStudio v3.3.2 в Чт апр 8 16:47:27 2021
--
-- Использованная кодировка текста: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Таблица: message
CREATE TABLE message
                      (id, text, date DateTime);
INSERT INTO message (id, text, date) VALUES (1169621316, 'О', '2021-04-08');
INSERT INTO message (id, text, date) VALUES (1169621316, 'О', '2021-04-08');
INSERT INTO message (id, text, date) VALUES (935989323, 'Блин,ну не знаю, сегодня день прошел так себе, мне грустно', '2021-04-08');
INSERT INTO message (id, text, date) VALUES (761561292, 'привет', '2021-04-08');
INSERT INTO message (id, text, date) VALUES (935989323, 'пидор', '2021-04-08');
INSERT INTO message (id, text, date) VALUES (1169621316, 'Destroyer пидор', '2021-04-08');
INSERT INTO message (id, text, date) VALUES (1462191225, 'Ну неплохо неплохо', '2021-04-08');
INSERT INTO message (id, text, date) VALUES (1462191225, 'Уже что то', '2021-04-08');
INSERT INTO message (id, text, date) VALUES (52103825, 'Бот привет', '2021-04-08');
INSERT INTO message (id, text, date) VALUES (1462191225, 'И оно работает', '2021-04-08');
INSERT INTO message (id, text, date) VALUES (1462191225, 'Мне нравится', '2021-04-08');
INSERT INTO message (id, text, date) VALUES (874541471, 'я чувствую себя одиноко', '2021-04-08');
INSERT INTO message (id, text, date) VALUES (874541471, 'ты умер или да', '2021-04-08');
INSERT INTO message (id, text, date) VALUES (874541471, 'ок', '2021-04-08');
INSERT INTO message (id, text, date) VALUES (1169621316, 'Бот пока что ничего не отвечает. Я просто собираю бд. Просьба не спамить. Только то, что запрашивает бот.', '2021-04-08');
INSERT INTO message (id, text, date) VALUES (874541471, '😎😎😎😎🤩🤩🤩🥳🥳🥳', '2021-04-08');
INSERT INTO message (id, text, date) VALUES (771750488, 'Привет', '2021-04-08');
INSERT INTO message (id, text, date) VALUES (771750488, 'Я чувствую страх', '2021-04-08');
INSERT INTO message (id, text, date) VALUES (771750488, 'Бот, мне плохо', '2021-04-08');
INSERT INTO message (id, text, date) VALUES (771750488, 'Бооооооооот', '2021-04-08');
INSERT INTO message (id, text, date) VALUES (769830625, 'П', '2021-04-08');
INSERT INTO message (id, text, date) VALUES (1102235480, 'Биба', '2021-04-08');
INSERT INTO message (id, text, date) VALUES (1102235480, 'Боба', '2021-04-08');
INSERT INTO message (id, text, date) VALUES (769830625, 'Подавленность', '2021-04-08');
INSERT INTO message (id, text, date) VALUES (935989323, 'все зашибись', '2021-04-08');
INSERT INTO message (id, text, date) VALUES (52103825, 'Чувствую себя отлично', '2021-04-08');
INSERT INTO message (id, text, date) VALUES (52103825, 'Хай', '2021-04-08');

-- Таблица: users
CREATE TABLE users
                      (id, color, text, date);
INSERT INTO users (id, color, text, date) VALUES (1169621316, '', '', '2021-04-08');
INSERT INTO users (id, color, text, date) VALUES (935989323, '', '', '2021-04-08');
INSERT INTO users (id, color, text, date) VALUES (1462191225, '', '', '2021-04-08');
INSERT INTO users (id, color, text, date) VALUES (874541471, '', '', '2021-04-08');
INSERT INTO users (id, color, text, date) VALUES (771750488, '', '', '2021-04-08');
INSERT INTO users (id, color, text, date) VALUES (1102235480, '', '', '2021-04-08');
INSERT INTO users (id, color, text, date) VALUES (769830625, '', '', '2021-04-08');
INSERT INTO users (id, color, text, date) VALUES (941882215, '', '', '2021-04-08');
INSERT INTO users (id, color, text, date) VALUES (52103825, '', '', '2021-04-08');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
