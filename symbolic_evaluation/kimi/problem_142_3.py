import mpmath as mp
mp.dps = 15

# Calculate the modified Bessel function of the first kind I_0(2)
i0 = mp.besseli(0, 2)

# Subtract 1 from the Bessel function result
bessel_term = i0 - 1

# Multiply by π/2 to get the final result
result = (mp.pi / 2) * bessel_term

# Print the result with 10 decimal precision
print(mp.nstr(result, n=10))