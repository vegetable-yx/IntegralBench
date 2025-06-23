import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate pi^3 using mpmath's constant
pi_cubed = mp.pi ** 3

# Divide the cubed pi by 32 to get final result
result = pi_cubed / 32

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))