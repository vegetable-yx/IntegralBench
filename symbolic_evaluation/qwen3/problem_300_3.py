import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute trigamma values using polygamma(1, x)
trigamma_3_4 = mp.polygamma(1, mp.mpf('3/4'))  # ψ'(3/4)
trigamma_9_4 = mp.polygamma(1, mp.mpf('9/4'))  # ψ'(9/4)

# Calculate the difference between trigamma values
diff_trigamma = trigamma_3_4 - trigamma_9_4

# Multiply by π/16 to get final result
result = (mp.pi / 16) * diff_trigamma

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))