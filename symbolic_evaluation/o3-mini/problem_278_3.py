import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define parameters a and b (example values, can be modified)
a = 1.0
b = 1.0

# Compute the argument for the Bessel function: (a * b) / 2
arg = (a * b) / 2

# Compute the modified Bessel function of the first kind of order 0
bessel_val = mp.besseli(0, arg)

# Compute the entire expression: (π * a / 2) * I₀(ab/2)
result = (mp.pi * a / 2) * bessel_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))