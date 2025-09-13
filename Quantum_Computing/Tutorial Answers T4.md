# Tutorial 4 – Shor and Grover’s Algorithms

**Q1.** Explain how the public and private keys of RSA are computed.  
**A1.** We find two large prime numbers p and q and compute n = pxq. Then we find theta n where theta(n) = (p-1)(q-1). We then find e where e lies between 1 and theta(n) and the gcd e is coprime with theta meaning that their gcd in 1. Then, d is computed where ed mod theta(n) = 1.  
Public key = (n,e) Private key = (n, d)

**Q2.** What is the role of prime numbers in computing the RSA keys?  
**A2.** Prime numbers are used p and q to find the value of n by multiplying them and theta of n. The idea is that the security of RSA relies on the fact that factorization of n to extremely large prime numbers would be very expensive computationally.

**Q3.** Describe the Shor quantum prime factorization algorithm, describing in detail the actions taken at each step.  
**A3.** We start by selecting a where a lies between n and 1. If gcd(a, n) > 1 then we found a factor otherwise we continue. We apply a function f(x) = a^x mod n. We start computing f(x) given values of x until we get repeated sequences, allowing us to identify the period of the function. Once we know the period of the function, we check two conditions:  
1- r is even, if not repeat with a different a  
2- a^r/2 mod n is not equal to n-1  
If yes, then our factors are gcd(a^r/2 +-1, n)  

In quantum computing terms, we initialize all values of X into superposition. Then we apply Oracle operation to compute values of f(x) in parallel. Then, we use inverse QFT to find period information and finally we measure the output. We use control and target registers, modular differentiation circuit, and inverse QFT.

**Q4.** What is the ‘period’ in prime factorization algorithms (quantum and classic)? Use examples to illustrate your answer.  
**A4.** How often does the output sequence repeat itself. Take n=15 as an example. a=2.  
f(x) = 2^x mod 15  
f(0) = 1  
f(1) = 2  
f(2) = 4  
f(3) = 8  
f(4) = 1  
It means that the period is 4 because the sequence repeats every four steps.

**Q5.** How is the ‘period’ computed in quantum and classical factorization algorithms?  
**A5. (Completed)** Classically: compute f(x) = a^x mod n for increasing x until the sequence repeats, which is slow.  
Quantum: place all values of x in superposition, use controlled modular exponentiation to compute f(x) in parallel, then apply QFT to extract the period efficiently.

**Q6.** Why is Shor’s quantum algorithm able to solve the prime factorization problem in normal real time? Where does the acceleration come from?  
**A6.** It comes from reducing the problem first using classical computing from factorization to finding the period. Then, finding the period is possible in polynomial time by relying on superposition and parallel processing

**Q7.** What is the role of Fourier transform in improving the performance of Shor Algorithm?  
**A7.** Quantum Fourier Transform allows computing the period of the function in parallel by using the equation QFT(x) = 1/root(n) summation from k=0 to n-1 of e^2*pi*i*x*k/n |k> which speeds up the process of finding the period of a function instead of the increasing sequential algorithm that is computationally expensive for large numbers.

**Q8.** Describe in detail the circuit for Shor Algorithm.  
**A8. (Completed)** The circuit has two registers. First, apply Hadamard gates to the input register to create superposition. Then use controlled modular exponentiation to fill the output register. Next, apply the inverse QFT to the input register. Finally, measure the input register to get information about the period.

**Q9.** Describe Grover’s algorithm and explain how it works?  
**A9.** Grover's algorithm is an algorithm that is used to speed up the task of finding an item in an unsorted list of items to achieve O(sqrt(n)) time complexity. It starts by initialization as all items are placed in superposition then Oracle query flips the phase of the item that is needed but without finding the exact location of the item. Then, amplitudes of all items are modified to reduce the probability of all items and increase the probability of the target item. We alternate in oracle query operations and amplitude amplification sqrt(n) times then we perform measurement when the probability of the item we target is almost certain.

**Q10.** What is the major factor behind the success of Grover’s algorithm?  
**A10.** It relies on quantum computing mechanisms to flip the phase of the target item and amplifying its amplitude sqrt(n) times to allow finding the target item without iterating through all items to locate it.

**Q11.** Describe the oracle operation in Grover’s algorithm and explain how it works.  
**A11.** Oracle operation flips the phase of only the target item without finding its exact location. This allows amplifying amplitudes of all items at the same time and basically making the target item stand out and maximize its probability in measurement.

**Q12.** Describe the diffusion of Grover’s algorithm. What is the purpose of this operation, and how does it work?  
**A12. (Completed)** Diffusion is the amplitude amplification step. It inverts all amplitudes about their average — this decreases the amplitudes of non-target states and increases the amplitude of the marked state, making it more likely to be measured.

**Q13.** Describe the circuit of Grover’s search algorithm, showing the roles of each gate.  
**A13. (Completed)** Apply Hadamard gates to all qubits to create superposition. Then alternate between:  
1. Oracle (phase flip of the marked state)  
2. Diffusion (inversion about the mean to amplify the marked state)  
Repeat this sequence about sqrt(N) times. Finally, measure the qubits to collapse to the target state with high probability.
