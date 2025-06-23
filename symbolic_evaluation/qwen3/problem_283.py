import mpmath as mp
mp.dps = 15

# Calculate sqrt(5)
sqrt5 = mp.sqrt(5)

# Compute the argument inside the logarithm
inner = 2 + sqrt5

# Calculate natural logarithm of (2 + sqrt(5))
log_val = mp.log(inner)

# Cube the logarithmic value
log_cubed = log_val ** 3

# Divide by 6 to get the final result
result = log_cubed / 6

# Print result with 10 decimal places
print(mp.nstr(result, n=10))