import mpmath as mp

# Set precision to 15 decimal places
mp.dps = 15

# Closed-form solution: pi * sqrt(2)
# Compute pi using mpmath constant
pi_val = mp.pi

# Compute square root of 2
sqrt2_val = mp.sqrt(2)

# Multiply to get the result
result = pi_val * sqrt2_val

# Print result to 10 decimal places
print(mp.nstr(result, n=10))