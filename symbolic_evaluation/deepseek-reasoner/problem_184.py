import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the natural logarithm of 3
ln3 = mp.log(3)

# Multiply by pi (mpmath constant)
pi_ln3 = mp.pi * ln3

# Divide by 8 to get the final result
result = pi_ln3 / 8

# Output the result to 10 decimal places
print(mp.nstr(result, n=10))