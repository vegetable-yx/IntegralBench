import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define input parameters (example values; user should modify as needed)
a = mp.mpf(1)  # Replace with desired value of a
b = mp.mpf(1)  # Replace with desired value of b

# Calculate the argument for the Bessel function: (a*b)/2
arg = (a * b) / 2

# Compute modified Bessel function of first kind, order 0
bessel_val = mp.besseli(0, arg)

# Compute the constant factor: (π * a) / 4
factor = (mp.pi * a) / 4

# Multiply factor by Bessel function value
result = factor * bessel_val

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))

Note: This code uses example values `a=1` and `b=1`. To use different values, modify the assignments for `a` and `b` in the code. The result will be printed as a single floating-point number with exactly 10 decimal places.