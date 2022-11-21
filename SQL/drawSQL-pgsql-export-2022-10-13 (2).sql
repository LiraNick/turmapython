CREATE TABLE "produtos"(
    "id" INTEGER NOT NULL,
    "nome" CHAR(255) NOT NULL,
    "cod" INTEGER NOT NULL,
    "id_categorias" CHAR(255) NOT NULL,
    "preco_venda" DOUBLE PRECISION NOT NULL,
    "id_receitas" INTEGER NOT NULL
);
ALTER TABLE
    "produtos" ADD PRIMARY KEY("id");
CREATE TABLE "materia_prima"(
    "id" INTEGER NOT NULL,
    "nome" CHAR(255) NOT NULL,
    "unidade_medida" CHAR(255) NOT NULL,
    "valor_total" DOUBLE PRECISION NOT NULL
);
ALTER TABLE
    "materia_prima" ADD PRIMARY KEY("id");
CREATE TABLE "receitas"(
    "id" INTEGER NOT NULL,
    "nome_receita" CHAR(255) NOT NULL,
    "custo" DOUBLE PRECISION NOT NULL,
    "id_elementos" INTEGER NOT NULL
);
ALTER TABLE
    "receitas" ADD PRIMARY KEY("id");
CREATE TABLE "pedido"(
    "id" INTEGER NOT NULL,
    "cliente" CHAR(255) NOT NULL,
    "id_produtos" CHAR(255) NOT NULL,
    "soma_custo" DOUBLE PRECISION NOT NULL,
    "total_receita_r" DOUBLE PRECISION NOT NULL,
    "soma_preco_v" DOUBLE PRECISION NOT NULL
);
ALTER TABLE
    "pedido" ADD PRIMARY KEY("id");
CREATE TABLE "categoria"(
    "id" INTEGER NOT NULL,
    "nome" CHAR(255) NOT NULL,
    "tag" CHAR(255) NOT NULL
);
ALTER TABLE
    "categoria" ADD PRIMARY KEY("id");
CREATE TABLE "Custo de produto"();
CREATE TABLE "elementos"(
    "id" INTEGER NOT NULL,
    "id_materia_prima" INTEGER NOT NULL,
    "id_receitas" INTEGER NOT NULL,
    "quantidade" DOUBLE PRECISION NOT NULL
);
ALTER TABLE
    "elementos" ADD PRIMARY KEY("id");
ALTER TABLE
    "produtos" ADD CONSTRAINT "id_receitas" FOREIGN KEY("id_receitas") REFERENCES "receitas"("id");
ALTER TABLE
    "receitas" ADD CONSTRAINT "id_elementos" FOREIGN KEY("id_elementos") REFERENCES "materia_prima"("id");
ALTER TABLE
    "pedido" ADD CONSTRAINT "id_produtos" FOREIGN KEY("id_produtos") REFERENCES "produtos"("id");
ALTER TABLE
    "produtos" ADD CONSTRAINT "id_categorias" FOREIGN KEY("id_categorias") REFERENCES "categoria"("id");
ALTER TABLE
    "elementos" ADD CONSTRAINT "id_materia_prima" FOREIGN KEY("id_materia_prima") REFERENCES "materia_prima"("id");
ALTER TABLE
    "elementos" ADD CONSTRAINT "id_receitas" FOREIGN KEY("id_receitas") REFERENCES "receitas"("id");