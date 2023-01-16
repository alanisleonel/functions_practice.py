# function named hello
# def hello():
#     print("hello")
# #invoking the function declared
# hello()

# function named pack with three arguments and returns a single list
# def pack(cars):
#     for x in cars:
#         print(x)

# cars = ["Ferrari", "Lamborghini", "Porsche"]

# pack(cars)
# def pack(a,b,c):
#     return [a,b,c]
# print(pack("Ferrari", "Lamborghini", "Porsche"))

# function name eat_lunch, accepts a list, prints ot series of strings
def eat_lunch(list):
    if len(list) == 0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(list)):
            if i == 0:
                print(f"First I eat {list[0]}")
        else:
            print(f"Next I eat {list[1]}")

# eat_lunch([])
# eat_lunch(["sandwich"])
eat_lunch(["apple","banana","sandwich","cookie"])