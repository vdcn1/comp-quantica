import qiskit
import numpy as np
from qiskit.circuit.library.standard_gates import ZGate

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

    for qu in range(n):
        circuito.h(qu)

    for qu in range(n):
        circuito.x(qu)
    
    circuito.h(n-1)
    circuito.mct(list(range(n-1)), n-1)  # multi-controlled-toffoli
    circuito.h(n-1)

    for qu in range(n):
        circuito.x(qu)

    for qu in range(n):
        circuito.h(qu)
    #0,1,2,3,4,5,6,7
    #p/ n = 3
    #0
    #1,2,3,4,5,6,7

    print(circuito)
    return circuito

def oraculo_trivial(n, k):
    qc = qiskit.QuantumCircuit(n)
    list_qu = list(range(n))
    bin_k = ('{0:0' + str(n) + 'b}').format(k)
    print(bin_k)

    bin_k = bin_k[::-1]

    for qu in range(n):
        qc.h(qu)
        
    qc.append(ZGate("zgate").control(num_ctrl_qubits = n-1),list_qu);

    for i in range(n):
        if bin_k[i] == '0':
            qc.x(i)

    backend = qiskit.Aer.get_backend('statevector_simulator')
    job = qiskit.execute(qc, backend)
    result = job.result()
    print('Estado gerado pelo circuito: ', result.get_statevector())

    print(qc.draw())
    return qc

def grover(oraculo):
    n = 4
    k = 2
    qc = qiskit.QuantumCircuit(n)
    
    for q in range(n):
        qc.h(q)
    
    list_qu = list(range(n))
    
    qc.append(oraculo(n,k), list_qu)
    
    qc.append(qinv_media(n),list_qu)
    
    qc.measure_all()

    print(qc.draw())
    
    return k
