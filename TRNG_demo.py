import qiskit
from qiskit import *
from qiskit.tools.monitor import job_monitor
from collections import Counter

#######################################################################################################################################################
# Attention!                                                                                                                                          #
# To anyone who wants to run this script, you must first fill in a Qiskit API token into IBMQ.save_account('') in order to run this script.           #
# Please go to IBM Quantum (https://quantum-computing.ibm.com/) to get your own API token and fill it between two single quotations.                  #
# If you do not have an IBMid account, you have to create one to get the API token.                                                                   #
# The offical Qiskit Youtube account have published a video about how to get the API token which can be found in https://youtu.be/M4EkW4VwhcI?t=360 . #
# The API token part starting from 6:00.                                                                                                              #
#######################################################################################################################################################

IBMQ.save_account('')
IBMQ.load_account()

qr = QuantumRegister(1)
cr = ClassicalRegister(1)
circuit = QuantumCircuit(qr, cr)
circuit.reset(qr[0])
circuit.h(qr[0])
circuit.measure(qr, cr)
times_of_shots = 3 # Maximum random number bit vaule
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
print("Random number is", times_of_shots, "bit")
print("Each quantum state =", Readout)
print("Each bit represents value (From 0 bit to", times_of_shots, "bit) =", N)
print("random_number =", random_number)
print("************************************")