import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate e^6 using mpmath's exponential function
e_power_6 = mp.exp(6)

# Subtract 1 from e^6
numerator = e_power_6 - 1

# Divide the result by 3
result = numerator / 3

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))