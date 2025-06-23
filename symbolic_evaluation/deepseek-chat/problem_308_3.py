import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate the natural logarithm of 2
ln2 = mp.log(2)

# Multiply by pi and then divide by 2
pi_times_ln2 = mp.pi * ln2
result = pi_times_ln2 / 2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))