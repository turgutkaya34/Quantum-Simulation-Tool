# Quantum-Simulation-Tool
# Quantum Simulation with Qiskit

This project demonstrates a quantum circuit simulation using Qiskit, integrated into a Streamlit web application. The purpose of this tool is to allow users to explore quantum circuits by modifying parameters and observing how changes affect the output. The app provides a simple yet interactive interface for experimenting with quantum operations and measuring the results.

## Features
- User-friendly interface built with Streamlit for quantum circuit interaction.
- Adjustable number of qubits (1-5) to explore different quantum circuit sizes.
- Parameterized quantum gates that can be adjusted in real time.
- Visualization of measurement results using histograms.
- Display of the quantum circuit structure for better understanding.

## Prerequisites
To run this project, ensure you have the following packages installed:

```sh
pip install numpy streamlit qiskit matplotlib ipykernel qiskit-aer
```

## How to Run
1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Run the Streamlit application with the following command:

```sh
streamlit run main.py
```

This will start a local web server, and you can interact with the quantum simulation through your browser.

## Usage
- **Select Number of Qubits**: Use the slider to select the number of qubits (between 1 and 5).
- **Set Parameter Values**: Adjust the rotation parameters (θ) for each qubit using the sliders.
- **Run Simulation**: The results of the quantum circuit measurements are displayed as a histogram.
- **Show Quantum Circuit**: Check the box to see the visual representation of the quantum circuit.

## Technology Stack
- **Qiskit**: A quantum computing framework used to create and simulate quantum circuits.
- **Streamlit**: A Python library for creating interactive web applications easily.
- **Matplotlib**: Used for plotting the histogram of the measurement results.

## Project Structure
- **main.py**: The main Python file containing the quantum simulation logic and Streamlit app code.

## Future Improvements
- Adding more complex quantum operations and different gate types.
- Providing a user-friendly interface for more advanced quantum algorithms.
- Integrating optimization algorithms to find optimal parameters for specific quantum states.

## License
This project is licensed under the MIT License.

## Acknowledgments
- **Qiskit Documentation**: For providing useful information about building quantum circuits.
- **Streamlit**: For making it easy to create interactive web applications.

Feel free to experiment with the parameters and explore how different settings affect the quantum state!

