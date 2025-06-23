import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate Catalan's constant (G)
catalan = mp.catalan

# Calculate sqrt(2)
sqrt2 = mp.sqrt(2)

# Calculate the argument for the logarithm: (1 + sqrt(2)) / 2
log_arg = (1 + sqrt2) / 2

# Calculate the logarithmic term: ln((1 + sqrt(2))/2)
log_term = mp.log(log_arg)

# Calculate pi multiplied by the logarithmic term
pi_log_term = mp.pi * log_term

# Calculate 2 times Catalan's constant
two_catalan = 2 * catalan

# Calculate the constant term: sqrt(2) - 1
constant_term = sqrt2 - 1

# Sum all components: pi*ln((1+sqrt2)/2) + 2G + (sqrt(2)-1)
result = pi_log_term + two_catalan + constant_term

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))