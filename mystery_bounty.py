import random
import time

# Insert Total Bounty Pool & Number of Tokens
mystery_bounty = float(238)
bounty_tokens = int(9)

# Initiate the list to house final prize allocations
prize_list = []

# Static allocation of 4 tokens, including 1p troll.
x_1 = float(round(mystery_bounty * 0.7, 2))
x_2 = float(round(mystery_bounty * 0.1, 2))
x_3 = float(round(mystery_bounty * 0.1, 2))
x_4 = float(0.01)
prize_list.append(x_1)
prize_list.append(x_2)
prize_list.append(x_3)
prize_list.append(x_4)

# Work out remaining prize pool total & tokens
current_prize_total = 0

# print(prize_list)

for i in prize_list:
    current_prize_total += float(i)

# Establish remaining tokens and prize pool
final_pot = mystery_bounty - current_prize_total
remaining_tokens = int(bounty_tokens - 4)


# Initiate variables for final allocation loop
remaining_prize_allocations = []
last_token_numer = remaining_tokens - 1
total_remaining_percentage = 100

# Allocate all except final, as final will be catch for any amount remaining
# Generate the random percentahe allocation of the remaining prize pool, min step of 10%
for i in range(remaining_tokens-1):
        allocation = random.randrange(1, total_remaining_percentage,10)
        total_remaining_percentage -= allocation
        remaining_prize_allocations.append(allocation)

# Multiply the remaining pot by the % allocation and add to pool
for i in remaining_prize_allocations:
    prize_allocation = round(final_pot*(i/100), 2)
    prize_list.append(prize_allocation)


# Find the total sum of remaining allocations
list_total = 0

for i in prize_list:
    list_total += i

# Allocate final award based on remaining money in the mystery_bounty pot.
final_prize = mystery_bounty - list_total
list_total += final_prize
prize_list.append(round(final_prize, 2))

# Shuffle the prizes so that not always 1st gets biggest value
random.shuffle(prize_list)

# Print allocations
list_rank = 1

# Print prize awards per bounty token
for i in prize_list:
    print(str(list_rank) + ": " + str(i))
    list_rank += 1

# Sanity check to ensure prize pool matches initial pot
if list_total != mystery_bounty:
    print('\n')
    print("ERROR: The prize pool doesn't match the total bounty pool")
    print('\n')
    print("Total awarded: " + str(list_total))
    print("Starting prize pool: " + str(mystery_bounty))
    print('\n')
else:
    print('\n')
    print("Total awarded: " + str(list_total))
    print("Starting prize pool: " + str(mystery_bounty))