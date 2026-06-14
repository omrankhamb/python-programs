class Demo:
    Count = 0

    # Constructor
    def __init__(self):
        print("Inside Constructror")

    # Destructor
    def __del__(self):
        print("Inside Destructror")


Demo.Count = 11
print(f"Calling Static Characterstics : {Demo.Count}")




        