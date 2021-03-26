import qiskit
from qiskit import *
from qiskit.tools.monitor import job_monitor
from collections import Counter
IBMQ.save_account('')   # You must fill in a Qiskit API token into IBMQ.save_account('') to run this script.
                        # Please go to IBM Quantum (https://quantum-computing.ibm.com/) to get your own API token and fill it between two single quotations.
                        # If you do not have an IBMid account, you have to create one to get the API token.
                        # The offical Qiskit Youtube account have published a video about how to get the API token can be found in https://youtu.be/M4EkW4VwhcI?t=360 .
                        # The API token part starting from 6:00.
IBMQ.load_account()

qr = QuantumRegister(1)
cr = ClassicalRegister(1)
circuit = QuantumCircuit(qr, cr)
circuit.reset(qr[0])
circuit.h(qr[0])
circuit.measure(qr, cr)
times_of_shots = 15
provider = IBMQ.get_provider('ibm-q')
qcomp = provider.get_backend('ibmq_quito')

job = execute(circuit, backend = qcomp, shots = times_of_shots, memory = True)
job_monitor(job)
result = job.result()
Readout = result.get_memory(circuit)

N = []
for n in range(times_of_shots):
    N.append(0)

i = 0
while i < len(Readout):   
    if (Readout[i] == '0'): 
        N[i] = 0
    elif (Readout[i] == '1'):
        N[i] = (2 ** i) * 1
    else:
        print("Execute Error! The result must be 0 or 1.")
        break
    i += 1

random_number = sum(N)

print("************************************")
print("Each quantum state =", Readout)
print("Each bit represents value =", N)
print("random_number =", random_number)
print("************************************")