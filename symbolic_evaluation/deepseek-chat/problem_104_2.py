import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Compute Li_2(1/4)
li2_pos = mp.polylog(2, 0.25)

# Compute Li_2(-1/4)
li2_neg = mp.polylog(2, -0.25)

# Compute the difference: Li_2(1/4) - Li_2(-1/4)
diff = li2_pos - li2_neg

# Multiply by 1/2 to get the final result
result = 0.5 * diff

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))