import mpmath as mp
mp.dps = 15

# Calculate e^4 using mpmath exponential function
e_power_4 = mp.exp(4)

# Subtract 1 from the result
result = e_power_4 - 1

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))