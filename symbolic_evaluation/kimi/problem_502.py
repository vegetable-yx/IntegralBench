import mpmath as mp

# Set internal decimal precision to 15 for accurate intermediate calculations
mp.dps = 15

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Add 1 to the logarithm result
result = 1 + ln2

# Print the final result with exactly 10 decimal places
print(mp.nstr(result, n=10))