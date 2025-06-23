import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate modified Bessel function of the first kind, order 0 at 2
bessel_i0 = mp.besseli(0, 2)

# Calculate modified Bessel function of the first kind, order 1 at 2
bessel_i1 = mp.besseli(1, 2)

# Calculate modified Struve function, order 0 at 2
struve_l0 = mp.struvel(0, 2)

# Calculate modified Struve function, order 1 at 2
struve_l1 = mp.struvel(1, 2)

# Compute the expression inside the brackets: I0(2)*L1(2) - I1(2)*L0(2)
inner_term = bessel_i0 * struve_l1 - bessel_i1 * struve_l0

# Multiply by π/2 to get the final result
result = (mp.pi / 2) * inner_term

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))