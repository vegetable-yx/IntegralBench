import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate 1/sqrt(2)
a = mp.mpf(1)/mp.sqrt(2)

# Compute hyperbolic cosine term
cosh_term = mp.cosh(a)

# Compute hyperbolic sine term
sinh_term = mp.sinh(a)

# Multiply sinh term by sqrt(2)
sqrt2_sinh = mp.sqrt(2) * sinh_term

# Calculate the difference between cosh and sqrt2*sinh terms
difference = cosh_term - sqrt2_sinh

# Multiply by 2 for final result
result = 2 * difference

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))