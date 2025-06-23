import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate the constant pi (π) using mpmath's built-in constant
pi_val = mp.pi

# Calculate the square root of 2 using mpmath's sqrt function
sqrt2_val = mp.sqrt(2)

# Multiply π by √2 to get the final result
result = pi_val * sqrt2_val

# Print the result formatted to exactly 10 decimal places
print(mp.nstr(result, n=10))