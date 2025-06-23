import mpmath as mp
mp.dps = 15

# Compute natural logarithm of 2
log_2 = mp.log(2)

# Square the logarithm
ln_squared = log_2 ** 2

# Multiply by -2 to get the final result
result = -2 * ln_squared

print(mp.nstr(result, n=10))