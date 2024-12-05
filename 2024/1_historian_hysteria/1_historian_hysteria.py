locations_1 = []
locations_2 = []

with open ("location_ids.txt", "r") as f:
    for line in f:
        locations_1.append(int(line.strip().split()[0]))
        locations_2.append(int(line.strip().split()[1]))

locations_1.sort()
locations_2.sort()

distances = []
similarity_scores = []
for i in range(len(locations_1)):
    distances.append(abs(locations_1[i] - locations_2[i]))
    similarity_scores.append(locations_1[i] * locations_2.count(locations_1[i]))

distances_sum = sum(distances)
similarity_scores_sum = sum(similarity_scores)

print(f"Total distance: {distances_sum}")
print(f"Total similarity score: {similarity_scores_sum}")

