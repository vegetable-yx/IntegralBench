import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute π using mpmath constant
pi_val = mp.pi

# Compute J_0(2) - Bessel function of the first kind order 0 at 2
j0_val = mp.besselj(0, 2)

# Calculate the expression: (π/4) * (1 - J_0(2))
result = (pi_val / 4) * (1 - j0_val)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))