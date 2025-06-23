import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate modified Bessel function of the first kind I_0(6)
bessel_term = mp.besseli(0, 6)

# Compute numerator (I_0(6) - 1)
numerator = bessel_term - 1

# Final result calculation (numerator divided by 3)
result = numerator / 3

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))