import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Assign values to parameters a and b (example values)
a = 1.0
b = 1.0

# Calculate square root of a
sqrt_a = mp.sqrt(a)

# Compute the argument for the Bessel function: b * sqrt(a)
arg = b * sqrt_a

# Calculate the modified Bessel function of the first kind, order 0
bessel_val = mp.besseli(0, arg)

# Compute constant factor: 2 * pi / a
factor = (2 * mp.pi) / a

# Multiply factor by Bessel function value
result = factor * bessel_val

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))