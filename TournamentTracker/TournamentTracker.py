def get_players_from_input(match_num):
    """Helper function to get players for a match from user input"""
    input_str = input(f"Enter players for Match {match_num} (comma separated): ")
    players = {name.strip() for name in input_str.split(',') if name.strip()}
    return players

# Get player sets from user input
match1 = get_players_from_input(1)
match2 = get_players_from_input(2)
match3 = get_players_from_input(3)

# 1. Find players who participated in all three matches
participated_all_matches = match1 & match2 & match3

# 2. Find players who participated in exactly two matches
participated_two_matches = ((match1 & match2) | (match1 & match3) | (match2 & match3)) - participated_all_matches

# 3. Find players who participated in only one match
participated_one_match = ((match1 - match2 - match3) | (match2 - match1 - match3) | (match3 - match1 - match2))

# 4. Count total unique players
total_unique_players = len(match1 | match2 | match3)

# 5. Find players in Match 1 only
players_in_match1_only = match1 - match2 - match3

# Print results in the specified format
print("Players in all matches:", sorted(participated_all_matches))
print("Players in exactly two matches:", sorted(participated_two_matches))
print("Players in only one match:", sorted(participated_one_match))
print("Total unique players:", total_unique_players)
print("Players in match 1 only:", sorted(players_in_match1_only))