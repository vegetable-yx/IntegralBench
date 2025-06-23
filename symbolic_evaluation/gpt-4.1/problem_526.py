import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Compute the natural logarithm of 3
ln3 = mp.log(3)

# Multiply pi by ln3
pi_times_ln3 = mp.pi * ln3

# Divide the result by 4 to obtain the final value
result = pi_times_ln3 / 4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))