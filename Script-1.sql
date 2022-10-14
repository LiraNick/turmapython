--"comentario"

create table lirinhaboladao(
    nome varchar(45) not null
    ,sobrenome varchar(50)not null
    ,idade integer null
);

alter table lirinhaboladao
add column id int not null generated by default as identity


create table funcionarios(
    id int not null generated by default as identity 
    ,nome varchar(45) not null 
    ,sobreNome varchar(50)not null
    ,salario int null 
    ,idade int null 
);


alter table funcionarios
add column CPF int generated always as identity; 

create table cobras(
    pernas int null
    ,olhos int null
    ,vertebrado boolean
    ,ra�a varchar(45) not null
    ,especie varchar(45) not null
    );

create table filmes(
    ator varchar(50)not null
    ,produtora varchar (50) not null
    ,quantidadedetempo int null
    ,EUA boolean
    ,genero varchar(50)not null
    );
    
   drop schema public cascade;

create schema public;

--DML

create table people(
    nome varchar(45) not null
    ,sobrenome varchar(50)not null
    ,idade integer null
);


insert into people(
	nome, 
	sobrenome,
	idade
)

values(
	'nicolau'
	,'boladao'
	,'19'
);

alter table people 
add column id int not null generated by default as identity

update people 
	set 
		sobrenome = 'boladao'
	where id >= 1 and id <= 2