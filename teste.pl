homem(eric).
homem(daniel).
homem(joao).
homem(jean).
homem(matheus).
homem(thiago).
homem(sergio).

mulher(jeciane).
mulher(erika).
mulher(eliene).
mulher(jeane).
mulher(larissa).
mulher(lanay).
mulher(leticia).
mulher(andreia).

cachorro(luke).
cachorro(billy).
cachorro(flocky).
cachorro(hercules).

pai(jeciane, joao).
pai(jean, joao).
pai(jeane, joao).
mae(jeciane, eliene).
mae(jean, eliene).
mae(jeane, eliene).

pai(larissa, sergio).
pai(lanay, sergio).
pai(leticia, sergio).
mae(larissa, jeane).
mae(lanay, jeane).
mae(leticia, jeane).

pai(matheus, jean).
pai(thiago, jean).
mae(thiago, andreia).
mae(matheus, andreia).

pai(erika, eric).
pai(daniel, eric).
mae(erika, jeciane).
mae(daniel, jeciane).

cachorroDe(luke, eric).
cachorroDe(luke, jeciane).
cachorroDe(billy, jean).
cachorroDe(billy, andreia).
cachorroDe(flocky, jean).
cachorroDe(hercules, sergio).
cachorroDe(hercules, jeane).

marido(jeciane, eric).
marido(eliene, joao).
marido(andreia, jean).
marido(jeane, sergio).

esposa(jean, andreia).
esposa(eric, jeciane).
esposa(joao, eliene).
esposa(sergio, jeane).

filho(X,Y) :- (pai(X,Y); mae(X,Y)),homem(X).
filha(X,Y) :- (pai(X,Y); mae(X,Y)), mulher(X).

irmaos(X,Y) :- (pai(X,Z),pai(Y,Z)) ; (mae(X,Z),mae(Y,Z)).
irmao(X,Y) :- ((pai(X,Z),pai(Y,Z)) ; (mae(X,Z),mae(Y,Z))),homem(X).
irma(X,Y) :- ((pai(X,Z),pai(Y,Z)) ; (mae(X,Z),mae(Y,Z))),mulher(X).

primos(X,Y) :- pai(X,Z), mae(Y,W), irmaos(Z,W).

