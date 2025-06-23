import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate pi to the fourth power
pi_power4 = mp.pi ** 4

# Compute the numerator (7 * pi^4)
numerator = 7 * pi_power4

# Divide by 240 to get the final result
result = numerator / 240

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))