# Tabla "suscripcion"
INSERT INTO suscripcion VALUES(1, "prueba@gmail.com", "124");
SELECT * from suscripcion;
SELECT * from suscripcion WHERE suscri_id = 1;
UPDATE suscripcion SET Pass = "hola" WHERE suscri_id = 1;

# Tabla "perfil1"
INSERT INTO perfil1 VALUES (1, "Valentino", "Giannico", "Valen", "2003-01-04", "Bajo", "Cordoba", "Verano del 92", "cancion1.mp3", "video1.mp4", "riff1.mp3", "melodia1", "portada1.png", "Futbol, Musica", null, 1);
SELECT * FROM perfil1 WHERE per_1 = 1;
UPDATE perfil1 SET instrumento = "Guitarra" WHERE per_1 = 1;

#Tabla "perfil2"
INSERT INTO perfil2 VALUES("", "Jorge Bustos, Valentino Giannico, Camila Lopez", "Carcel en Llamas", "Valentino", "Giannico", "Valen", "Tan solo, Musica Ligera", 1)
SELECT * from perfil2;
SELECT * from perfil2 WHERE per_2 = 1;
UPDATE perfil2 SET nombreBanda = "Tan Bionica" WHERE per_2 = 1;

#Tabla "per1_per2"
INSERT INTO per1_per2 VALUES (1, 1);
SELECT * from per1_per2 WHERE per_1_2 = 1;
SELECT * from per1_per2 WHERE per_2_1 = 1;

# Tabla "misvideos"
INSERT INTO misvideos VALUES ("", "solista.mp4", "conMiBanda.mp4", "instrumental.mp4", "solo1.mp4, solo2.mp4", "riff1.mp4, riff2.mp4", "arpegio1.mp4", "melodia1.mp4, melodia2.mp4", 1);
SELECT * FROM misvideos WHERE vid_1_1 = 1;
UPDATE misvideos SET instrumental = "instrumentalJazz.mp4";

# Tabla "videos_perfil1"
INSERT INTO videos_perfil1 VALUES (1,1);
SELECT * FROM videos_perfil1 WHERE per_1_4 = 1;

# Tabla "per2_videos"
INSERT INTO per2_videos VALUES (1,1);
SELECT * FROM per2_videos WHERE per_2_2 = 1;

# Tabla "mp3"
INSERT INTO mp3 VALUES("", "solo1.mp3, solo2.mp3", "riff1.mp3, riff2.mp3", "arpegio1.mp3", "melodia1.mp3", 1, 1);
SELECT * FROM mp3 WHERE per_1_3 = 1;

# Tabla "mismp3_perfil1"
INSERT INTO mismp3_perfil1 VALUES (1,(SELECT per_1 FROM perfil1 WHERE nombre="Valentino"));
SELECT * FROM mismp3_perfil1 WHERE Per_1_5 = (SELECT per_1 FROM perfil1 WHERE nombre = "Valentino");

# Tabla "mp3_perfil2"
INSERT INTO mp3_perfil2 VALUES (1, (SELECT per_2 FROM perfil2 WHERE nombre="Valentino"));
SELECT * FROM mp3_perfil2 WHERE per_2_4 = (SELECT per_2 FROM perfil2 WHERE nombre = "Valentino");