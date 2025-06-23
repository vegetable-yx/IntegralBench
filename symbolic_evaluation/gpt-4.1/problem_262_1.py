import mpmath as mp
mp.dps = 15

# Compute the Bessel function of the first kind J_1(2)
j1_value = mp.besselj(1, 2)

# Multiply by pi
pi_times_j1 = mp.pi * j1_value

# Divide by 8 to get the final result
result = pi_times_j1 / 8

print(mp.nstr(result, n=10))