import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the value of a (example value, can be changed)
a = 1.0

# Calculate π using mpmath constant
pi_val = mp.pi

# Calculate the denominator term 4a
denominator = 4 * a

# Compute the fraction π/(4a)
fraction = pi_val / denominator

# Calculate the Bessel function of first kind of order 1 at a
bessel_term = mp.besselj(1, a)

# Multiply to get final result
result = fraction * bessel_term

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))