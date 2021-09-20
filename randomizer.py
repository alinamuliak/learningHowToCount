import random


def read_file():
    problems_set = {}
    with open('problems.txt') as problems:
        problems = problems.readlines()
        for line in problems:
            line = line.split('|')
            problem = line[0]
            problem_type = line[1].strip()
            if problem_type not in problems_set:
                problems_set[problem_type] = [problem]
            else:
                problems_set[problem_type].append(problem)
    return problems_set


def permutation(problem):
    num = random.randint(5, 29)
    return [problem.replace('0', str(num)), [num]]


def allocations_with(problem):
    num = random.randint(6, 50)
    return [problem.replece('0', str(num)), [num]]


def allocations_without(problem):
    pass


def combinations(problem):
    pass


def multinomial(problem):
    list_words = ['EXELLENT', 'MISSISSIPPI', 'PEPPERONI', 'SPAGHETTI', 'BUBBLE',
                  'BANANA', 'PROGRAMMING', 'PYLYP', 'SUCCESSFULLY', 'CUCUMBER']
    list_groups = [('apples', 'people'), ('carrots', 'bunnies'), ('apples', 'people'),
                   ('sweets', 'children'), ('notebooks', 'students'), ('cookies', 'sad people'),
                   ('bananas', 'monkey'), ('plants', 'houses'), ('fish', 'cats')]
    if '$' in problem:
        word = random.choice(list_words)
        problem.replace('$', word)
        values = [len(word)]
    else:
        first, second = random.choice(list_groups)
        problem.replace('*', first, 1)
        problem.replace('*', second, 1)
        first_num = random.randint(2, 15)
        second_num = random.randint(first_num, 25)
        problem.replace('0', first_num, 1)
        problem.replace('0', second_num, 1)
        values = [first_num, second_num]
    return problem, values


def basic_calc(problem):
    list_outfits = [('skirts', 'blouses'), ('jeans', 't-shirts'), ('jeans', 'hoodies'),
                    ('shorts', 't-shorts'), ('shoes', 'dresses'), ('pants', 'sweaters'),
                    ('trousers', 'blouses'), ('pants', 't-shirts'), ('shoes', 'overalls')]
    first, second = random.choice(list_outfits)
    problem.replace('*', first, 1)
    problem.replace('*', second, 1)
    first_num = random.randint(2, 15)
    second_num = random.randint(first_num, 25)
    problem.replace('0', first_num, 1)
    problem.replace('0', second_num, 1)
    values = [first_num, second_num]
    return problem, values


def randomizing_problems(problem_type, problem):
    problem_types = {'P': permutation, 'M': multinomial, 'Ay': allocations_with,
                     'An': allocations_without, 'C': combinations, 'B': basic_calc}
    text, values = problem_types[problem_type(problem)]
    solution = [text, problem_type, values]
    return solution


if __name__ == "__main__":
    problems = read_file()
