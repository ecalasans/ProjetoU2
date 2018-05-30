import pyswip
import skfuzzy as fuzzy
from skfuzzy import control as ctrl
import numpy as np

#Funcao para converter deteccao booleana em binaria - para usar nas regras do Prolog
def estadoSensores(F1, F2, Dir, Esq):
    entrada = [F1, F2, Dir, Esq]

    saida = []

    for i in entrada:
        if i == True:
            saida.append(1)
        else:
            saida.append(0)

    return saida


def consultaProlog(consulta):
    #Cria objeto Prolog
    p = pyswip.Prolog()

    p.consult("regras.pl")

    #Faz a consulta com o string passado
    resultado = list(p.query(consulta))

    # Cria lista de velocidades das rodas
    velocidades = []


        # Armazena em temp uma lista com os valores do dicionario criado em resultado
    temp = resultado[0]

        # Se houver dados pra retornar
        # Preenche velocidades com os valores da consulta - lembre que Y vem antes de X pelo resultado

    for i in temp.values():
            # Converte o resultado para float pois eh produzido um str
        velocidades.append(float(i))


    return velocidades

def consultaFuzzy(entF1, entF2, entDir, entEsq):
    # Cria os ANTECEDENTES e CONSEQUENTES
    aF1 = ctrl.Antecedent(np.arange(0, 2.1, 0.1), "aF1")
    aF2 = ctrl.Antecedent(np.arange(0, 2.1, 0.1), "aF2")
    aDir = ctrl.Antecedent(np.arange(0, 2.1, 0.1), "aDir")
    aEsq = ctrl.Antecedent(np.arange(0, 2.1, 0.1), "aEsq")

    rodaD = ctrl.Consequent(np.arange(-2, 2.1, 0.1), "rodaD")
    rodaE = ctrl.Consequent(np.arange(-2, 2.1, 0.1), "rodaE")

    # Coloca os valores nos antecedentes e consequentes - plota as funcoes
# SensorF1
    aF1['perto'] = fuzzy.trapmf(aF1.universe, [0, 0, 0.8, 1.2])
    aF1['longe'] = fuzzy.trapmf(aF1.universe, [0.8, 1.2, 2, 2])
        
    # SensorF2
    aF2['perto'] = fuzzy.trapmf(aF2.universe, [0, 0, 0.8, 1.2])
    aF2['longe'] = fuzzy.trapmf(aF2.universe, [0.8, 1.2, 2, 2])
        
    # # SensorDir
    aDir['perto'] = fuzzy.trapmf(aDir.universe, [0, 0, 0.8, 1.2])
    aDir['longe'] = fuzzy.trapmf(aDir.universe, [0.8, 1.2, 2, 2])
    
    # SensorEsq
    aEsq['perto'] = fuzzy.trapmf(aEsq.universe, [0, 0, 0.8, 1.2])
    aEsq['longe'] = fuzzy.trapmf(aEsq.universe, [0.8, 1.2, 2, 2])


    # RodaD
    rodaD['tras'] = fuzzy.trimf(rodaD.universe, [-2, -2, 2])
    rodaD['frente'] = fuzzy.trimf(rodaD.universe, [-2, 2, 2])
    #rodaD['tras'].view()

    # RodaE
    rodaE['tras'] = fuzzy.trimf(rodaE.universe, [-2, -2, 2])
    rodaE['frente'] = fuzzy.trimf(rodaE.universe, [-2, 2, 2])

    # Regras
    r1 = ctrl.Rule(antecedent=aF1['perto'] & aF2['perto'],
                   consequent=rodaE['frente'])
    r2 = ctrl.Rule(antecedent=aF1['perto'] & aF2['perto'],
                   consequent=rodaD['tras'])

    r3 = ctrl.Rule(antecedent=aF1['perto'] & aDir['perto'],
                   consequent=rodaE['tras'])
    r4 = ctrl.Rule(antecedent=aF1['perto'] & aDir['perto'],
                   consequent=rodaD['frente'])

    r5 = ctrl.Rule(antecedent=aDir['perto'],
                   consequent=rodaE['frente'])
    r6 = ctrl.Rule(antecedent=aDir['perto'],
                   consequent=rodaD['frente'])

    r7 = ctrl.Rule(antecedent=aEsq['perto'],
                   consequent=rodaE['frente'])
    r8 = ctrl.Rule(antecedent=aEsq['perto'],
                   consequent=rodaD['frente'])

    r9 = ctrl.Rule(antecedent=aF1['longe'] & aF2['longe'],
                   consequent=rodaE['frente'])
    r10 = ctrl.Rule(antecedent=aF1['longe'] & aF2['longe'],
                    consequent=rodaD['frente'])

    r11 = ctrl.Rule(antecedent=aF2['perto'] & aEsq['perto'],
                    consequent=rodaE['frente'])
    r12 = ctrl.Rule(antecedent=aF2['perto'] & aEsq['perto'],
                    consequent=rodaD['tras'])

    # r13 = ctrl.Rule(antecedent=aDir['perto'] & aEsq['perto'],
    #                 consequent=rodaE['frente'])
    # r14 = ctrl.Rule(antecedent=aDir['perto'] & aEsq['perto'],
    #                 consequent=rodaD['frente'])

    r15 = ctrl.Rule(antecedent=aF1['longe'] & aF2['longe'] & aDir['perto'],
                    consequent=rodaE['frente'])
    r16 = ctrl.Rule(antecedent=aF1['longe'] & aF2['longe'] & aDir['perto'],
                    consequent=rodaD['frente'])

    r17 = ctrl.Rule(antecedent=aF1['longe'] & aF2['longe'] & aEsq['perto'],
                    consequent=rodaE['frente'])
    r18 = ctrl.Rule(antecedent=aF1['longe'] & aF2['longe'] & aEsq['perto'],
                    consequent=rodaD['frente'])

    r19 = ctrl.Rule(antecedent=aF1['perto'] & aF2['perto'] & aDir['perto'],
                    consequent=rodaE['tras'])
    r20 = ctrl.Rule(antecedent=aF1['perto'] & aF2['perto'] & aDir['perto'],
                    consequent=rodaD['frente'])

    r21 = ctrl.Rule(antecedent=aF1['perto'] & aF2['perto'] & aEsq['perto'],
                    consequent=rodaE['frente'])
    r22 = ctrl.Rule(antecedent=aF1['perto'] & aF2['perto'] & aEsq['perto'],
                    consequent=rodaD['tras'])

    # r23 = ctrl.Rule(antecedent=aF1['longe'] & aF2['longe'],
    #                consequent=rodaE['frente'])
    # r24 = ctrl.Rule(antecedent=aF1['longe'] & aF2['longe'],
    #                consequent=rodaD['frente'])
    #
    # r25 = ctrl.Rule(antecedent=aF1['longe'] & aDir['longe'],
    #                consequent=rodaE['frente'])
    # r26 = ctrl.Rule(antecedent=aF1['longe'] & aDir['longe'],
    #                consequent=rodaD['frente'])

    # r27 = ctrl.Rule(antecedent=aDir['perto'] & aEsq['perto'],
    #                 consequent=rodaE['frente'])
    # r28 = ctrl.Rule(antecedent=aDir['perto'] & aEsq['perto'],
    #                 consequent=rodaD['frente'])

    r29 = ctrl.Rule(antecedent=aF1['perto'] & aF2['perto'] & aDir['longe'],
                    consequent=rodaE['frente'])
    r30 = ctrl.Rule(antecedent=aF1['longe'] & aF2['longe'] & aDir['longe'],
                    consequent=rodaD['frente'])

    r31 = ctrl.Rule(antecedent=aF1['perto'] & aF2['perto'] & aEsq['longe'],
                    consequent=rodaE['frente'])
    r32 = ctrl.Rule(antecedent=aF1['longe'] & aF2['longe'] & aEsq['longe'],
                    consequent=rodaD['frente'])



    # Cria MAQUINA DE INFERENCIA
    controleRodas = ctrl.ControlSystem([r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11,
                                        r12,  r15, r16, r17, r18, r19, r20,
                                        r21, r22,  r29,
                                        r30, r31, r32])

    resultados = ctrl.ControlSystemSimulation(control_system=controleRodas)

    # Entrada de dados
    resultados.input['aF1'] = entF1
    resultados.input['aF2'] = entF2
    resultados.input['aDir'] = entDir
    resultados.input['aEsq'] = entEsq

    # Defuzzificacao
    resultados.compute()

    vRodas = [resultados.output['rodaE'], resultados.output['rodaD']]

    return vRodas


