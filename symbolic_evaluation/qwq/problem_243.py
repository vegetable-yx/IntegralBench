import mpmath as mp
mp.dps = 15  # Set internal precision

# Calculate pi^4 by squaring pi^2
pi_squared = mp.pi ** 2
pi_fourth = pi_squared ** 2

# Divide by 64 to get final result
result = pi_fourth / 64

# Print result with 10 decimal places
print(mp.nstr(result, n=10))