import mpmath as mp

# Set internal decimal precision to 15 to ensure accurate results
mp.dps = 15

# Calculate the square root of 6
sqrt6 = mp.sqrt(6)

# Compute the term (5 + 2*sqrt(6))
term = 5 + 2 * sqrt6

# Compute pi squared
pi_squared = mp.pi ** 2

# Multiply term by pi_squared
numerator = term * pi_squared

# Divide by 32 to get the final result
result = numerator / 32

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))