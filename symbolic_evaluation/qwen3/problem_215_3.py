import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute the Bessel function of the first kind J_1 at x=1/2
bessel_value = mp.besselj(1, 0.5)

# Compute the square root of 2π
sqrt_2pi = mp.sqrt(2 * mp.pi)

# Multiply the components to get the final result
result = sqrt_2pi * bessel_value

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))