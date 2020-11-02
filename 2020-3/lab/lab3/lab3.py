import qiskit
import numpy as np
def inv_media(vetor):
    media = np.mean(vetor)
    for i in range(len(vetor)):
        dist = vetor[i] - media
        vetor[i] = media - dist
    inv_media = vetor
    return inv_media

def qinv_media(n):
    '''
    :param n: número de qubits
    :return: circuit inversão sobre a média
    '''
    q = qiskit.QuantumRegister(n, name = 'q')
    circuito = qiskit.QuantumCircuit(q)

    for i in range(n):
        circuito.h(q[i])

    circuito.h([0,1,2])
    circuito.z([0,1,2])
    circuito.cz(0,1)
    circuito.cz(1,2)
    circuito.h([0,1,2])


    for i in range(n):
        circuito.h(q[i]) 
    circuito.draw()

    print(circuito)
    return circuito

def oraculo_trivial(n, k):
    
    return circuito_oraculo

def grover(oraculo):
    
    return k
