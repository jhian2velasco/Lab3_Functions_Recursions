# APPENDIX EXERCISE 2: RECURSIVE FAULT TRACE


# Student-specific inputs
LAST_NAME = "VELASCO"          # Change to your surname
SEED_NUM = 4                   # Change to the last digit of your ID
FAVORITE_ARTIST = "ARTIST"     # Change to your favorite artist


# Global counter for recursive calls
recursive_calls = 0


def generate_fault_code(last_name, seed_num, artist):
    name_value = sum(ord(char) for char in last_name)
    artist_value = sum(ord(char) for char in artist)

    fault_code = (name_value + artist_value + seed_num) % 1000

    return fault_code


def trace_fault(fault_code, trace):
    global recursive_calls

    recursive_calls += 1

    # Add current fault code to the trace
    trace.append(fault_code)

    # BASE CONDITION
    if fault_code <= 10:
        return trace

    # Recursive step
    next_code = fault_code // 2

    return trace_fault(next_code, trace)


def run_fault_trace():
    global recursive_calls

    print("\n========================================")
    print("       RECURSIVE FAULT TRACE")
    print("========================================")

    print(f"Surname: {LAST_NAME}")
    print(f"Seed Number: {SEED_NUM}")
    print(f"Favorite Artist: {FAVORITE_ARTIST}")

    # Generate student-specific fault code
    fault_code = generate_fault_code(
        LAST_NAME,
        SEED_NUM,
        FAVORITE_ARTIST
    )

    print("\nGenerated Fault Data:")
    print(f"Initial Fault Code: {fault_code}")

    # Reset counter
    recursive_calls = 0

    # Perform recursive trace
    trace = []
    result = trace_fault(fault_code, trace)

    print("\nRecursive Trace:")
    for index, value in enumerate(result, start=1):
        print(f"Level {index}: {value}")

    print("\nNumber of Recursive Calls:")
    print(recursive_calls)

    print("\nFinal Output:")
    print("----------------------------------------")
    print(f"Initial Fault Code: {fault_code}")
    print(f"Final Fault Code: {result[-1]}")
    print(f"Recursive Calls: {recursive_calls}")
    print("Fault tracing completed successfully.")
    print("----------------------------------------")


if __name__ == "__main__":
    run_fault_trace()