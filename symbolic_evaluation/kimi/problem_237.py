import mpmath as mp

# Set precision to 15 decimal places for calculations
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Multiply by 4 and π
result = 4 * mp.pi * sqrt2

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))