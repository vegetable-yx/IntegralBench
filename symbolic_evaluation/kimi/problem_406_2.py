import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the numerator for the first arcsin argument
numerator1 = mp.sqrt(3) - 1
# Calculate the first argument: (√3 - 1)/2
arg1 = numerator1 / 2
# Compute first arcsin term
term1 = mp.asin(arg1)

# Calculate the numerator for the second arcsin argument
numerator2 = 1 - mp.sqrt(3)
# Calculate the second argument: (1 - √3)/2
arg2 = numerator2 / 2
# Compute second arcsin term
term2 = mp.asin(arg2)

# Combine the results: term1 - term2
result = term1 - term2

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))