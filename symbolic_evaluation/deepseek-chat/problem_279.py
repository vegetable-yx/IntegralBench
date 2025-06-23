import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Example values for parameters (replace with actual values if different)
a = mp.mpf(1)
b = mp.mpf(1)

# Calculate the argument for the Bessel function: (b * a) / 2
arg = b * a / 2

# Compute modified Bessel function of first kind, order 0
I0 = mp.besseli(0, arg)

# Multiply result by pi
result = mp.pi * I0

# Print final result to 10 decimal places
print(mp.nstr(result, n=10))