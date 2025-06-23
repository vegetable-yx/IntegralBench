import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate 4 times pi using exact symbolic constant
result = 4 * mp.pi

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))