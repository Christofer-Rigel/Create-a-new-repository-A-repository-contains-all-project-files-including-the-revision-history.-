# Define logic gate functions
def AND(a, b):
    return a & b

def OR(a, b):
    return a | b

def NOT(a):
    return ~a & 1  # Ensuring single-bit output

# Circuit function
def circuit(A, B, C):
    and1 = AND(A, B)  # First AND gate
    
    notC = NOT(C)  # NOT gate
    and2 = AND(notC, B)  # Second AND gate
    and3 = AND(C, A)  # Third AND gate
    
    or1 = OR(and2, and3)  # First OR gate
    
    Q = OR(and1, or1)  # Final OR gate
    
    return Q

# Test the circuit for all input combinations
print("A B C | Q")
for A in [0, 1]:
    for B in [0, 1]:
        for C in [0, 1]:
            print(A, B, C, "|", circuit(A, B, C))
