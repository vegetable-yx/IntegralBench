import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute Struve H function of order 1 at 2
struve_val = mp.struveh(1, 2)

# Compute Bessel function of the second kind of order 1 at 2
bessel_y_val = mp.bessely(1, 2)

# Combine the Struve and Bessel values: H_1(2) - Y_1(2)
diff_val = struve_val - bessel_y_val

# Multiply by π/4 to get the final result
result = (mp.pi / 4) * diff_val

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))