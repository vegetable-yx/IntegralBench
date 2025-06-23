import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Divide pi squared by 8
term1 = pi_squared / 8

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Multiply the terms and apply negative sign
result = -term1 * ln2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))