# mine a log file and search if it contains 'python or not'
# and to find om which line is present

data = True
i = 1

with open("D:/Work/Python/Learning/Files I/O/log.txt") as f:
    while data:
        data = f.readline().lower() # to search while keeping all data lowered
        if "python" in data:
            print(data)
            print(f"Yes it contains 'python' on line {i}.")
        i+=1