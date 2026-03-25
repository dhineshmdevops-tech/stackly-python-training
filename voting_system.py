votes = {"A": 0, "B": 0, "C": 0}

for i in range (5):
    vote = input("vote (A/B/C): ")
    if vote in votes:
        votes[vote] += 1

winner = max(votes, key=votes.get)
print("winner is:", winner)