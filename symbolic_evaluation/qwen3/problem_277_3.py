import mpmath as mp
mp.dps = 15

# Compute modified Bessel functions of the first kind at 1 and 0
I1_1 = mp.besseli(1, 1)
I0_1 = mp.besseli(0, 1)

# Calculate the expression components
sum_bessel_terms = 1 + I1_1 - I0_1

# Multiply by 2π to get final result
result = 2 * mp.pi * sum_bessel_terms

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))