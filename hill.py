import random
import string

def generate_random_solution(answer):
    l = len(answer)
    return [random.choice(string.printable) for _ in range(l)]

def evaluate(solution, answer):
    target = list(answer)
    diff = 0
    for i in range(len(target)):
        s = solution[i]
        t = target[i]
        # calculate ASCII difference
        diff += abs(ord(s) - ord(t))
    return diff

def mutate_solution(solution):
    ind = random.randint(0, len(solution)-1)
    solution[ind] = random.choice(string.printable)
    return solution

def SimpleHillClimbing():
    answer = "Artificial Intelligence"
    best = generate_random_solution(answer)
    best_score = evaluate(best, answer)
    iteration = 0
    max_iterations = 100000   # safety stop

    while True:
        iteration += 1
        print("Score:", best_score, " Solution:", "".join(best))
        if best_score == 0:
            print("Perfect match found!")
            break
        new_solution = mutate_solution(list(best))
        score = evaluate(new_solution, answer)
        if score < best_score:
            best = new_solution
            best_score = score
        if iteration >= max_iterations:
            print("Stopped after", max_iterations, "iterations")
            break

SimpleHillClimbing()
