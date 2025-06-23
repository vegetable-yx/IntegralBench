import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the parameter 'a' (example value, can be changed by user)
a = 1.0

# Compute modified Bessel function of first kind, order 0
I0 = mp.besseli(0, a)

# Compute modified Struve function, order 0
L0 = mp.struvel(0, a)

# Compute modified Bessel function of first kind, order 1
I1 = mp.besseli(1, a)

# Compute modified Struve function, order 1
L1 = mp.struvel(1, a)

# Calculate term1: (π/2) * [I0(a) - L0(a)]
term1 = (mp.pi / 2) * (I0 - L0)

# Calculate term2: (a/2) * [I1(a) - L1(a)]
term2 = (a / 2) * (I1 - L1)

# Calculate term3: (π/2 - 1)
term3 = mp.pi/2 - 1

# Combine terms: result = term1 - term2 - term3
result = term1 - term2 - term3

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))