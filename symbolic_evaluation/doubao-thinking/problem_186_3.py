import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate square root of 6
sqrt6 = mp.sqrt(6)

# Compute the (3 - sqrt(6)) term
numerator_part = 3 - sqrt6

# Calculate pi squared
pi_squared = mp.pi ** 2

# Multiply pi squared by the numerator part
product = pi_squared * numerator_part

# Divide by 96 to get final result
result = product / 96

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))