import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate π using mpmath's constant
pi_val = mp.pi

# Compute π squared
pi_squared = mp.power(pi_val, 2)

# Compute π to the fourth power by squaring pi_squared
pi_fourth = mp.power(pi_squared, 2)

# Calculate numerator (3 * π^4)
numerator = mp.fmul(3, pi_fourth)

# Compute final result by dividing numerator by 128
result = mp.fdiv(numerator, 128)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))