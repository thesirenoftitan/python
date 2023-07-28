def main():
    time = input("What time is it?\n")
    float_time = convert(time)

    if 7 <= float_time <8.01:
        print("breakfast time")
    elif 12 <= float_time <13.01:
        print("lunch time")
    elif 18 <= float_time <19.01:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    hours_float = float(hours)
    minutes_float = float(minutes)
    float_time = hours_float + minutes_float / 60
    return float_time

if __name__ == "__main__":
    main()
