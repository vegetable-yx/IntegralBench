import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Calculate Euler's number (e)
e_value = mp.e

# Compute the difference between e and 1/e
e_difference = e_value - 1/e_value

# Multiply components to get final result
result = sqrt2 * e_difference

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))