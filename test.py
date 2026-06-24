# print("Hello, World!")


# def add(a, b):
#     return a + b

# result = add(3, 5)
# print(result)  # Output: 8

# def multiply(x, y):
#     return x * y

# print(multiply(4, 5))  # Output: 20

# def greet(name="World"):
#     print(f"Hello, {name}!")

# greet()        # Output: Hello, World!
# greet("Alice") # Output: Hello, Alice!

# positional arguments, 1 star
def make_pizza(*toppings):
    print("Making a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza("pepperoni", "mushrooms", "green peppers")

# keyword arguments, 2 stars
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)