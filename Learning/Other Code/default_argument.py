# name = jay is default argument as if argument is not passed to
# function then function takes that particular value
def fn(name = "Jay"): 
    print(f"Hello {name}.")

fn("Sameer") # if we pass argument
fn() # if we dont pass the argument