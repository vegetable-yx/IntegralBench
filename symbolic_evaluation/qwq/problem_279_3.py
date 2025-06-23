import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Compute modified Bessel function of the first kind of order 0 at z=1
i0_value = mp.besseli(0, 1)

# Multiply by π to get the final result
result = mp.pi * i0_value

print(mp.nstr(result, n=10))