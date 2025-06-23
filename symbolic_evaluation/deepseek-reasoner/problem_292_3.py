import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate π using mpmath constant
pi_val = mp.pi

# Compute π squared
pi_squared = mp.power(pi_val, 2)

# Compute π to the fourth power
pi_fourth = mp.power(pi_squared, 2)

# Divide by 16 to get final result
result = pi_fourth / 16

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))