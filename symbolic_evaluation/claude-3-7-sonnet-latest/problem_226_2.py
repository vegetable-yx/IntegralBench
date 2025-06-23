import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute pi using mpmath constant
pi_val = mp.pi

# Calculate pi cubed
pi_cubed = pi_val ** 3

# Multiply by 7 to get numerator
numerator = 7 * pi_cubed

# Divide by denominator 24 to get final result
result = numerator / 24

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))