import mpmath as mp

# Set internal decimal precision to 15 for accurate computation to 10 decimal places
mp.dps = 15

# Calculate the constant factor: 2
factor = 2

# Calculate pi using mpmath constant
pi_val = mp.pi

# Calculate the Bessel function of the first kind of order 1 at z=1
bessel_val = mp.besselj(1, 1)

# Compute the final result: 2 * pi * J_1(1)
result = factor * pi_val * bessel_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))