# Tutorial 2 – Teleportation

**Q1.** What are the vector representations of state |0⟩ and state |1⟩?  
**A1.** |0> is represented as [1,0] while |1> is [0,1]

**Q2.** The Hadamard gate puts a qubit into superposition by transforming |0⟩ and |1⟩. What is the expression resulting from transforming state |0⟩, and what is the expression resulting from transforming state |1⟩?  
**A2.** H|0> = 1/root(2) * (|0> + |1>) and H|1> = 1/root(2) * (|0> - |1>)

**Q3.** The expression resulting from adding the transformations of |0⟩ and |1⟩ above describes the qubit superposition state. What is α and what is β in this expression?  
**A3.** alpha and beta are complex numbers that represent the probability amplitudes such that |alpha|^2 + |Beta|^2 = 1

**Q4.** What are Bell states and how do they arise? What is the significance of Bell state and why do we care about them?  
**A4.** Bell states are four states in which two qubits are maximally entangled with each other. Bell states play a key role in enabling quantum operations such as teleportation and error correction, so they are key to quantum operations in quantum circuits. They arise when two qubits are maximally entangled together.  
Phi +: 1/root(2) * (|00> + |11>)  
Phi -: 1/root(2) * (|00> - |11>)  
Psi +: 1/root(2) * (|01> + |10>)  
Psi -: 1/root(2) * (|01> - |10>)

**Q5.** Entanglement is a relation between two qubits implemented using the CNOT gate, which is equivalent to the XOR gate in classical logic. Generate a truth table showing the relation between the control and target states.  
**A5.**  
Control | Target | XOR/CNOT  
0 | 0 | 0  
0 | 1 | 1  
1 | 0 | 1  
1 | 1 | 0

**Q6.** What is the special encryption property of the XOR (CNOT) operation? Illustrate this using logical expressions.  
**A6.** XOR is special and used in encryption because applying XOR to any variable twice will retrieve the original state of the variable therefore it can be convenient when used in encryption and decryption

**Q7.** What is teleportation and how it works? What is the difference between teleportation and other types of network messaging?  
**A7.** Teleportation in quantum computing means that the state of any unknown qubit is transferred (not copied) from the sender to the receiver instantaneously.  It is implemented by creating a bell pair or quantum pair between the sender and the receiver and entangling them (Hadamard to Alice Ancilla and CNOT with Ancilla as control and Bob's qubit as target) and then applying a cnot gate between Alice's ancilla and her qubit then applying hadamard to her qubit. Alice then measures the states of her two qubits and communicates the result to Bob through traditional channels and he can then perform operations to retrieve the original state of the unknown qubit. It differs as it does not copy the data but instead collapses it at the sender and reconstructs it at the receiver and it also transmits it instantly even though time is consumed by the traditional communication channels.

**Q8.** Explain using a circuit diagram how Anas can teleport a state of a qubit to Bandar without direct copying of the state.  
**A8.** Explained in the previous question.

**Q9.** What is the task completed in phase one of the teleportation process, and what is the impact of this task on the involved qubits?  
**A9.** Entanglement btween the two qubits in the bell pair. This task enables Bob's qubit to change based on the change that Alice's qubit undergoes, which is essential to achieve successful teleportation.

**Q10.** What is the task performed in phase 2 of the teleportation process and what are the outcomes of this phase and where are these outcomes stored? What do these outcomes represent?  
**A10.** Phase two entangles Alice's two qubits together to allow them to be correlated and then places Alice's qubit in superposition and measures the states of both qubits. The outcomes are stored in classical registers that hold discrete values and then they are communicated with Bob by using traditional channels to allow Bob to reconstruct the unknown state based on the outputs he receives.

**Q11.** Explain how Bandar recovers the original state transferred by Anas? What are the gates used? And what are the conditions used to apply these gates?  
**A11. (Completed)** CNOT gate is used (cx) with the Ancilla and Controlled Z gate is used (cz) with Alice's qubit. Based on the measurements, Bob can reconstruct the unknown state as follows:  
00 -> Apply I  
01 -> Apply X  
10 -> Apply Z  
11 -> Apply XZ
