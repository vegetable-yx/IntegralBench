import mpmath as mp

mp.dps = 15  # Set internal precision

# Compute modified Bessel function of the first kind I_0 at 1
i0 = mp.besseli(0, 1)

# Multiply by pi to obtain the final result
result = mp.pi * i0

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))