import qiskit
import numpy as np
from qiskit.circuit.library.standard_gates import ZGate

n = int(input("Digite o número do qubits: "))
k = int(input("Digite o target do qubits: "))
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