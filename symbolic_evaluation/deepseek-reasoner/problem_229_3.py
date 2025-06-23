import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate π^4 using intermediate steps for clarity
pi_val = mp.pi
pi_squared = mp.power(pi_val, 2)
pi_fourth = mp.power(pi_squared, 2)

# Compute the final result by dividing π^4 by 192
result = mp.fdiv(pi_fourth, 192)

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))