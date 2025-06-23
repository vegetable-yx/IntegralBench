import mpmath as mp

# Set internal decimal precision to 15 digits for intermediate calculations
mp.dps = 15

# Compute the square of pi
pi_val = mp.pi
result = pi_val ** 2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))