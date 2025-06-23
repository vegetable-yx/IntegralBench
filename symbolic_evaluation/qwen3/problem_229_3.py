import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate π^2 first for intermediate step
pi_squared = mp.pi ** 2

# Square the result to get π^4
pi_fourth = pi_squared ** 2

# Divide by 1280 to get final value
result = pi_fourth / 1280

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))