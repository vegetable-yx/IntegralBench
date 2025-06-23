import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate e (base of natural logarithm)
e_val = mp.e

# Calculate e^{-1} = 1/e
e_inv = 1 / e_val

# Compute the result: e - e^{-1}
result = e_val - e_inv

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))