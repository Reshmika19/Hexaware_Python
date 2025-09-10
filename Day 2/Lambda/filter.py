# Scenario 3: Filtering odd player IDs using filter() and lambda

player_ids = [101, 102, 103, 104, 105]

odd_ids = list(filter(lambda x: x % 2 != 0, player_ids))

print("All Player IDs:", player_ids)
print("Odd Player IDs (for lottery draw):", odd_ids)
