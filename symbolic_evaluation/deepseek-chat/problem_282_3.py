import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate π (pi) using mpmath constant
pi_val = mp.pi

# Calculate the square root of 2
sqrt2_val = mp.sqrt(2)

# Calculate the denominator: √2
denominator = sqrt2_val

# Calculate the fraction: π / √2
fraction = pi_val / denominator

# Calculate hyperbolic cosine of 4
cosh_val = mp.cosh(4)

# Multiply the fraction by cosh(4)
result = fraction * cosh_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))