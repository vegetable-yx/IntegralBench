import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi^4
pi_power4 = mp.pi**4

# Divide by 1920 to get the final result
result = pi_power4 / 1920

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))