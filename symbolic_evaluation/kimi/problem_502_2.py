import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Add 1 to the logarithm
result = 1 + ln2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))