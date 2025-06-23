import mpmath as mp

mp.dps = 15  # Set internal precision

# Example parameters (adjust values as needed)
a = 1.0
b = 1.0

ab_half = (a * b) / 2  # Calculate (a*b)/2 once for reuse
a_squared = a ** 2      # Pre-calculate a squared

# Compute modified Bessel functions
I0 = mp.besseli(0, ab_half)  # I_0(ab/2)
I1 = mp.besseli(1, ab_half)  # I_1(ab/2)

# Calculate first term: (πa²/4) * I0
term1 = (mp.pi * a_squared / 4) * I0

# Calculate second term: (πa/(2b)) * I1
term2 = (mp.pi * a / (2 * b)) * I1

# Combine terms for final result
result = term1 - term2

# Print with 10 decimal precision
print(mp.nstr(result, n=10))