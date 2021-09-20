import time
def print_slow(text: str) -> None:
    for symbol in text:
        print(symbol, flush=True, end='')
        time.sleep(0.1)

def find_solution(numbers: list, problem_type: str) -> str:
    problems_types = {'P': 'n!',
                      'Ay': 'n ^ k',
                      'An': 'n! / (n - k)!',
                      'M': 'n! / (k1! * k2! * ... * kr!)',
                      'C': 'n! / (n - k)! * k!',
                      'B': 'm * n * ..'}
    if problem_type in ('P', 'An'):
        result_formula = problems_types[problem_type].replace('n', str(numbers[0]))
    elif problem_type in ('Ay', 'C'):
        result_formula = problems_types[problem_type].replace('n', str(numbers[0])).replace('k', str(numbers[1]))
    elif problem_type == 'M':
        result_formula = problems_types[problem_type].replace('n', str(numbers[0]))[:6]
        for k in numbers[1:]:
            result_formula += str(k) + '! * '
        result_formula = result_formula[:-3] + ')'
    elif problem_type == 'B':
        result_formula = ''
        for num in numbers:
            result_formula += str(num) + ' * '
        result_formula = result_formula[:-3]
    else:
        return -1
    return result_formula

def check_user_answer(correct_answer: str) -> bool:
    user_answer = input('Enter your answer (for example: 5!, 25! / 20!): ')
    if correct_answer.replace(' ', '') == user_answer.replace(' ', ''):
        return True
    return False

def generate_solution(numbers: list, problem_type: str, result_formula: str):
    problems_types = {'P': 'permutation',
    'Ay': 'allocation with repetition',
    'An': 'allocation without repetition',
    'M': 'permutation of n objects with k1, k2, ...  indistinguishable objects',
    'C': 'unordered group combinations',
    'B': 'basic principle of counting'}

    return f'SOLUTION:\n{result_formula}\n\nIn such types of problems, \
{problems_types[problem_type]} should be used. The common formula is as follows: {problems_types[problem_type]}'

# if __name__ == '__main__':
#     numbers = [5]
#     p_t = 'P'
#     correct_formula = find_solution(numbers, p_t)
#     user_answer_correctness = check_user_answer(correct_formula)
#     if user_answer_correctness:
#         print('Well done!')
#     else:
#         print(generate_solution(numbers, p_t, correct_formula))
