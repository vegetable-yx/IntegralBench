import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define parameters a and b (replace with actual values)
a = 1.0  # Example value for a
b = 1.0  # Example value for b

# Compute square root of a
sqrt_a = mp.sqrt(a)

# Compute the argument for the Bessel function: (b * a) / 2
bessel_arg = (b * a) / 2

# Compute modified Bessel function of first kind, order 0
bessel_val = mp.besseli(0, bessel_arg)

# Compute the constant factor: π * sqrt(a) / 2
factor = (mp.pi * sqrt_a) / 2

# Multiply factor by Bessel function value
result = factor * bessel_val

# Print final result to 10 decimal places
print(mp.nstr(result, n=10))