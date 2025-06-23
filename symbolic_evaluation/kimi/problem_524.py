import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Compute e^2 (base of natural logarithm squared)
e_squared = mp.exp(2)  # Alternatively: e_squared = mp.e ** 2

# Add 1 to e^2
numerator = e_squared + 1

# Divide by 4 to get final result
result = numerator / 4

# Output result to 10 decimal places
print(mp.nstr(result, n=10))