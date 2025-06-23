import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute π using mpmath constant
pi_val = mp.pi

# Square π
pi_squared = mp.power(pi_val, 2)

# Divide by 16 to get the result
result = pi_squared / 16

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))