# Generate table till 20 with creating each table in separate file
for i in range(2,21):
    with open(f"D:/Work/Python/Learning/Files I/O/table/table_of{i}.txt","w") as f:
        for j in range(1,11):
            f.write(f"{i} X {j} = {i*j}")
            if(j!=10):
                f.write("\n")
    