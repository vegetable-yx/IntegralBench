import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# Calculate the exact fraction 2/5 using mpmath
result = mp.mpf('2') / mp.mpf('5')

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))