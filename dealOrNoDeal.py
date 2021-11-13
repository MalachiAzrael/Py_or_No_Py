import random
import os

boxes = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0,
         12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0, 21: 0, 22: 0}
monies = [0.01, 0.1, 0.5, 1, 5, 10, 50, 100, 250, 500, 750, 1000, 3000, 5000, 10000, 15000, 20000, 35000, 50000, 75000,
          100000, 250000]
round_list = [16, 13, 10, 7, 4, 1]
offer = 0
average_value = 0
testing_mode = bool(int(input("Is this a test? ")))
choice = ""
do_swap = ""


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def validation(input_val, lowest=-9001, highest=9001):
    if not str(input_val).isnumeric():
        raise Exception
    input_val = int(input_val)
    if input_val < lowest or input_val > highest:
        raise Exception
    return input_val


def eliminate_val(input_val):
    input_val = int(input_val)
    if input_val not in boxes.keys():
        raise Exception
    return input_val


def banker():
    global offer, average_value
    remaining_value = 0
    for n in boxes.values():
        remaining_value = remaining_value + n
    remaining_value = remaining_value + chosen_value
    average_value = remaining_value / (len(boxes) + 1)
    offer = int(round(average_value, -3 if average_value >= 1000 else -1))
    #todo random fudging


for i in boxes:
    r = random.randint(0, (len(monies) - 1))
    boxes[i] = monies.pop(r)

while True:
    try:
        chosen_box = validation(input("Please Choose a Box (1, 22): "), 1, 22)
        chosen_value = boxes.pop(chosen_box)
        break
    except Exception:
        print("Try another box (1, 22): ")

for current_round in round_list:
    if testing_mode:
        boxes = {21: 100}
        banker()
        choice = "No Deal"
        break

    while len(boxes) > current_round:
        try:
            banker()
            popped_value = boxes.pop(eliminate_val(input("Choose box to remove: ")))
            clear()
            print("Box removed was worth", popped_value)
            if popped_value > average_value:
                print("Ouch that hurt your average")
            else:
                print("That's ok, you needed to get rid of that one")
            #todo various phrases based on value
            print("Remaining Boxes:", list(boxes))
            print("Remaining Values:", sorted(list(boxes.values())))
            continue
        except Exception:
            print("That box has already been taken")
    banker()
    print("Banker Offer: ", offer)

# Deal or No Deal
    while True:
        choice = input("Deal or No Deal?: ")
        if choice == "Deal" or choice == "No Deal":
            break
        else:
            print("That's not an option")

    if choice == "Deal":
        break
    elif choice == "No Deal":
        continue

if choice == "Deal":
    if chosen_value <= offer:
        print("You beat the banker")
    else:
        print("The Banker conned you")
else:
    final_box = boxes.popitem()
    print("Box %i remains" % final_box[0])

    while not do_swap == "Yes" or do_swap == "No":
        do_swap = input("Would you like to swap? ")

    if do_swap == "Yes":
        discarded_box = chosen_box
        discarded_value = chosen_value
        chosen_box = final_box[0]
        chosen_value = final_box[1]

    print("Your Box: %i, contains: %i" % (chosen_box, chosen_value))
    print("Your last offer was", offer)
    if offer > chosen_value:
        print("You could have won more")
    else:
        print("You Beat the Banker!!!!!!")

# print("Testing")
# print("Boxes:", boxes)
# print("Money:", monies)
# print("Chosen value:", chosen_value)
# print("Chosen box:", chosen_box)
# print("Done")
