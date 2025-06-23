import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the natural logarithm of 5
log5 = mp.log(5)

# Multiply π by the logarithm and divide by 4
result = (mp.pi * log5) / 4

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))