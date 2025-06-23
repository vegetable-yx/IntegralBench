import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate 2 * π using mpmath's pi constant
two_pi = 2 * mp.pi

# Compute square root of 2π using mpmath's sqrt function
result = mp.sqrt(two_pi)

# Print result with 10 decimal places using nstr formatting
print(mp.nstr(result, n=10))