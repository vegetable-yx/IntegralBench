import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate π squared
pi_squared = mp.pi ** 2

# Calculate natural logarithm of 3
ln_3 = mp.log(3)

# Compute the final result by multiplying π² with ln(3) and dividing by 3
result = (pi_squared * ln_3) / 3

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))