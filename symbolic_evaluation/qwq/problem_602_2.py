import mpmath as mp
mp.dps = 15  # Set decimal precision to 15 digits

# Calculate pi^4 using mpmath's pi constant
pi_4 = mp.pi**4

# Divide by 120 to get the final result
result = pi_4 / 120

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))