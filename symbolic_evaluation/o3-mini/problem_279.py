import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# User-defined parameters (example values - replace with actual values)
a = 1.0
b = 1.0

# Calculate the argument for the Bessel function
arg = (a * b) / 2

# Compute the modified Bessel function of the first kind (order 0)
bessel_value = mp.besseli(0, arg)

# Multiply by π to get final result
result = mp.pi * bessel_value

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))