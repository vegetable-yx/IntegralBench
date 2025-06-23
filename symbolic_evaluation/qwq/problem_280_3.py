import mpmath as mp
mp.dps = 15

# Compute modified Bessel functions of the first kind
I_3_4 = mp.besseli(3/4, 3)
I_5_4 = mp.besseli(5/4, 3)

# Sum the Bessel function results
sum_bessel = I_3_4 + I_5_4

# Multiply by sqrt(3*pi)
result = mp.sqrt(3 * mp.pi)
final_result = result * sum_bessel

print(mp.nstr(final_result, n=10))