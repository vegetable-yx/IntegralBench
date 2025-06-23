import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute π using mpmath constant
pi_val = mp.pi

# Square the value of π
pi_squared = pi_val ** 2

# Divide the squared result by 2
result = pi_squared / 2

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))