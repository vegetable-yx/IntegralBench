import mpmath as mp
# Set decimal places for internal calculations
mp.dps = 15

# Calculate pi constant from mpmath
pi_value = mp.pi

# Compute the final result as pi divided by 4
result = pi_value / 4

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))