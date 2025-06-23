import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the first part: (729/6 + 243/5 + 81/4 + 27/3 + 9/2 + 3) + ln(2)
term1_1 = mp.fdiv(729, 6)
term1_2 = mp.fdiv(243, 5)
term1_3 = mp.fdiv(81, 4)
term1_4 = mp.fdiv(27, 3)
term1_5 = mp.fdiv(9, 2)
term1_6 = mp.mpf(3)
log_term = mp.log(2)  # Natural logarithm of 2
part1 = term1_1 + term1_2 + term1_3 + term1_4 + term1_5 + term1_6 + log_term

# Compute the second part: (64/6 + 32/5 + 16/4 + 8/3 + 4/2 + 2)
term2_1 = mp.fdiv(64, 6)
term2_2 = mp.fdiv(32, 5)
term2_3 = mp.fdiv(16, 4)
term2_4 = mp.fdiv(8, 3)
term2_5 = mp.fdiv(4, 2)
term2_6 = mp.mpf(2)
part2 = term2_1 + term2_2 + term2_3 + term2_4 + term2_5 + term2_6

# Compute the difference and multiply by 6
difference = part1 - part2
result = mp.fmul(6, difference)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))