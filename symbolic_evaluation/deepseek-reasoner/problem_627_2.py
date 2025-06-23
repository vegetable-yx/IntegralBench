import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate each term of the expression separately
pi_over_4 = mp.pi / 4  # Compute π/4
ln2_over_2 = mp.log(2) / 2  # Compute (ln 2)/2
constant_term = mp.mpf(1)  # Convert integer 1 to mpmath float

# Combine the terms according to the expression: π/4 + (ln2)/2 - 1
result = pi_over_4 + ln2_over_2 - constant_term

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))