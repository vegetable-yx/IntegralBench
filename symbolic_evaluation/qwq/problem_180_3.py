import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate square root of 2
sqrt_two = mp.sqrt(2)

# Divide by 2 to get final result
result = sqrt_two / 2

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))