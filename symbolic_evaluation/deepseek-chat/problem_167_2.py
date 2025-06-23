import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Assign the constant π
pi_constant = mp.pi

# Divide π by 2 to obtain the result
result = pi_constant / 2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))