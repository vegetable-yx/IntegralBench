import mpmath as mp
mp.dps = 15

# Calculate 2^(3/2) using exact exponent
base = mp.mpf(2)
exponent = mp.mpf(3)/mp.mpf(2)
two_power = base ** exponent  # Equivalent to 2*sqrt(2)

# Calculate hyperbolic cosine component
cosh_value = mp.cosh(mp.mpf(1))  # Compute cosh(1)
cosh_term = cosh_value - 1       # Subtract 1 from cosh result

# Combine components for final result
result = two_power * cosh_term

# Print with 10 decimal precision
print(mp.nstr(result, n=10))