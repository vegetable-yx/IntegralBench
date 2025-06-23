import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Example values for parameters a and b
# Replace these with actual values as needed
a = 1.0
b = 1.0

# Compute the argument for Bessel functions: (a*b)/2
arg = (a * b) / 2.0

# Calculate modified Bessel functions I0 and I2 at argument
I0_val = mp.besseli(0, arg)  # Modified Bessel I0
I2_val = mp.besseli(2, arg)  # Modified Bessel I2

# Sum the Bessel function values
bessel_sum = I0_val + I2_val

# Compute constant factor: πa²/8
constant_factor = (mp.pi * a**2) / 8.0

# Multiply constant factor by Bessel sum for final result
result = constant_factor * bessel_sum

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))