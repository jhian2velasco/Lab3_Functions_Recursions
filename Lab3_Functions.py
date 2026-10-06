# [CELL 1] STUDENT CONFIGURATION
LAST_NAME = "Velasco"
STUDENT_ID = "TUPM-26-1934"
SEED_DIGIT = int(STUDENT_ID[-1])

#Replace with your surname
# Replace with your ID
ID_SUM = sum(int(d) for d in STUDENT_ID if d.isdigit())
NAME_LENGTH = len(LAST_NAME)
print("Student:", LAST_NAME)
print("Seed Digit:", SEED_DIGIT)
print("Digit Sum:", ID_SUM)
print("Surname Length:", NAME_LENGTH)

# [CELL 2] FUNCTIONAL ENCAPSULATION
def greet():
    print("=" * 40)
    print(f"System Initialized for: {LAST_NAME}")
    print("=" * 40)

def identity_code():
    code = SEED_DIGIT * NAME_LENGTH
    return code
greet()
print("Identity Code:", identity_code())

# (CELL 3] LEGB VALIDATION
global_value = ID_SUM
def scope_test():
    global_value = SEED_DIGIT
    print("Inside function:", global_value)
scope_test()
print("Outside function:", global_value)

# [CELL 4] PARAMETRIC PROCESSING
def user_summary(title, *scores, **info):
    print(f"=== {title} ===")
    total = sum(scores)
    average = total / len(scores)
    print("Scores:", scores)
    print ("Total:", total)
    print("Average:", round(average, 2))
    for k, v in info.items():
        print(f"{k}: {v}")
    return average
avg = user_summary(
    F"{LAST_NAME} Academic Report",
    SEED_DIGIT * 10,
    ID_SUM % 100,
    NAME_LENGTH * 5,
    id=STUDENT_ID,
    surname=LAST_NAME
)

# [CELL 5] RETURN MECHANISM
def compute_area(radius):
    return 3.1416 * radius**2

area = compute_area (SEED_DIGIT + 2)
print("Computed Area:", round(area, 2))

# [CELL 6] SAFE CALCULATOR
def safe_calculator(x, y):
    try:
        result =x/y
    except ZeroDivisionError:
        result = "UNDEFINED"
    return result
print("Calculation Result:", safe_calculator(ID_SUM, SEED_DIGIT))

# [CELL 7] RECURSION

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

print("Factorial Result:", factorial(SEED_DIGIT))

# [CELL 8] STRING RECURSION

def reverse(text):
    if len(text) <= 1:
        return text
    return text[-1] + reverse(text[:-1])

print("Reversed Surname:", reverse(STUDENT_ID.upper()))

# [CELL 9] DECORATOR
def logger (func):
    def wrapper(*args, **kwargs):
        print("Executing:", func.__name__)
        return func(*args, **kwargs)
    return wrapper

@logger
def multiply(x, y):
    return x * y

print("Multiplication:", multiply(SEED_DIGIT, NAME_LENGTH))

# [CELL 10] LAMBDA
data = list(range(1, SEED_DIGIT + 10))
squared = list(map(lambda x: x**2, data))

print("Squared Data:", squared)

# [CELL 11] GENERATOR
def even_squares (limit):
    for i in range(limit):
        if i % 2 == 0:
            if i % 2 == 0:
                yield i**2

for value in even_squares (NAME_LENGTH + SEED_DIGIT):
    print(value)

