import mpmath as mp
# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Multiply by pi to get the final result
result = mp.pi * sqrt2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))