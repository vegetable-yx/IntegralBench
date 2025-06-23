import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define parameters a and b (example values; can be changed as needed)
a = 1
b = 1

# Compute the argument for the hypergeometric function: (a²b²)/4
arg = (a**2 * b**2) / 4

# Evaluate the generalized hypergeometric function ₀F₁(;1; arg)
hyper_term = mp.hyp0f1(1, arg)

# Multiply by π√2 to get the final result
result = mp.pi * mp.sqrt(2) * hyper_term

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))