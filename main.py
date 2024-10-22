# Required imports
import numpy as np
import streamlit as st
from qiskit import QuantumCircuit, transpile, assemble
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
from qiskit.circuit import Parameter
from matplotlib import pyplot as plt

# To run this code, you need to install the following packages:
# pip install numpy streamlit qiskit matplotlib ipykernel qiskit-aer

# Streamlit app title
st.title("Quantum Simulation with Qiskit")

# Define a parameterized quantum circuit to simulate different scenarios
def create_quantum_simulation(num_qubits, parameters):
    qc = QuantumCircuit(num_qubits)
    
    # Apply parameterized rotations to each qubit
    for i in range(num_qubits):
        qc.rx(parameters[i], i)
    
    # Apply some controlled operations between qubits
    for i in range(num_qubits - 1):
        qc.cx(i, i + 1)
    
    qc.measure_all()
    return qc

# User input for number of qubits
num_qubits = st.slider("Select number of qubits", min_value=1, max_value=5, value=3)

# Create parameters for the quantum circuit
parameters = [Parameter(f'θ_{i}') for i in range(num_qubits)]
circuit = create_quantum_simulation(num_qubits, parameters)

# Compile the circuit to be run on a simulator
simulator = Aer.get_backend('aer_simulator')
compiled_circuit = transpile(circuit, simulator)

# User input for parameter values
param_values = {}
for i in range(num_qubits):
    param_values[parameters[i]] = st.slider(f"Set value for parameter θ_{i}", min_value=0.0, max_value=2*np.pi, value=np.pi/2)

# Bind parameters with the values provided by the user
bound_circuit = circuit.assign_parameters(param_values)

# Run the simulation
compiled_circuit = transpile(bound_circuit, simulator)
result = simulator.run(compiled_circuit).result()
counts = result.get_counts()

# Plot the result using matplotlib and display in Streamlit
fig, ax = plt.subplots()
plot_histogram(counts, ax=ax)
st.pyplot(fig)

# Display the quantum circuit
draw_circuit = st.checkbox("Show Quantum Circuit")
if draw_circuit:
    st.text(bound_circuit.draw())
