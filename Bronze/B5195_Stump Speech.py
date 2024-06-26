def calculate_score(speech, phrase_scores):
    total_score = 0
    for phrase, score in phrase_scores.items():
        start = 0
        while True:
            start = speech.find(phrase, start)
            if start == -1:
                break
            total_score += score
            start += 1
    return total_score


K = int(input())

results = []

for dataset_number in range(1, K + 1):
    n = int(input())
    phrase_scores = {}

    for _ in range(n):
        phrase = input()
        score = int(input())
        phrase_scores[phrase] = score

    speech = input()
    score = calculate_score(speech, phrase_scores)
    results.append(f"Data Set {dataset_number}:\n{score}")

print("\n".join(results))
