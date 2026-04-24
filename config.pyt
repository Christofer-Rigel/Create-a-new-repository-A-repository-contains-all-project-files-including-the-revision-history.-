import time
from decimal import Decimal, getcontext

# Set VERY high precision
getcontext().prec = 10000  # increase for more pain

# Two massive numbers
a = Decimal("9" * 5000)   # 5000-digit number
b = Decimal("8" * 5000)

start_time = time.time()
run_time = 3600  # 1 hour (in seconds)

result = Decimal(0)
iteration = 0

while time.time() - start_time < run_time:
    # Heavy repeated computation
    temp = (a * b) / (Decimal(iteration + 1) + Decimal(1))
    
    # Accumulate result slowly
    result += temp.sqrt()  # sqrt makes it even slower
    
    iteration += 1

    # Optional: print progress every few seconds
    if iteration % 100 == 0:
        print(f"Iteration: {iteration}")

print("\nFinal Result:")
print(result)