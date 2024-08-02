from collections import deque
def measure_water(jug1_capacity, jug2_capacity, target_amount):
    visited_states = set()
    actions_queue = deque([(0, 0, "")])

    while actions_queue:
        jug1_current, jug2_current, action_sequence = actions_queue.popleft()

        if jug1_current == target_amount or jug2_current == target_amount:
            return action_sequence

        if (jug1_capacity, jug2_current) not in visited_states:
            visited_states.add((jug1_capacity, jug2_current))
            actions_queue.append((jug1_capacity, jug2_current, action_sequence + "Fill Jug1\n"))

        if (jug1_current, jug2_capacity) not in visited_states:
            visited_states.add((jug1_current, jug2_capacity))
            actions_queue.append((jug1_current, jug2_capacity, action_sequence + "Fill Jug2\n"))

        if (0, jug2_current) not in visited_states:
            visited_states.add((0, jug2_current))
            actions_queue.append((0, jug2_current, action_sequence + "Empty Jug1\n"))

        if (jug1_current, 0) not in visited_states:
            visited_states.add((jug1_current, 0))
            actions_queue.append((jug1_current, 0, action_sequence + "Empty Jug2\n"))

        pour_amount = min(jug1_current, jug2_capacity - jug2_current)
        if (jug1_current - pour_amount, jug2_current + pour_amount) not in visited_states:
            visited_states.add((jug1_current - pour_amount, jug2_current + pour_amount))
            actions_queue.append((jug1_current - pour_amount, jug2_current + pour_amount, action_sequence + "Pour Jug1 to Jug2\n"))

        pour_amount = min(jug2_current, jug1_capacity - jug1_current)
        if (jug1_current + pour_amount, jug2_current - pour_amount) not in visited_states:
            visited_states.add((jug1_current + pour_amount, jug2_current - pour_amount))
            actions_queue.append((jug1_current + pour_amount, jug2_current - pour_amount, action_sequence + "Pour Jug2 to Jug1\n"))

    return "Target amount cannot be measured"


jug1_capacity = int(input("Enter Jug_1 capacity:"))
jug2_capacity = int(input("Enter Jug_2 capacity:"))
target_amount = int(input("Enter target amount:"))

actions_sequence = measure_water(jug1_capacity, jug2_capacity, target_amount)
print(actions_sequence)
