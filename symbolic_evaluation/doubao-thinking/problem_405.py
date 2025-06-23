import mpmath as mp
# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate e^4 using mpmath exponential function
e_power_4 = mp.exp(4)

# Subtract 1 from the computed exponential value
result = e_power_4 - 1

# Print the final result with 10 decimal places precision
print(mp.nstr(result, n=10))