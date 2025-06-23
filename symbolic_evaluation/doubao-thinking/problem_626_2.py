import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Compute the constant pi
pi_val = mp.pi

# Divide pi by 2
denom = 2
fraction = pi_val / denom

# Compute natural logarithm of the fraction
result = mp.log(fraction)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))