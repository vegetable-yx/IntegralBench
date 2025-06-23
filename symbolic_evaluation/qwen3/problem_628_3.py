import mpmath as mp
mp.dps = 15

# Calculate the sum of 2 and pi
sum_2_pi = mp.mpf(2) + mp.pi

# Divide the sum by 8 and apply negative sign
result = -sum_2_pi / 8

# Print the result with 10 decimal precision
print(mp.nstr(result, n=10))