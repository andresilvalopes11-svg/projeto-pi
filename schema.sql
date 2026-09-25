
/*
CREATE TABLE espaco (
    id integer PRIMARY KEY AUTOINCREMENT,
    nome varchar(100) NOT NULL,
    tipo varchar(50) NOT NULL,
    capacidade integer NOT NULL,
    bloco varchar(50) NOT NULL,
    icone varchar(10)
);

INSERT INTO espaco (nome, tipo, capacidade, bloco, icone)
VALUES ('Lab. Informática 2', 'Laboratório', 30, 'B', '💻'),
       ('Lab. Ciências', 'Laboratório', 25, 'A', '🔬'),
       ('Sala 104', 'Sala de aula', 38, 'C', '📚'),
       ('Auditório', 'Auditório', 120, 'Principal', '🎤'),
       ('Sala de Vídeo', 'Multimídia', 40, 'B', '🎬'),
       ('Sala de Reunião', 'Reunião', 12, 'A', '👥');
*/


CREATE TABLE reserva (
    id integer PRIMARY KEY AUTOINCREMENT,
    data DATE,
    hora_inicio TIME,
    hora_fim TIME,
    id_espaco integer,
    foreign KEY (id_espaco) references espaco(id)
);

INSERT INTO reserva (data, hora_inicio, hora_fim, id_espaco)
VALUES ('2026-09-23', '08:30', '10:00', 1),
       ('2026-07-14', '11:30', '13:00', 2);

