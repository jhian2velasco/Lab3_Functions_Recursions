# APPENDIX EXERCISE 3
# INTELLIGENT EQUIPMENT MONITORING PIPELINE


from telemetry import generate_telemetry
from diagnostics import (
    validate_value,
    transform_data,
    create_report
)



LAST_NAME = "VELASCO"          # Change to your surname
SEED_NUM = 4                   # Change to your ID's last digit
FAVORITE_ARTIST = "ARTIST"     # Change to your favorite artist



def main():

    print("\n==============================================")
    print("   INTELLIGENT EQUIPMENT MONITORING SYSTEM")
    print("==============================================")

    print(f"Surname: {LAST_NAME}")
    print(f"Seed Number: {SEED_NUM}")
    print(f"Favorite Artist: {FAVORITE_ARTIST}")

   
    telemetry_stream = generate_telemetry(
        LAST_NAME,
        SEED_NUM,
        FAVORITE_ARTIST
    )

    valid_values = []
    invalid_count = 0
    processed_count = 0

    print("\nGenerated Telemetry Data:")

    # Process generator values one at a time
    for value in telemetry_stream:

        processed_count += 1

        print(f"Reading {processed_count}: {value}")


        try:

            if not validate_value(value):
                raise ValueError("Invalid telemetry value.")

            valid_values.append(float(value))

        except (ValueError, TypeError) as error:

            invalid_count += 1
            print(f"  -> Invalid reading: {error}")

    
    processed_values = transform_data(valid_values)

    print("\nProcessed Results:")

    for index, value in enumerate(
        processed_values,
        start=1
    ):
        print(f"Processed {index}: {value}")


    report = create_report(
        processed_values,
        len(valid_values),
        invalid_count
    )


    print("\n==============================================")
    print("          FINAL DIAGNOSTIC SUMMARY")
    print("==============================================")

    print(
        f"Processed Readings: "
        f"{report['Processed Readings']}"
    )

    print(
        f"Valid Readings: "
        f"{report['Valid Readings']}"
    )

    print(
        f"Invalid Readings: "
        f"{report['Invalid Readings']}"
    )

    print(
        f"Detected Abnormal Conditions: "
        f"{report['Abnormal Conditions']}"
    )

    print(
        f"Abnormal Values: "
        f"{report['Abnormal Values']}"
    )

    print(
        f"Overall Equipment Status: "
        f"{report['Overall Status']}"
    )

    print("==============================================")



if __name__ == "__main__":
    main()