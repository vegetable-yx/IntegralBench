import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the exact value 1/3 using mpmath
# This fraction is represented exactly in rational form
result = mp.mpf(1) / 3

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))