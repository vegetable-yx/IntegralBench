import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate natural logarithm of 2 using mpmath's log function
result = mp.log(2)

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))