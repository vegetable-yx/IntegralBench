import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate pi^4 using intermediate steps
pi_val = mp.pi
pi_squared = mp.power(pi_val, 2)
pi_fourth = mp.power(pi_squared, 2)

# Compute the final result by dividing by 128
result = pi_fourth / 128

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))