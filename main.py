import randomizer as rd
import solutions as sl
import sys

def main():
    sl.print_slow("Bonjour! If you want to learn how to count, do not leave.")
    problem, problem_type, values = rd.randomizing_problems()
    sl.print_slow("Are you ready to think a little bit? y/n: ")
    decision1 = input()
    if decision1.lower() != 'y':
        sl.print_slow("See you next time! I'm pretty sure you do not know everything!")
        sys.exit()
    while True:
        sl.print_slow('\n\n THIS IS YOUR PROBLEM:\n')
        sl.print_slow(problem + '\n\nANY IDEAS????\n')
        correct_answer = sl.find_solution(values, problem_type)
        user_answer = sl.check_user_answer(correct_answer)
        if not user_answer:
            sl.generate_solution(values, problem_type, correct_answer)
        sl.print_slow('Do you want to try one more? y/n: ')
        one_more_time = input()
        if not one_more_time:
            break
    sl.print_slow('THANKS FOR USING!!!!!')

main()
