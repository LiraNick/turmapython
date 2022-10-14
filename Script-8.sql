CREATE TABLE "produtos"(
    "id" INTEGER NOT NULL,
    "nome" CHAR(255) NOT NULL,
    "cod" INTEGER NOT NULL,
    "categoria" INTEGER NOT NULL
);
ALTER TABLE
    "produtos" ADD PRIMARY KEY("id");
CREATE TABLE "materia_prima"(
    "id" INTEGER NOT NULL,
    "nome" CHAR(255) NOT NULL,
    "tipo" CHAR(255) NOT NULL,
    "fornecedor" CHAR(255) NOT NULL,
    "caracteristica" CHAR(255) NOT NULL,
    "unidade_medida" INTEGER NOT NULL,
    "valor" FLOAT NOT NULL
);
ALTER TABLE
    "materia_prima" ADD PRIMARY KEY("id");
CREATE TABLE "receitas"(
    "id" INTEGER NOT NULL,
    "nome_receita" INTEGER NOT NULL,
    "materia_prima" CHAR(255) NOT NULL,
    "custo" FLOAT NOT NULL
);
ALTER TABLE
    "receitas" ADD PRIMARY KEY("id")
    
alter table receitas 
ADD nome_receitas VARCHAR(60);
    
ALTER TABLE receitas 
DROP nome_receita;

-- Drop table

-- DROP TABLE public.produtos;

CREATE TABLE public.produtos (
	id int4 NOT NULL,
	nome bpchar(255) NOT NULL,
	cod int4 NOT NULL,
	categoria int4 NOT NULL,
	CONSTRAINT produtos_pkey PRIMARY KEY (id)
);

-- Drop table

-- DROP TABLE public.receitas;

CREATE TABLE public.receitas (
	id int4 NOT NULL,
	nome_receita int4 NOT NULL,
	materia_prima bpchar(255) NOT NULL,
	custo float8 NOT NULL,
	CONSTRAINT receitas_pkey PRIMARY KEY (id)
);

-- Drop table

-- DROP TABLE public.materia_prima;

CREATE TABLE public.materia_prima (
	id int4 NOT NULL,
	nome bpchar(255) NOT NULL,
	tipo bpchar(255) NOT NULL,
	fornecedor bpchar(255) NOT NULL,
	caracteristica bpchar(255) NOT NULL,
	unidade_medida int4 NOT NULL,
	valor float8 NOT NULL,
	CONSTRAINT materia_prima_pkey PRIMARY KEY (id)
);
