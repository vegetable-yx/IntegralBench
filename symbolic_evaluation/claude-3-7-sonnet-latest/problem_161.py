import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define parameters (example values, can be modified by user)
a = 1.0
b = 1.0

# Compute the square root of a
sqrt_a = mp.sqrt(a)

# Compute the argument for the Bessel function: b * sqrt(a)
bessel_arg = b * sqrt_a

# Compute the modified Bessel function of the first kind, order 0
bessel_val = mp.besseli(0, bessel_arg)

# Multiply by a and pi
result = a * mp.pi * bessel_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))