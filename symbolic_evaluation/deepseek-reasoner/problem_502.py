import mpmath as mp

# Set precision to 15 decimal places for calculations
mp.dps = 15

# Calculate the rational term 10747/10
term_rational = mp.mpf(10747)/10

# Calculate the logarithmic term 6*ln(2)
term_log = 6 * mp.log(2)

# Sum both components for final result
result = term_rational + term_log

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))