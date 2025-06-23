import mpmath as mp
mp.dps = 15

# Calculate pi/4 directly using mpmath's constant
result = mp.pi / 4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))