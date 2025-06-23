import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the parameter 'a' (example value)
a = 1.0

# Compute sin(a)
sina = mp.sin(a)

# Compute sin(a)/a
sina_over_a = sina / a

# Compute the term (1 - sin(a)/a)
one_minus_term = 1 - sina_over_a

# Compute pi / a^2
pi_over_a2 = mp.pi / (a**2)

# Multiply the terms to get the final result
result = pi_over_a2 * one_minus_term

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))