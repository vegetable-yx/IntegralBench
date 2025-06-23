import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate square root of 6
sqrt6 = mp.sqrt(6)

# Multiply by 2
two_sqrt6 = 2 * sqrt6

# Add 7
sum_val = 7 + two_sqrt6

# Compute pi squared
pi_sq = mp.pi ** 2

# Multiply pi squared by the sum
product_val = pi_sq * sum_val

# Divide by 100
result = product_val / 100

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))