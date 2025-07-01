def number_counter():
    print("Number Counter")

    try:
        start = int(input("Enter the starting number: "))
        end = int(input("Enter the ending number: "))
        step = int(input("Enter the step value (e.g., 1): "))

        if step == 0:
            print("Step value cannot be 0.")
            return

        print("\nCounting:")
        if start < end:
            for i in range(start, end + 1, step):
                print(i, end=' ', flush=True)
        else:
            for i in range(start, end - 1, -step):
                print(i, end=' ', flush=True)

        print("\n Done!")

    except ValueError:
        print(" Please enter valid integers.")

if __name__ == "__main__":
    number_counter()
