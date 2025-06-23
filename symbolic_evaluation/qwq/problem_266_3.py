import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate the Bessel function of the first kind J_1 at 2
bessel_value = mp.besselj(1, 2)

# Multiply by π/2 to get the final result
result = (mp.pi / 2) * bessel_value

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))