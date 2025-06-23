import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate π using mpmath's built-in constant
pi_val = mp.pi

# Compute π squared
pi_squared = mp.power(pi_val, 2)

# Compute π to the fourth power by squaring pi_squared
pi_fourth = mp.power(pi_squared, 2)

# Divide by 16 to get final result
result = mp.fdiv(pi_fourth, 16)

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))