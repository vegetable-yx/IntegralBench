import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Example values for parameters a and b (arbitrary choice for demonstration)
# Replace with actual values if specific numbers are required
a = mp.mpf(1)
b = mp.mpf(1)

# Compute the argument for the hypergeometric function: (a^2 * b^2) / 4
z = (a**2 * b**2) / 4

# Evaluate the hypergeometric function {}_0F_1(;1; z)
hyper_term = mp.hyp0f1(1, z)

# Compute the constant factor: pi * sqrt(2)
constant_factor = mp.pi * mp.sqrt(2)

# Multiply constant factor by hypergeometric term
result = constant_factor * hyper_term

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))