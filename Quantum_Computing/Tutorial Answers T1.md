# Tutorial 1 – Quantum Basics

**Q1.** What is the first discovery that led to the birth of quantum mechanics?  
**A1.** The first discovery was Planck's theorem in which he discovered the theory of quantization. The theory states that the universe is grainy and it is made up of discrete indivisible units. As an example, even though light looks continuous, it is made up of tiny particles known as photons. This theory laid the foundation for quantum mechanics and led to many discoveries and advancements in the field later.

**Q2.** Describe in some detail each of the following quantum particle behaviors and describe the impact of each on quantum computing: superposition, coherence, interference, entanglement?  
**A2.**  
Superposition is a property of qubits in quantum computing that allows the qubit to exist in a complex linear combination of multiple states at the same time. That is, when not measured, the qubits can have a number of possible  states with their probability amplitudes. Superposition is necessary when building quantum computers as it allows us to build them and achieve much higher computational speed.

Coherence is a feature of quantum mechanics in which a qubit can exist is a coherent state allowing it to maintain its quantum properties such as superposition and entanglement which are necessary in quantum computing. The particles exist in the coherent state when they are free from interference and disturbance such as measurement and heat and radiation and noise. Coherence allows qubits to have quantum properties which gives quantum computers benefits over traditional computers.

Interference means that the phases of qubits ither add up or cancel each other when the qubits undergo quantum interactions with each other. This proprty is necessary to have better control over qubits and implement quantum operations freely. The bloch sphere is used to map the phases of the qubits and how they interfere together.

Entanglement is a property that allows qubits to be uniquely interconnected with each other such that when the state of one qubit changes it affects the state of the other qubit instantly. Entanglement enables quantum computers to perform concurrent computation and it is considered the basis for teleportation in quantum computing to transfer the state of the qubit.

**Q3.** What are the possible states of a qubit? Use Dirac and algebraic expression to describe the possible states.  
**A3.** A qubit exists in a complex linear combination of different states which are usually the ground state |0> and the excited state |1>. 

The qubit can be described as psi = alpha * |0> + Beta * |1> where alpha and beta are complex probability amplitudes.  
(Completed: Note that |alpha|^2 + |beta|^2 = 1, which ensures proper normalization of the qubit state.)

**Q4.** Explain how superposition is implemented. Use Qiskit notation (code) and a circuit diagram showing the gates (control) used.  
**A4.** Superposition is implemented by using a Hadamard gate which takes any qubit and places it in superposition meaning that the qubit has an equal probability of existing in the ground state or an excited state. Hadamard gate H|0> = 1/root(2) * (|0> + |1>) and H|1> = 1/root(2) * (|0> - |1>). In qiskit code hadamard is implemented as  

```

qc = QuantumCircuit(1)
qc.h(0)

```

and the circuit consists of a line for the qubit with a red H box.

**Q5.** What is the exact role of the Hadamard gate in implementing superposition? Describe the resulting qubit state using algebraic expressions.  
**A5.** H|0> = 1/root(2) * (|0> + |1>) and H|1> = 1/root(2) * (|0> - |1>). Hadamard gate places any qubit in superposition causing it to have an equal probability of existing in the ground or excited state.

**Q6.** What are the major technologies used to build qubits?  
**A6.** Qubits are built by relying on superconducting material that builds superconducting circuits. In addition, spinning qubits that rely on electron spins and photonic qubits that rely onn photons are used to build qubits. Isolated ions are also used and they are controlled by lazer technologies.

**Q7.** What are the major problems with current qubits? And how these problems are being dealt with?  
**A7. (Completed)** Current qubits suffer from some problems including that they can easily collapse into decoherence if measured or disturbed by heat, radiation, magnetism. This makes qubits hard to handle and utilize efficiently. Moreover, qubits suffer from no cloning theorem which prevents us from measuring the qubits in superposition or in a complex linear combination of states without collapsing them into a discrete value. Another problem is that qubits cost a lot of resources to implement and handle.  
These problems are being handled by developing methods like **quantum error correction codes**, **noise mitigation techniques**, and improved physical implementations such as superconducting circuits and trapped ions.

**Q8.** What is entanglement, and how is it implemented, and what is its significance in quantum computing? Use Qiskit code and circuit diagrams to illustrate your answer.  
**A8.** Already answered in a question before. It is implemented by creating two qubits and applying Hadamard gate to the first qubit and a controlled gate with the first qubit as control and the other qubit as the target. It is done as follows:  

```

qc = quantumCircuit(2)
qc.h(0)
qc.cx(0,1)

```

This places the circuit's qubits in the first bell state 1/root(2) * ( |00> + |11>)

**Q9.** Describe the role of quantum gates and circuits in building quantum applications.  
**A9. (Completed)** Quantum circuits are necessary in quantum computing as they are used to build high level applications. Unlike traditional circuits that are used for designing computer architecture, quantum circuits are used in building actual applications by creating qubits and performing quantum operations to them using quantum gates. Quantum algorithms like Shor’s and Grover’s are built as circuits of gates.

**Q10.** What are the major functions of Pauli gates?  
**A10.** Pauli gates apply different operations to the qubits. Pauli X changes the state of the qubit and acts as a traditional not gate changing qubits from ground to excited state and vice versa where x(|0>) = |1>. Pauli Z flips the state of the qubit which does not affect probabilities but it affects the intrference between qubits when they interact together where z|1> = - |1>. S gate acts as half a Z gate as it changes the phase of a qubit by rotating the qubit around Z axis by only 90 degrees. Pauli Y acts as a gate that rotates the qubit around the Y axis in the XZ plane allowing it to change its probability amplitude.

**Q11.** What is the significance of the Hadamard Gate?  
**A11.** It puts the qubits in a state of superposition. Further details were already discussed.

**Q12.** What is the function of the CNOT gate?  
**A12.** It is used to flip the state of a target qubit if the control qubit is 1 as an example cx(1, 0) gives (1,1). It is a necessary gate as it is used in qubit entanglement and it also plays a key role in achieving the four bell states and performing teleportation along with other quantum operations.

**Q13.** Using quantum gates, build a circuit for a true random generator.  
**A13. (Completed)**  

```

qc = quantumCircuit(1,1)
qc.h(0)
qc.measure(0,0)

```

This places a qubit in superposition to allow the qubit to exist in an equal probability of having states 0 or 1 (50% each). Then it measures the qubit and store the results in a traditional register.
