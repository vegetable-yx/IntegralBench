import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Compute natural logarithm of 3
ln3 = mp.log(3)

# Multiply by pi and divide by 4 to get result
pi_times_ln3 = mp.pi * ln3
result = pi_times_ln3 / 4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))