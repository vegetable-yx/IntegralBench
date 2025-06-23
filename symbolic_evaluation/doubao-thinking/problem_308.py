import mpmath as mp
mp.dps = 15

# Calculate pi/2 using mpmath's constant for pi
result = mp.pi / 2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))