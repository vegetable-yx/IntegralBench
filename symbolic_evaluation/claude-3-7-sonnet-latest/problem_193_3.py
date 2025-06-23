import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute π using mpmath constant
pi_val = mp.pi

# Compute natural logarithm of 2
ln2 = mp.log(2)

# Square the logarithm of 2
ln2_sq = ln2 ** 2

# Compute π cubed
pi_cubed = pi_val ** 3

# Multiply π^3 by ln²(2)
numerator = pi_cubed * ln2_sq

# Divide by 8 to get the final result
result = numerator / 8

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))