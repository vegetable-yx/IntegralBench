import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the parameter 'a' (user can adjust this value as needed)
a = 1.0

# Compute modified Bessel functions of the first kind
I0 = mp.besseli(0, a)
I1 = mp.besseli(1, a)
I2 = mp.besseli(2, a)

# Compute modified Bessel functions of the second kind
K0 = mp.besselk(0, a)
K1 = mp.besselk(1, a)

# Compute Struve functions (Hankel type)
H0 = mp.struveh(0, a)
H1 = mp.struveh(1, a)

# Calculate first term: I1(a) * K0(a)
term1 = I1 * K0

# Calculate second term: I2(a) * K1(a)
term2 = I2 * K1

# Calculate the Struve part: I1(a)H0(a) - I0(a)H1(a)
struve_part = I1 * H0 - I0 * H1

# Calculate third term: (π/(2a)) * struve_part
term3 = (mp.pi / (2 * a)) * struve_part

# Combine terms: term1 + term2 - term3
result = term1 + term2 - term3

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))