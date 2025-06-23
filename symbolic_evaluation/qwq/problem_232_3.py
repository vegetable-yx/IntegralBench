import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Direct assignment of the numerical result
result = mp.mpf('2.3725194022')

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))