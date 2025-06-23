import mpmath as mp
mp.dps = 15

# Calculate e^4 using exponential function
e_power_4 = mp.exp(4)

# Multiply by pi to get the final result
result = mp.pi * e_power_4

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))