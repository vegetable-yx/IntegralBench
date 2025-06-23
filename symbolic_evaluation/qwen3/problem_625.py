import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate π using mpmath's constant
pi_value = mp.pi

# Calculate square root of 2 using mpmath's sqrt function
sqrt_two = mp.sqrt(2)

# Multiply π and sqrt(2)
numerator = pi_value * sqrt_two

# Divide by 4 to get final result
result = numerator / 4

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))