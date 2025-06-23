import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the first bracket: 729 + 1458/5 + 243/2 + 54 + 27 + 18 + 6*ln(2)
term1 = 729
term2 = mp.mpf(1458) / 5
term3 = mp.mpf(243) / 2
term4 = 54
term5 = 27
term6 = 18
# Calculate the logarithmic term
log_term = 6 * mp.log(2)
# Sum all terms in the first bracket
first_bracket = term1 + term2 + term3 + term4 + term5 + term6 + log_term

# Calculate the second bracket: 64 + 192/5 + 24 + 16 + 12 + 12
term7 = 64
term8 = mp.mpf(192) / 5
term9 = 24
term10 = 16
term11 = 12
term12 = 12
# Sum all terms in the second bracket
second_bracket = term7 + term8 + term9 + term10 + term11 + term12

# Compute final result: first_bracket minus second_bracket
result = first_bracket - second_bracket

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))