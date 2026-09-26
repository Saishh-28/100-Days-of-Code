num = [1,2,3]
nem_nums = [n+1 for n in num]
print (nem_nums)

print([i for i in range(1,5) if i % 2 == 0])

if answer_state == "Exit":
    missing_states = []
    for state in all_states:
        if state not in guessed_states:
            missing_states.append(state)
            new_data = pandas. DataFrame (missing_states)
            new_data.to_csv("states_to_learn.csv")
        break

missing_states = [state for state in all_states if state not in guessed_states]