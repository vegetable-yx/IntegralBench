import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Calculate the square root of 3
sqrt3 = mp.sqrt(3)

# Sum the square roots
sum_sqrts = sqrt2 + sqrt3

# Compute the natural logarithm of the sum
log_val = mp.log(sum_sqrts)

# Multiply by π/4 to get the final result
result = (mp.pi / 4) * log_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))