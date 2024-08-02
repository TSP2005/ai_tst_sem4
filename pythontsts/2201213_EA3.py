import random

N = int(input("Enter the number of students: "))
k = int(input("Enter the number of groups: "))
marks = [random.randint(0, 100) for _ in range(N)]


def calculate_diversity(groups):
    diversity = 0
    for group in groups:
        if len(group) > 1:
            avg = sum(group) / len(group)
            diversity += sum(abs(mark - avg) for mark in group)
    return diversity


def stochastic_hill_climbing(marks, k):
    groups = [[] for _ in range(k)]
    for mark in marks:
        groups[random.randint(0, k - 1)].append(mark)

    current_diversity = calculate_diversity(groups)
    steps = 0

    while steps < 100:
        steps += 1
        new_groups = [list(group) for group in groups]

        group_from = random.randint(0, k - 1)
        group_to = random.randint(0, k - 2)
        if group_to >= group_from:
            group_to += 1
        if new_groups[group_from]:
            student = new_groups[group_from].pop(random.randint(0, len(new_groups[group_from]) - 1))
            new_groups[group_to].append(student)
        new_diversity = calculate_diversity(new_groups)
        if new_diversity < current_diversity or random.random() < (
                current_diversity - new_diversity) / current_diversity:
            groups = new_groups
            current_diversity = new_diversity
    return groups

final_groups = stochastic_hill_climbing(marks, k)
print("Final groups:", final_groups)
print("Diversity:", calculate_diversity(final_groups))