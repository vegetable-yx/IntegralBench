import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Compute J2(2): Bessel function of the first kind, order 2 at z=2
j2_val = mp.besselj(2, 2)

# Compute J3(2): Bessel function of the first kind, order 3 at z=2
j3_val = mp.besselj(3, 2)

# Calculate first term: J2(2) divided by 8
term1 = j2_val / 8

# Calculate second term: 3 times J3(2) divided by 4
term2 = (3 * j3_val) / 4

# Combine terms: term1 minus term2
result = term1 - term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))