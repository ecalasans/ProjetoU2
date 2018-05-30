%controle(Ve, Vd, SensF1, SensF2, SensD, SensE, DetF1 , DetF2, DetDir, DetEsq)

%Quina direita
controle('-0.1','0.5',SensF1, SensF2, SensD,
	SensE, DetF1 ,DetF2, DetDir, DetEsq) :- SensF1 =< 0.5, SensF2 =< 0.5, SensD =< 0.5,
											SensE =\= 0, DetF1 =:= 1, DetF2 =:= 1,
											DetDir =:= 1, DetEsq =:= 0.
controle('-0.3','0.6',SensF1, SensF2, SensD,
	SensE, DetF1 ,DetF2, DetDir, DetEsq) :- SensF1 =< 0.2, SensF2 =\= 0, SensD =< 0.2,
											SensE =\= 0, DetF1 =:= 1, DetF2 =:= 0,
											DetDir =:= 1, DetEsq =:= 0.


%Parede ah frente
controle('0.0','0.5',SensF1, SensF2, SensD,
	SensE, DetF1 ,DetF2, DetDir, DetEsq) :- SensF1 =< 0.5, SensF2 =< 0.5, SensD =\= 0,
											SensE =\= 0, DetF1 =:= 1, DetF2 =:= 1,
											DetDir =:= 0, DetEsq =:= 0.
controle('0.0','0.5',SensF1, SensF2, SensD,
	SensE, DetF1 ,DetF2, DetDir, DetEsq) :- SensF1 =< 0.8, SensF2 =< 0.5, SensD =\= 0,
											SensE =\= 0, DetF1 =:= 1, DetF2 =:= 0,
											DetDir =:= 0, DetEsq =:= 0.

controle('0.5','0.0',SensF1, SensF2, SensD,
	SensE, DetF1 ,DetF2, DetDir, DetEsq) :- SensF1 =\= 0, SensF2 =< 0.8, SensD =\= 0,
											SensE =\= 0, DetF1 =:= 0, DetF2 =:= 1,
											DetDir =:= 0, DetEsq =:= 0.



%Quina esquerda
controle('0.5','0.0',SensF1, SensF2, SensD,
	SensE, DetF1 ,DetF2, DetDir, DetEsq) :- SensF1 =< 0.5, SensF2 =< 0.5, SensD =\= 0,
											SensE =< 0.5, DetF1 =:= 1, DetF2 =:= 1,
											DetDir =:= 0, DetEsq =:= 1.

controle('0.5','-0.3',SensF1, SensF2, SensD,
	SensE, DetF1 ,DetF2, DetDir, DetEsq) :- SensF1 =\= 0, SensF2 =< 0.5, SensD =\= 0,
											SensE < 0.5, DetF1 =:= 0, DetF2 =:= 1,
											DetDir =:= 0, DetEsq =:= 1.
controle('0.5','-0.3',SensF1, SensF2, SensD,
	SensE, DetF1 ,DetF2, DetDir, DetEsq) :- SensF1 =\= 0, SensF2 =< 0.5, SensD =\= 0,
											SensE < 0.2, DetF1 =:= 0, DetF2 =:= 1,
											DetDir =:= 0, DetEsq =:= 1.

%Livre
controle('0.5','0.5',SensF1, SensF2, SensD,
	SensE, DetF1 ,DetF2, DetDir, DetEsq) :- SensF1 =\= 0, SensF2 =\= 0, SensD =\= 0,
											SensE =\= 0, DetF1 =:= 0, DetF2 =:= 0,
											DetDir =:= 0, DetEsq =:= 0.

controle('0.5','0.5',SensF1, SensF2, SensD,
	SensE, DetF1 ,DetF2, DetDir, DetEsq) :- SensF1 =\= 0, SensF2 =\= 0, SensD =\= 0,
											SensE =\= 0, DetF1 =:= 0, DetF2 =:= 0,
											DetDir =:= 1, DetEsq =:= 1.

%Parede ah esquerda
controle('0.5','0.5',SensF1, SensF2, SensD,
	SensE, DetF1 ,DetF2, DetDir, DetEsq) :- SensF1 =\= 0, SensF2 =\= 0, SensD =\= 0,
											SensE < 0.5, DetF1 =:= 0, DetF2 =:= 0,
											DetDir =:= 0, DetEsq =:= 1.

%Parede ah direita
controle('0.5','0.5',SensF1, SensF2, SensD,
	SensE, DetF1 ,DetF2, DetDir, DetEsq) :- SensF1 =\= 0, SensF2 =\= 0, SensD =< 0.5,
											SensE =\= 0, DetF1 =:= 0, DetF2 =:= 0,
											DetDir =:= 1, DetEsq =:= 0.

%Encurralado de frente
controle('0.5','0.0',SensF1, SensF2, SensD,
	SensE, DetF1 ,DetF2, DetDir, DetEsq) :- SensF1 =< 0.5, SensF2 =< 0.5, SensD =< 0.5,
											SensE =< 0.5, DetF1 =:= 1, DetF2 =:= 1,
											DetDir =:= 1, DetEsq =:= 1.

controle('-0.5','0.0',SensF1, SensF2, SensD,
	SensE, DetF1 ,DetF2, DetDir, DetEsq) :- SensF1 =< 0.5, SensF2 =\= 0, SensD =\= 0,
											SensE =\= 0, DetF1 =:= 1, DetF2 =:= 0,
											DetDir =:= 0, DetEsq =:= 0.

%Encurralado de costas
controle('0.5','0.5',SensF1, SensF2, SensD,
	SensE, DetF1 ,DetF2, DetDir, DetEsq) :- SensF1 =\= 0, SensF2 =\= 0, SensD =< 0.5,
											SensE =< 0.5, DetF1 =:= 0, DetF2 =:= 0,
											DetDir =:= 1, DetEsq =:= 1.

%Girando para a esquerda
controle('0.0','0.5',SensF1, SensF2, SensD,
	SensE, DetF1 ,DetF2, DetDir, DetEsq) :- SensF1 =< 0.5, SensF2 =< 0.5, SensD =< 0.5,
											SensE =< 0.5, DetF1 =:= 1; DetF2 =:= 0,
											DetDir =:= 1, DetEsq =:= 0.