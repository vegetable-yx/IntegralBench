import mpmath as mp

mp.dps = 15  # Set decimal places for internal calculations

# Calculate the hypergeometric function component
a = mp.mpf('3/4')        # Numerator parameter
b1 = mp.mpf('5/4')       # First denominator parameter
b2 = mp.mpf('1/2')       # Second denominator parameter
z = mp.mpf('-1/16')      # Function argument
hypergeom = mp.hyper([a], [b1, b2], z)

# Calculate the square root of pi/2
sqrt_pi_over_2 = mp.sqrt(mp.pi/2)

# Combine components for final result
result = sqrt_pi_over_2 * hypergeom

# Print with 10 decimal precision
print(mp.nstr(result, n=10))