import random

def get_random_int(min_val, max_val):
    """
    Returns a random integer between min_val and max_val.
    """
    return random.randint(min_val, max_val)


def get_random_operator():
    """
    Returns a random operator from the list ['+', '-', '*'].
    """
    return random.choice(['+', '-', '*'])


def generate_problem(n1, n2, operator):
    """
    Generates a math problem string and its correct answer based on the operator.
    """
    problem = f"{n1} {operator} {n2}"
    if operator == '+':
        correct_answer = n1 + n2
    elif operator == '-':
        correct_answer = n1 - n2
    else:
        correct_answer = n1 * n2
    return problem, correct_answer


def math_quiz():
    score = 0
    total_questions = 5  # Setting the number of questions in the quiz

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = get_random_int(1, 10)  # Generate random number for first operand
        num2 = get_random_int(1, 10)  # Generate random number for second operand
        operator = get_random_operator()  # Choose a random operator

        # Generate the problem and the correct answer
        problem, correct_answer = generate_problem(num1, num2, operator)

        print(f"\nQuestion: {problem}")
        user_answer = input("Your answer: ")

        try:
            user_answer = int(user_answer)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue  # Skip to the next question if input is invalid

        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()
