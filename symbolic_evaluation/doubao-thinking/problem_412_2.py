import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Assign Euler's number constant
result = mp.e

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))