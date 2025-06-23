import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Calculate the coefficient sqrt(2)/4
coefficient = sqrt2 / 4

# Calculate pi squared
pi_squared = mp.pi ** 2

# Multiply components to get final result
result = coefficient * pi_squared

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))