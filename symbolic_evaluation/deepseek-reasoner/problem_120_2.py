import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π squared
pi_squared = mp.pi ** 2

# Square pi_squared to get π^4
pi_fourth = pi_squared ** 2

# Divide π^4 by 32 to get final result
result = pi_fourth / 32

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))