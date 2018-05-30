import numpy as np
import vrep
import sys
import time
import funcoes

# Encerra conexoes previas
vrep.simxFinish(-1)

# Faz a conexao com o Vrep
clientID = vrep.simxStart('127.0.0.1', 19999, True, True, 5000, 5)  # Connect to V-REP

# Verifica se a conexao foi efetiva
if clientID != -1:
    print("Conectado ao VRep!!  Obaaaaa!!!")
    vrep.simxAddStatusbarMessage(clientID, "Conexao estabelecida!", operationMode=vrep.simx_opmode_oneshot)

else:
    print("Nao conectado ao VRep!!!")
    sys.exit("Xau!!")

# Instancia manipuladores para os atuadores(rodas) e os sensores
codErro, motorE = vrep.simxGetObjectHandle(clientID, "Pioneer_p3dx_leftMotor",
                                           vrep.simx_opmode_blocking)
codErro, motorD = vrep.simxGetObjectHandle(clientID, "Pioneer_p3dx_rightMotor",
                                           vrep.simx_opmode_blocking)

codErro, sensorFrontal1 = vrep.simxGetObjectHandle(clientID, "Pioneer_p3dx_ultrasonicSensor5",
                                                   vrep.simx_opmode_blocking)
codErro, sensorFrontal2 = vrep.simxGetObjectHandle(clientID, "Pioneer_p3dx_ultrasonicSensor4",
                                                   vrep.simx_opmode_blocking)
codErro, sensorEsq = vrep.simxGetObjectHandle(clientID, "Pioneer_p3dx_ultrasonicSensor1", vrep.simx_opmode_blocking)
codErro, sensorDir = vrep.simxGetObjectHandle(clientID, "Pioneer_p3dx_ultrasonicSensor8", vrep.simx_opmode_blocking)

# Inicializa valores para a velocidade das rodas
codErro = vrep.simxSetJointTargetVelocity(clientID, jointHandle=motorE, targetVelocity=0.5,
                                          operationMode=vrep.simx_opmode_streaming)
codErro = vrep.simxSetJointTargetVelocity(clientID, jointHandle=motorD, targetVelocity=0.5,
                                          operationMode=vrep.simx_opmode_streaming)

# Inicializa leitura dos sensores
returnCode, detectionState, detectedPoint, detectedObjectHandle, detectedSurfaceNormalVector = \
    vrep.simxReadProximitySensor(clientID, sensorHandle=sensorFrontal1,
                                 operationMode=vrep.simx_opmode_streaming)

returnCode, detectionState, detectedPoint, detectedObjectHandle, detectedSurfaceNormalVector = \
    vrep.simxReadProximitySensor(clientID, sensorHandle=sensorFrontal2,
                                 operationMode=vrep.simx_opmode_streaming)
returnCode, detectionState, detectedPoint, detectedObjectHandle, detectedSurfaceNormalVector = \
    vrep.simxReadProximitySensor(clientID, sensorHandle=sensorEsq,
                                 operationMode=vrep.simx_opmode_streaming)

returnCode, detectionState, detectedPoint, detectedObjectHandle, detectedSurfaceNormalVector = \
    vrep.simxReadProximitySensor(clientID, sensorHandle=sensorDir,
                                 operationMode=vrep.simx_opmode_streaming)

# Loop para funcionamento do script
for i in range(0, 10000):

    # Leitura dos sensores
    codF1, detStateF1, detF1, detectedObjectHandleF1, detectedSurfaceNormalVectorF1 = \
        vrep.simxReadProximitySensor(clientID, sensorHandle=sensorFrontal1,
                                     operationMode=vrep.simx_opmode_buffer)

    codF2, detStateF2, detF2, detectedObjectHandleF2, detectedSurfaceNormalVectorF2 = \
        vrep.simxReadProximitySensor(clientID, sensorHandle=sensorFrontal2,
                                     operationMode=vrep.simx_opmode_buffer)

    codEsq, detStateEsq, detEsq, detectedObjectHandleEsq, detectedSurfaceNormalVectorEsq = \
        vrep.simxReadProximitySensor(clientID, sensorHandle=sensorEsq,
                                     operationMode=vrep.simx_opmode_buffer)

    codDir, detStateDir, detDir, detectedObjectHandleDir, detectedSurfaceNormalVectorDir = \
        vrep.simxReadProximitySensor(clientID, sensorHandle=sensorDir,
                                     operationMode=vrep.simx_opmode_buffer)

    # Calcula a norma euclidiana de cada sensor
    distF1 = np.float64(np.linalg.norm(detF1)).item()
    distF2 = np.float64(np.linalg.norm(detF2)).item()
    distEsq = np.float64(np.linalg.norm(detEsq)).item()
    distDir = np.float64(np.linalg.norm(detDir)).item()

    detectados = funcoes.estadoSensores(detStateF1, detStateF2, detStateDir, detStateEsq)

    print detectados

    print "{0:.2f}".format(distF1), "{0:.2f}".format(distF2), "{0:.2f}".format(distDir), "{0:.2f}".format(distEsq)

    # Se os sensores detectarem algum obstaculo
    if detStateF1 == True or detStateF2 == True or detStateEsq == True or detStateDir == True:

        #Faz consulta na logica fuzzy e recebe resultados
        vRodas = funcoes.consultaFuzzy(distF1, distF2, distDir, distEsq)
        print vRodas

        codErro = vrep.simxAddStatusbarMessage(clientID, "Sensor F1 = " + "{0:.2f}".format(distF1) +
                                               " Sensor F2 = " + "{0:.2f}".format(distF2) +
                                               " Sensor Dir = " "{0:.2f}".format(distDir) +
                                               " Sensor Esq = " + "{0:.2f}".format(distF1),
                                               operationMode=vrep.simx_opmode_oneshot)

        codErro = vrep.simxAddStatusbarMessage(clientID,"Vel. Roda Esq = " + "{0:.2f}".format(vRodas[0])
                                               + "Vel. Roda Dir = " + "{0:.2f}".format(vRodas[1]))

        codErro = vrep.simxAddStatusbarMessage(clientID, "Resultado Fuzzy = " + vRodas,
                                     operationMode=vrep.simx_opmode_oneshot)


    time.sleep(0.5)