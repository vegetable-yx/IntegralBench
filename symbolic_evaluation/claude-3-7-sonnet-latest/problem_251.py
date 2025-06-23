import mpmath as mp

# Set internal precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Compute pi using mpmath constant
pi_val = mp.pi

# Square the value of pi
pi_squared = mp.power(pi_val, 2)

# Divide the squared pi by 4 to get the result
result = pi_squared / 4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))