import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of 2011
sqrt_2011 = mp.sqrt(2011)

# Subtract the square root from 2011
result = 2011 - sqrt_2011

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))