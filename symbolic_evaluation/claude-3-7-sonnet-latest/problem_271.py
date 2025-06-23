import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute pi once
pi_val = mp.pi

# Calculate pi cubed
pi_cubed = pi_val ** 3

# Compute the term (25 - 6*pi)
inner_term = 25 - 6 * pi_val

# Multiply pi_cubed by the inner term
numerator = pi_cubed * inner_term

# Divide by 512 to get the final result
result = numerator / 512

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))