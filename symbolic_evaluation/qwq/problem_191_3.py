import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate π squared
pi_squared = mp.pi ** 2

# Calculate π squared squared (π^4)
pi_fourth = pi_squared ** 2

# Divide π^4 by 1440 to get final result
result = pi_fourth / 1440

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))