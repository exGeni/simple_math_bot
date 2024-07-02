import random

def format_number(num):
    return int(num) if num.is_integer() else num
# Dictionary for replacing operators with emojis
OPERATORS = {
    '+': '➕',
    '-': '➖',
    '*': '✖️',
    ':': '➗',
    '=': '🟰'
}

# Dictionary for replacing powers with emojis
POWERS = {
    '2': '²',
    '3': '³',
    '4': '⁴',
    '5': '⁵'
}

def replace_operators(equation):
    for op, emoji in OPERATORS.items():
        equation = equation.replace(op, emoji)
    return equation

def replace_powers(equation):
    for power, emoji in POWERS.items():
        equation = equation.replace(f"^{power}", emoji)
    return equation

def generate_addition(level):
    if level == 1:
        y = random.randint(1, 10)
        result = random.randint(y + 1, 20)
        x = result - y
        return replace_operators(f"x + {y} = {result}")
    elif level == 2:
        variants = [
            lambda: f"x + x + {random.randint(1, 10)} = {random.randint(5, 30)}",
            lambda: f"x + {format_number(random.randint(1, 10) * 0.5)} = {format_number(random.randint(5, 20) * 0.5)}",
            lambda: f"{format_number(random.randint(1, 10) * 0.5)} + x = {format_number(random.randint(5, 20) * 0.5)}",
            lambda: f"x + ({random.randint(1, 5)} + {random.randint(1, 5)}) = {random.randint(5, 30)}",
        ]
        return replace_operators(random.choice(variants)())
    elif level == 3:
        x = format_number(random.randint(-20, 20) * 0.5)
        result = format_number(random.randint(-20, 20) * 0.5)
        return replace_operators(f"{x} + y = {result}")

def generate_subtraction(level):
    if level == 1:
        result = random.randint(1, 10)
        y = random.randint(1, 10)
        x = result + y
        return replace_operators(f"x - {y} = {result}")
    elif level == 2:
        variants = [
            lambda: f"x - ({random.randint(1, 10)} - {random.randint(1, 5)}) = {format_number(random.randint(-10, 10) * 0.5)}",
            lambda: f"x - {format_number(random.randint(1, 10) * 0.5)} = {format_number(random.randint(-10, 10) * 0.5)}",
            lambda: f"{format_number(random.randint(5, 20) * 0.5)} - x = {format_number(random.randint(-10, 10) * 0.5)}",
        ]
        return replace_operators(random.choice(variants)())
    elif level == 3:
        x = format_number(random.randint(-20, 20) * 0.5)
        result = format_number(random.randint(-20, 20) * 0.5)
        return replace_operators(f"{x} - y = {result}")

def generate_multiplication(level):
    if level == 1:
        y = random.randint(1, 10)
        x = random.randint(1, 10)
        result = x * y
        return replace_operators(f"x * {y} = {result}")
    elif level == 2:
        variants = [
            lambda: (lambda x, y: f"x * {y} = {x * y}")(random.randint(1, 10), random.randint(1, 10)),
            lambda: (lambda x, y: f"{y} * x = {x * y}")(random.randint(1, 10), random.randint(1, 10)),
            lambda: (lambda x: f"x * (x + {random.randint(1, 5)}) = {x * (x + random.randint(1, 5))}")(random.randint(1, 10)),
        ]
        return replace_operators(random.choice(variants)())
    elif level == 3:
        variants = [
            lambda: f"x * y = {random.randint(1, 100)}",
            lambda: (lambda x: f"x^2 = {x**2}")(random.randint(2, 10)),
            lambda: (lambda x: f"x^3 = {x**3}")(random.randint(2, 5)),
            lambda: (lambda x, p: f"x^{p} = {x**p}")(random.randint(2, 3), random.randint(4, 5)),
            lambda: (lambda x, y: f"x^2 + {y} = {x**2 + y}")(random.randint(2, 10), random.randint(1, 20)),
            lambda: (lambda x, y: f"x^2 - {y} = {x**2 - y}")(random.randint(2, 10), random.randint(1, 20)),
            lambda: (lambda x: f"(x + {random.randint(1, 5)})^2 = {(x + random.randint(1, 5))**2}")(random.randint(1, 5)),
        ]
        return replace_powers(replace_operators(random.choice(variants)()))

def generate_division(level):
    if level == 1:
        y = random.randint(1, 10)
        x = random.randint(1, 10) * y
        return replace_operators(f"x : {y} = {x // y}")
    elif level == 2:
        variants = [
            lambda: (lambda x, y: f"x : {y} = {x}")(random.randint(1, 10), random.randint(2, 5)),
            lambda: (lambda x, y: f"{x * y} : x = {y}")(random.randint(2, 10), random.randint(2, 5)),
            lambda: (lambda x, y, z: f"(x + {z}) : {y} = {x}")(random.randint(1, 10), random.randint(2, 5), random.randint(1, 10)),
        ]
        return replace_operators(random.choice(variants)())
    elif level == 3:
        variants = [
            lambda: f"{format_number(random.randint(1, 50) * 0.5)} : y = {format_number(random.randint(1, 10) * 0.5)}",
            lambda: f"x : {random.randint(1, 10)} = {format_number(random.randint(1, 10) * 0.5)}",
            lambda: f"(x + {format_number(random.randint(1, 20) * 0.5)}) : y = {format_number(random.randint(1, 10) * 0.5)}",
            lambda: f"x : (y + {random.randint(1, 5)}) = {format_number(random.randint(1, 10) * 0.5)}",
        ]
        return replace_operators(random.choice(variants)())

def generate_examples(level, num_rows):
    operations = [generate_addition, generate_subtraction, generate_multiplication, generate_division]
    examples = [[] for _ in range(4)]

    for i in range(num_rows):
        for j, operation in enumerate(operations):
            examples[j].append(operation(level))

    return examples