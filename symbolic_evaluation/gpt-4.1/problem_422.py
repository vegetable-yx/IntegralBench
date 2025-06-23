import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute 2 raised to the power of 4/3
exponent = mp.mpf(4) / 3  # Exact representation of exponent 4/3
base_power = mp.power(2, exponent)  # Calculate 2^(4/3)

# Multiply by 1/4 (equivalent to dividing by 4)
result = base_power / 4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))