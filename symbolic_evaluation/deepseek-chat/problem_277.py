import mpmath as mp

# Set internal precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Example values for variables a and b (replace with desired values)
a = 1.0
b = 1.0

# Calculate the argument for the Bessel function: (a * b) / 2
arg = (a * b) / 2

# Compute the modified Bessel function of the first kind of order 1
bessel_val = mp.besseli(1, arg)

# Calculate the constant factor: (π * a) / (2 * b)
factor = (mp.pi * a) / (2 * b)

# Multiply factor by Bessel value to get final result
result = factor * bessel_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))