import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate components separately
sqrt2 = mp.sqrt(2)          # Compute square root of 2
bessel_term = mp.besselj(1, 1)  # Calculate Bessel function J_1(1)

# Multiply all components together
result = sqrt2 * mp.pi * bessel_term

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))