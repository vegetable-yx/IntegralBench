import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Extract the constant e (base of natural logarithm)
e_val = mp.e

# Compute e^{-1}
e_inv = 1 / e_val

# Calculate numerator: e + e^{-1}
numerator = e_val + e_inv

# Denominator is 2
denominator = 2

# Compute cosh(1) = (e + e^{-1}) / 2
cosh1 = numerator / denominator

# Multiply by π to get the final result
result = mp.pi * cosh1

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))