import numpy as np
import skfuzzy as fuzzy
from skfuzzy import control as ctrl

entF1 = 0
entF2 = 4
entDir = 2
entEsq = 1

# Cria os ANTECEDENTES e CONSEQUENTES
aF1 = ctrl.Antecedent(np.arange(0, 6, 1), "aF1")
aF2 = ctrl.Antecedent(np.arange(0, 6, 1), "aF2")
aDir = ctrl.Antecedent(np.arange(0, 6, 1), "aDir")
aEsq = ctrl.Antecedent(np.arange(0, 6, 1), "aEsq")

rodaD = ctrl.Consequent(np.arange(0, 0.6, 0.1), "rodaD")
rodaE = ctrl.Consequent(np.arange(0, 0.6, 0.1), "rodaE")

# Coloca os valores nos antecedentes e consequentes - plota as funcoes
# SensorF1
aF1['muitoPerto'] = fuzzy.trimf(aF1.universe, [0, 0, 2])
aF1['perto'] = fuzzy.trimf(aF1.universe, [1, 3, 4])
aF1['longe'] = fuzzy.trimf(aF1.universe, [3, 4, 5])

aF1['perto'].view()

# SensorF2
aF2['muitoPerto'] = fuzzy.trimf(aF2.universe, [0, 0, 2])
aF2['perto'] = fuzzy.trimf(aF2.universe, [1, 3, 4])
aF2['longe'] = fuzzy.trimf(aF2.universe, [3, 4, 5])

# SensorDir
aDir['muitoPerto'] = fuzzy.trimf(aDir.universe, [0, 0, 2])
aDir['perto'] = fuzzy.trimf(aDir.universe, [1, 3, 4])
aDir['longe'] = fuzzy.trimf(aDir.universe, [3, 4, 5])

# SensorEsq
aEsq['muitoPerto'] = fuzzy.trimf(aEsq.universe, [0, 0, 2])
aEsq['perto'] = fuzzy.trimf(aEsq.universe, [1, 3, 4])
aEsq['longe'] = fuzzy.trimf(aEsq.universe, [3, 4, 5])

# RodaD
rodaD['para'] = fuzzy.trimf(rodaD.universe, [0, 0, 0.5])
rodaD['gira'] = fuzzy.trimf(rodaD.universe, [0, 0.5, 0.5])

# RodaE
rodaE['para'] = fuzzy.trimf(rodaE.universe, [0, 0, 0.5])
rodaE['gira'] = fuzzy.trimf(rodaE.universe, [0, 0.5, 0.5])

# Regras
r1 = ctrl.Rule(antecedent=aF1['muitoPerto'] or aF2['muitoPerto'],
               consequent=rodaE['para'])
r2 = ctrl.Rule(antecedent=aF1['muitoPerto'] or aF2['muitoPerto'],
               consequent=rodaD['gira'])

r3 = ctrl.Rule(antecedent=aF1['muitoPerto'] or aDir['muitoPerto'],
               consequent=rodaE['para'])
r4 = ctrl.Rule(antecedent=aF1['muitoPerto'] or aDir['muitoPerto'],
               consequent=rodaD['gira'])

r5 = ctrl.Rule(antecedent=aDir['muitoPerto'] or aDir['perto'],
               consequent=rodaE['gira'])
r6 = ctrl.Rule(antecedent=aDir['muitoPerto'] or aDir['perto'],
               consequent=rodaD['gira'])

r7 = ctrl.Rule(antecedent=aF1['longe'] or aF2['longe'],
               consequent=rodaE['gira'])
r8 = ctrl.Rule(antecedent=aF1['longe'] or aF2['longe'],
               consequent=rodaD['gira'])

r9 = ctrl.Rule(aF2['muitoPerto'] or aEsq['muitoPerto'],
               consequent=rodaE['gira'])
r10 = ctrl.Rule(aF2['muitoPerto'] or aEsq['muitoPerto'],
                consequent=rodaD['gira'])

r11 = ctrl.Rule(aEsq['muitoPerto'] or aEsq['perto'],
                consequent=rodaE['gira'])
r12 = ctrl.Rule(aEsq['muitoPerto'] or aEsq['perto'],
                consequent=rodaD['gira'])

# Cria MAQUINA DE INFERENCIA
controleRodas = ctrl.ControlSystem(rules=[r1, r2, r3, r4, r5, r6, r7, r8, r9,
                                          r10, r11, r12])

resultados = ctrl.ControlSystemSimulation(control_system=controleRodas)

# Entrada de dados
resultados.input['aF1'] = entF1
resultados.input['aF2'] = entF2
resultados.input['aDir'] = entDir
resultados.input['aEsq'] = entEsq

# Defuzzificacao
resultados.compute()

#Resultados
print resultados.output['rodaE']
print resultados.output['rodaD']

rodaE.view(sim=resultados)
rodaD.view(sim=resultados)