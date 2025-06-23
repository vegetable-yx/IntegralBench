import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate π squared
pi_squared = mp.pi ** 2

# Calculate square root of 2
sqrt_2 = mp.sqrt(2)

# Multiply π² by √2
product = pi_squared * sqrt_2

# Divide by 2 to get final result
result = product / 2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))