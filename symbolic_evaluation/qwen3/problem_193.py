import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate π^4 using mpmath's pi
pi_power_4 = mp.power(mp.pi, 4)

# Divide by 48 to get the final result
result = pi_power_4 / 48

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))