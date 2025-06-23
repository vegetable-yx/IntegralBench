import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π^2
pi_squared = mp.pi ** 2

# Square the result to get π^4
pi_fourth = pi_squared ** 2

# Divide by 1000 to get final result
result = pi_fourth / 1000

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))