import mpmath as mp

# Set the precision to 15 decimal places for internal calculations
mp.dps = 15

# Assign the mathematical constant e to a variable
result = mp.e

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))