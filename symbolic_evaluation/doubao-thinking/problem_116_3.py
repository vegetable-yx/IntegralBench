import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate π using mpmath's constant
pi_val = mp.pi

# Compute π squared
pi_squared = mp.power(pi_val, 2)

# Compute π to the fourth power by squaring π squared
pi_fourth = mp.power(pi_squared, 2)

# Divide π^4 by 64 to get the final result
result = mp.fdiv(pi_fourth, 64)

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))