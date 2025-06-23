import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate π^2 first for better numerical stability
pi_squared = mp.pi ** 2

# Square the result to get π^4
pi_fourth = pi_squared ** 2

# Divide by 120 to get the final result
result = pi_fourth / 120

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))