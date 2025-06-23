import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the Bessel function of the first kind J_{1/2}(2)
bessel_value = mp.besselj(0.5, 2)

# Calculate the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Multiply the Bessel function by sqrt(pi) to get the final result
result = sqrt_pi * bessel_value

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))