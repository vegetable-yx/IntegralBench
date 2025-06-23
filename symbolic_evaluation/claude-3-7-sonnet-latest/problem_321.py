import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Define the value of 'a' (replace with desired value)
a = 1.0

# Compute modified Struve function of order 0
L0 = mp.struvel(0, a)

# Compute modified Bessel function of the first kind of order 0
I0 = mp.besseli(0, a)

# Compute modified Bessel function of the first kind of order 1
I1 = mp.besseli(1, a)

# Calculate first term: (π/2) * L₀(a)
term1 = (mp.pi / 2) * L0

# Calculate second term: (π/2) * I₀(a)
term2 = (mp.pi / 2) * I0

# Calculate third term: (π²/4) * I₁(a)
term3 = (mp.pi**2 / 4) * I1

# Combine all terms: term1 - term2 + term3
result = term1 - term2 + term3

# Print final result to 10 decimal places
print(mp.nstr(result, n=10))