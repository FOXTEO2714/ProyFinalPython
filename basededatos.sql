create database tareaspython;

use tareaspython;

drop table tareas;


CREATE  TABLE tareas IF NOT EXISTS  (
	id int auto_increment primary key,
    descripcion varchar(150) not null,
    fecha timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    usuario varchar(150) not null,
    estado varchar(150)
);

drop table tareas;



insert into tareas values(null, 'tarea1', now(), 'Jose Aley', 'activa')

alter table tareas modify fecha timestamp not null;

truncate table tareas;

select * from tareas; 