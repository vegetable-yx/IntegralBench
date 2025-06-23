import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate 7! (5040)
factorial_7 = mp.factorial(7)

# Compute π^4
pi_power4 = mp.pi ** 4

# Calculate numerator: 7! * π^4
numerator = factorial_7 * pi_power4

# Calculate denominator: 2^16 (65536)
denominator = 2 ** 16

# Compute final result
result = numerator / denominator

# Print result with 10 decimal places
print(mp.nstr(result, n=10))