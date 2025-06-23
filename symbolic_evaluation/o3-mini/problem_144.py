import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Define the value of the parameter 'a' (example value, can be changed)
a_val = mp.mpf(1.0)

# Compute required special functions
I0 = mp.besseli(0, a_val)  # Modified Bessel I0
I1 = mp.besseli(1, a_val)  # Modified Bessel I1
L0 = mp.struvel(0, a_val)   # Modified Struve L0
L1 = mp.struvel(1, a_val)   # Modified Struve L1

# Calculate intermediate expressions for the numerator
# Part 1: 8a[(4 + a^2)I0 - 4I1]
inner_part1 = (4 + a_val**2) * I0 - 4 * I1
term1 = 8 * a_val * inner_part1

# Part 2: -[π(a^4 + 8a^2 - 16) - 8a^2]L0
inner_part2 = mp.pi * (a_val**4 + 8*a_val**2 - 16) - 8*a_val**2
term2 = -inner_part2 * L0

# Part 3: 2a[π(a^2 + 8) - 16]L1
inner_part3 = mp.pi * (a_val**2 + 8) - 16
term3 = 2 * a_val * inner_part3 * L1

# Combine terms for numerator
numerator = term1 + term2 + term3

# Denominator: 16a^3
denominator = 16 * a_val**3

# Final result
result = numerator / denominator

# Print result to 10 decimal places
print(mp.nstr(result, n=10))