import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate the natural logarithm of 2
ln2 = mp.log(2)

# Calculate pi (using mpmath's constant)
pi_val = mp.pi

# Multiply pi by ln(2)
product = pi_val * ln2

# Divide by 8 to get the final result
result = product / 8

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))