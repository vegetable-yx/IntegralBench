import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define input parameters (example values, can be modified by user)
a = 1.0
b = 1.0

# Compute the argument for the cosh function: (a*b)/2
arg = (a * b) / 2.0

# Calculate the hyperbolic cosine of the argument
cosh_val = mp.cosh(arg)

# Compute the constant factor: sqrt(2*pi)
sqrt_2pi = mp.sqrt(2 * mp.pi)

# Multiply components to get final result
result = sqrt_2pi * cosh_val

# Print result rounded to 10 decimal places
print(mp.nstr(result, n=10))