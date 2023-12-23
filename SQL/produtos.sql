create table produtos (
		prdcode int primary key,
		prdname varchar(50),
		undcode int,
		foreign key (undcode) references unidade_medida(undcode)
		);