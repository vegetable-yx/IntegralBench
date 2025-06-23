import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Compute e raised to the power of 6
e_power_6 = mp.exp(6)

# Calculate the numerator (e^6 - 1)
numerator = e_power_6 - 1

# Divide by 9 to get the final result
result = numerator / 9

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))