import mpmath as mp

# Set decimal places for internal precision
mp.dps = 15

# Define parameters (example values, can be changed by user)
a = 1.0
b = 1.0

# Compute square root of parameter a
sqrt_a = mp.sqrt(a)

# Calculate the argument for the cosh function
arg = (b * sqrt_a) / 2

# Evaluate hyperbolic cosine of the argument
cosh_val = mp.cosh(arg)

# Multiply result by pi to get final value
result = mp.pi * cosh_val

# Print result to 10 decimal places
print(mp.nstr(result, n=10))