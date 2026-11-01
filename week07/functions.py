#SELF ASSESMENT QUESTIONS
#1. The first I spotted came from the traceback. When I ran the code in the broken file python gave me back a SyntaxError and it highlighted the 2nd for loop. Since we went over it in class it was easy to see that the colon was missing and it gave me the line number as well. I think that puts me in pretty good shape about my debugging insticnts because it was pretty easy to see where the bug was since the code tells me itself. I definitely do need to work on checking when my code runs well but does not give the write answer though.
#2. apply_discount(price, tier) takes in a price and a tier and then gives the final price after the discount of the specific tier associated with it. SO like 15% off for gold, 10% off for silver, and 5% off for bronze. If there is anothr tier not inlcluded then it gets no discount so the price is the same. I think a colleague could use it without reading the actual code because a lot of the inputs explain what the code does anyway.
#3.I used AI to help me find the last bug in exercise 5 which was the the off-by one error. I was able to find the other two bugs on my own but I was having a hard time finding the last one. I think that is a good use of AI because it helped me find the bug and then I was able to understand it and fix it myself. I think that is a good way to use AI because it helps you learn and understand the code better.

#  Exercise 1 
def calculate_tax(price, rate):
    """Return the tax owed on a price at the given rate (e.g. 0.07 for 7%)."""
    return price * rate


print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")


# Exercise 2 
def apply_discount(price, tier):
    """Return the price after the tier discount (gold 15%, silver 10%, bronze 5%)."""
    if tier == "gold":
        return price * (1 - 0.15)
    elif tier == "silver":
        return price * (1 - 0.10)
    elif tier == "bronze":
        return price * (1 - 0.05)
    else:
        return price


print(f"gold:   ${apply_discount(200, 'gold'):.2f}")
print(f"silver: ${apply_discount(200, 'silver'):.2f}")
print(f"bronze: ${apply_discount(200, 'bronze'):.2f}")
print(f"none:   ${apply_discount(200, 'none'):.2f}")


# Exercise 3
discounted = apply_discount(200, "gold")
print(f"After gold discount: ${discounted:.2f}")
taxed = discounted + calculate_tax(discounted, 0.07)
print(f"After tax: ${taxed:.2f}")


def final_price(price, tier, tax_rate):
    """Return the price after applying the tier discount, then adding tax."""
    discounted_price = apply_discount(price, tier)
    return discounted_price + calculate_tax(discounted_price, tax_rate)


print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')


#Exercise 4 -
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")


# Exercise 5
# FiXed version of broken_sales.py. Three bugs:
#   1. Logic bug: total = sale replaced the total every time, so it ended up keeping
#      the last sale only. Fix: use total += sale to add to each individual sale. 
#   2. Syntax bug: the second for loop was missing its colon. Fix: add :.
#   3. Off-by-one bug: while i <= len(sales) ran one time extra and was the reasoning behind the IndexError
#    Fix: use i < len(sales).
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale  # fix 1: was `total = sale`
print(f"Total: ${total}")

count = 0
for sale in sales:  # fix 2: added missing colon
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):  # fix 3: was `<=`
    print(sales[i])
    i += 1


# Exercise 6 
# Scope explanation:
# Scope is the specific area of the program where a variable can be defined
# The x = 100 is outside the function which makes it a global variable, while the x = 999 inside the double_it() is a local variable that only exists while the function is running. Assigning to x inside the function makes a new local variable, rather than changing the global one, so the global x stays 100.
# Predicted output: 100, 1998, then 100.
x = 100  # global variable


def double_it():
    x = 999  # local variable — different from global x!
    return x * 2


print(x)            # 100
print(double_it())  # 1998
print(x)            # 100 (global x is unchanged)