import mpmath as mp

# Set the precision to 15 decimal places for internal calculations
mp.dps = 15

# Compute the modified Bessel function of the first kind of order 0 at 2
i0 = mp.besseli(0, 2)

# Compute the modified Struve function of order 1 at 2
l1 = mp.struvel(1, 2)

# Compute the modified Bessel function of the first kind of order 1 at 2
i1 = mp.besseli(1, 2)

# Compute the modified Struve function of order 0 at 2
l0 = mp.struvel(0, 2)

# Calculate the expression inside the brackets: I0(2)*L1(2) - I1(2)*L0(2)
inner_expr = i0 * l1 - i1 * l0

# Multiply by pi to get the final result
result = mp.pi * inner_expr

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))