import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute individual logarithmic terms
log2 = mp.log(2)
log5 = mp.log(5)
log3 = mp.log(3)
log7 = mp.log(7)

# Compute the 4*ln(2) term
term1 = 4 * log2

# Combine all terms: 4*ln(2) + ln(5) - ln(3) - ln(7)
result = term1 + log5 - log3 - log7

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))