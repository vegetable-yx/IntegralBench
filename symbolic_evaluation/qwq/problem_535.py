import mpmath as mp
mp.dps = 15

# Calculate e^3 using mpmath's exp function
e_cubed = mp.exp(3)

# Divide the result by 3 to get the final value
result = e_cubed / 3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))