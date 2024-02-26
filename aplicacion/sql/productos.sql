CREATE TABLE productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre varchar(50),
    descripcion varchar(512),
    precio INTEGER,
    existencias INTEGER
);

INSERT INTO productos (nombre, descripcion, precio, existencias)
VALUES ('Laptop Intel', 'Laptop potente', 1500, 30);

