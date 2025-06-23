import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate each term in the inner expression
term1 = mp.mpf(665) / mp.mpf(6)   # 665/6
term2 = mp.mpf(211) / mp.mpf(5)   # 211/5
term3 = mp.mpf(65) / mp.mpf(4)    # 65/4
term4 = mp.mpf(19) / mp.mpf(3)    # 19/3
term5 = mp.mpf(5) / mp.mpf(2)     # 5/2
term6 = mp.mpf(1)                 # 1
term7 = mp.log(2)                 # ln(2)

# Sum all terms inside the parentheses
inner_sum = term1 + term2 + term3 + term4 + term5 + term6 + term7

# Multiply the sum by 6
result = mp.mpf(6) * inner_sum

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))