import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Calculate π (pi)
pi_val = mp.pi

# Compute the modified Bessel function of the first kind at order 0 for argument 2
bessel_val = mp.besseli(0, 2)

# Evaluate the expression: (π/2) * [1 - I_0(2)]
result = (pi_val / 2) * (1 - bessel_val)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))