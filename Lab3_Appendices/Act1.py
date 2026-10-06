# APPENDIX EXERCISE 1: EQUIPMENT DIAGNOSTIC SYSTEM

# Student-specific inputs
LAST_NAME = "VELASCO"          # Change to your surname
SEED_NUM = 4                   # Change to the last digit of your ID
FAVORITE_ARTIST = "ARTIST"     # Change to your favorite artist


def diagnostic_logger(func):
    def wrapper(*args, **kwargs):
        print("\n[EXECUTION LOG]")
        print(f"Running diagnostic function: {func.__name__}")

        result = func(*args, **kwargs)

        print(f"Completed: {func.__name__}")
        return result

    return wrapper


def generate_readings(last_name, seed_num, artist):
    name_value = sum(ord(char) for char in last_name)
    artist_value = sum(ord(char) for char in artist)

    temperature = 40 + (name_value + seed_num) % 35
    pressure = 80 + (artist_value + seed_num) % 50
    vibration = (len(last_name) + len(artist) + seed_num) / 2

    return {
        "Temperature": temperature,
        "Pressure": pressure,
        "Vibration": vibration
    }


def validate_readings(readings):
    validated = {}

    for name, value in readings.items():
        try:
            value = float(value)

            if value < 0:
                raise ValueError("Negative reading is invalid.")

            validated[name] = value

        except (ValueError, TypeError) as error:
            validated[name] = None
            print(f"Invalid {name}: {error}")

    return validated


def calculate_average(readings):
    valid_values = [
        value for value in readings.values()
        if value is not None
    ]

    if not valid_values:
        return 0

    return sum(valid_values) / len(valid_values)


def classify_equipment(readings):
    try:
        temperature = readings["Temperature"]
        pressure = readings["Pressure"]
        vibration = readings["Vibration"]

        if (
            temperature > 70
            or pressure > 120
            or vibration > 10
        ):
            return "WARNING"

        elif (
            temperature > 60
            or pressure > 110
            or vibration > 7
        ):
            return "CAUTION"

        else:
            return "NORMAL"

    except (KeyError, TypeError):
        return "INVALID DATA"


@diagnostic_logger
def run_diagnostic():
    print("\n========================================")
    print("     EQUIPMENT DIAGNOSTIC SYSTEM")
    print("========================================")

    print(f"Surname: {LAST_NAME}")
    print(f"Seed Number: {SEED_NUM}")
    print(f"Favorite Artist: {FAVORITE_ARTIST}")

    # Generate readings
    readings = generate_readings(
        LAST_NAME,
        SEED_NUM,
        FAVORITE_ARTIST
    )

    print("\nGenerated Equipment Data:")
    for name, value in readings.items():
        print(f"{name}: {value:.2f}")

    # Validate readings
    validated = validate_readings(readings)

    print("\nValidation Results:")
    for name, value in validated.items():
        if value is not None:
            print(f"{name}: VALID")
        else:
            print(f"{name}: INVALID")

    # Calculate
    average = calculate_average(validated)

    print("\nDiagnostic Results:")
    print(f"Average Reading: {average:.2f}")

    # Classify
    condition = classify_equipment(validated)

    print(f"Equipment Condition: {condition}")

    print("\nFinal Output:")
    print("----------------------------------------")
    print(f"Equipment Status: {condition}")
    print(f"Average Reading: {average:.2f}")
    print("----------------------------------------")


if __name__ == "__main__":
    run_diagnostic()