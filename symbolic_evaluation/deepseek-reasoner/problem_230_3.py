import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate pi^4 using mpmath's pi constant
pi_power4 = mp.pi ** 4

# Divide the result by 1024
result = pi_power4 / 1024

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))