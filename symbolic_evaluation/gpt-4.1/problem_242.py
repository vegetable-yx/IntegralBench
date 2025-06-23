import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute trigamma at 1/3: ψ_1(1/3)
trigamma_1_3 = mp.polygamma(1, mp.mpf(1)/3)

# Compute trigamma at 2/3: ψ_1(2/3)
trigamma_2_3 = mp.polygamma(1, mp.mpf(2)/3)

# Calculate the difference: ψ_1(1/3) - ψ_1(2/3)
diff = trigamma_1_3 - trigamma_2_3

# Divide by 12 to get the final result
result = diff / 12

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))