import mpmath as mp
mp.dps = 15

# Direct assignment of the exact integer result
result = 18

# Print the result with 10 decimal places formatting
print(mp.nstr(result, n=10))