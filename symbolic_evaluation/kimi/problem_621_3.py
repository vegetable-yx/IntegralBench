import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate π using mpmath's constant
pi_value = mp.pi

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Multiply π and ln(2)
product = pi_value * ln2

# Divide by 2 and apply negative sign
result = -product / 2

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))