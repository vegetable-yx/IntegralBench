import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Compute π using mpmath's constant
pi = mp.pi

# Calculate square root of 3
sqrt3 = mp.sqrt(3)

# Calculate natural logarithm of 3
ln3 = mp.log(3)

# Multiply the fundamental values together
product = pi * sqrt3 * ln3

# Divide by 36 to get final result
result = product / 36

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))