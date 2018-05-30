import pyswip

p = pyswip.Prolog()

p.consult("regras.pl")


strConsulta = "controle(X,Y,0.463057556611,0.462818784724,3.57562973659e-34,3.57562973659e-34,1,1,0,1)"

resultado = list(p.query(strConsulta))

temp = resultado

if not temp:
    print "Lista vazia"

velocidades = []

for i in temp:
    velocidades.append(i)

print velocidades
print type(velocidades[0])






