import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate square root of 2
sqrt_2 = mp.sqrt(2)

# Multiply by sqrt(2) to get the final result
result = mp.pi * sqrt_2

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))