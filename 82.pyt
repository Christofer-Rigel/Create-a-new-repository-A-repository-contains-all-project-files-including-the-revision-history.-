import math

# Define safe environment with math functions
safe_env = {
    'abs': abs,
    'round': round,
    'math': math,
    'pi': math.pi,
    'e': math.e,
    '__builtins__': {},  # Disable unsafe functions
}

# Memory to store variables
variables = {}

print("=== Complex Python Calculator ===")
print("Type your expression or 'exit' to quit.")
print("You can use math functions like sin(), cos(), log(), etc.")
print("Example: sin(pi/2) + log(10) * 3")

while True:
    try:
        expr = input(">>> ")
        if expr.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        # Allow variable assignments like x = 2
        if "=" in expr:
            var, val_expr = expr.split("=", 1)
            var = var.strip()
            val = eval(val_expr, {**safe_env, **variables})
            variables[var] = val
            print(f"{var} = {val}")
        else:
            # Evaluate the expression
            result = eval(expr, {**safe_env, **variables})
            print(f"Result: {result}")

    except Exception as e:
        print(f"Error: {e}")