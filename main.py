import randomizer as rd
import solutions as sl
import sys


def main():
    sl.print_slow("Bonjour! If you want to learn how to count, do not leave. ")
    sl.print_slow("Are you ready to think a little bit? y/n: ")
    decision1 = input()
    if decision1.lower() != 'y':
        sl.print_slow("See you next time! I'm pretty sure you do not know everything!")
        sys.exit()
    while True:
        problem, problem_type, values = rd.randomizing_problems()
        sl.print_slow('\n\nTHIS IS YOUR PROBLEM:\n')
        sl.print_slow(problem + '\n\nANY IDEAS????\nWhat you should use?:\nPermutation - P\nCombinations - '
                                'C\nAllocation with replacement - Ay\nAllocation without replacement - '
                                'An\nMultinomial coefficient - M\nBasic principle of counting - B\n\n')
        correct_answer = sl.find_solution(values, problem_type)
        user_type = input()
        if user_type.lower() != problem_type.lower():
            sl.print_slow(sl.generate_solution(values, problem_type, correct_answer))
        else:
            user_answer = sl.check_user_answer(correct_answer)
            if not user_answer:
                sl.print_slow(sl.generate_solution(values, problem_type, correct_answer))
            else:
                sl.print_slow('Well done!!\n')
        sl.print_slow('\nDo you want to try one more? y/n: ')
        one_more_time = input()
        if one_more_time != 'y':
            break
    sl.print_slow('THANKS FOR USING!!!!!<3')


main()
