import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define input parameters (example values, can be modified)
a = 1.0
b = 1.0

# Compute the argument for the Bessel function: (a*b)/2
arg = (a * b) / 2

# Calculate the modified Bessel function of first kind (order 0)
bessel_value = mp.besseli(0, arg)

# Compute the constant factor: (a * pi)/2
factor = (a * mp.pi) / 2

# Multiply factor by Bessel function value
result = factor * bessel_value

# Print final result with 10 decimal places precision
print(mp.nstr(result, n=10))