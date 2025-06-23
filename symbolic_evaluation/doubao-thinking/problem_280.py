import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate π using mpmath constant
pi_value = mp.pi

# Calculate square root of 3
sqrt_3 = mp.sqrt(3)

# Multiply π and √3
product = pi_value * sqrt_3

# Divide the product by 2 to get final result
result = product / 2

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))