import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Assign values to parameters a and b (example values)
a = 1.0
b = 1.0

# Compute the argument for Bessel functions: ba = b * a
ba = b * a

# Compute modified Bessel functions of the first kind
# I0(ba) at order 0
I0 = mp.besseli(0, ba)
# I1(ba) at order 1
I1 = mp.besseli(1, ba)

# Compute the difference between the Bessel functions
bessel_diff = I0 - I1

# Compute the constant factor: (π * a) / 2
factor = (mp.pi * a) / 2

# Multiply factor by Bessel difference to get final result
result = factor * bessel_diff

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))