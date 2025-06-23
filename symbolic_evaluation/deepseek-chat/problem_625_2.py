import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Calculate pi (π) using mpmath constant
pi_value = mp.pi

# Calculate square root of 2
sqrt_two = mp.sqrt(2)

# Multiply pi by sqrt(2)
numerator = pi_value * sqrt_two

# Divide the numerator by 4 to get the final result
result = numerator / 4

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))