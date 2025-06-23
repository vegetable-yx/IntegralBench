import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Define the value of 'a' (user should adjust this as needed)
a = 1.0  # Example value, can be changed to any non-zero number

# Compute first term: π/(2a)
term1 = mp.pi / (2 * a)

# Compute second term: sin(a)/a²
term2 = mp.sin(a) / (a**2)

# Combine terms to get final result
result = term1 + term2

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))