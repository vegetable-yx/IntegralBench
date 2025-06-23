import mpmath as mp

# Set precision to 15 decimal places
mp.dps = 15

# Compute Struve H function of order 0 at x=1
struve_value = mp.struveh(0, 1)

# Compute Bessel function of the second kind of order 0 at x=1
bessel_y_value = mp.bessely(0, 1)

# Calculate the difference: StruveH(0,1) - Y(0,1)
difference = struve_value - bessel_y_value

# Multiply by pi/2 to get the final result
result = (mp.pi / 2) * difference

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))