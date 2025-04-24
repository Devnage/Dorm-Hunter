import database

dormitoryDatabase = database.dormitoryDatabase

print(" ")
print("Welcome to Dorm Hunter")

def ask():
    print(" ")
    print("What do you want to do?")
    print("[1] - Search for dormitory")
    print("[2] - Search for dormitory with filters")
    print("[3] - List all dormitories")
    print("[4] - Optimized dorm within your preferred location")
    print("[5] - Quit Dorm Hunter")

    try:
        choice = int(input("Choice: "))
        if choice in range(1, 6):
            return choice
        else:
            reask()
    except ValueError:
        reask()

def reask():
    print(" ")
    print("Please enter 1, 2, 3, 4 or 5 only!")
    print(" ")

def dormitoryList(specified_dorms = []):
    print(" ")

    has_result = False

    for dorm, info in dormitoryDatabase.items():
        found = False
        if len(specified_dorms) != 0:
            for sdorm in specified_dorms:
                if sdorm.lower() in dorm.lower():
                    found = True
                    break
            if not found:
                continue
        
        has_result = True

        print(dorm)
        for category, value in info.items():
            displayValue = None
            if category == "Location":
                displayValue = value
            elif category == "Distance from Gate" or category == "Distance from Colleges":
                continue
            elif category == "Rate":
                bounds = list(value.values())
                if bounds[0] != bounds[1]: 
                    displayValue = "PHP {0}-{1}".format(*bounds)
                else:
                    displayValue = "PHP {0}".format(bounds[0])
            elif category == "Pax":
                bounds = list(value.values())
                if bounds[0] != bounds[1]: 
                    displayValue = "{0}-{1} persons".format(*bounds)
                else:
                    displayValue = "{0} persons".format(bounds[0])
            elif category == "Contact Details":
                print("    {0}:".format(category))
                contactDetail = list(value.items())
                for i in range(len(contactDetail)):
                    print("        {0}: {1}".format(contactDetail[i][0], contactDetail[i][1]))
                continue
            else:
                print("    {0}:".format(category))
                amenity = list(value.items())
                for i in range(len(amenity)):
                    if amenity[i][1] == True:
                        print("        {0}".format(amenity[i][0]))
                continue
            print("    {0}: {1}".format(category, displayValue))
        print(" ")

    return has_result

def find_applicable_dorm(input_category, input_value, dorms):
    applicable_dorms = {}
    for dorm, info in dorms.items():
        for category, value in info.items():
            if category  == input_category and input_category == "Location":
                if input_value == "Any":
                    applicable_dorms[dorm] = info
                    break
                if value == input_value:
                    applicable_dorms[dorm] = info
                    break
            elif category == input_category and input_category == "Rate":
                if input_value >= list(value.values())[0]:
                    applicable_dorms[dorm] = info
                    break
            elif category == input_category and input_category == "Pax":
                if input_value >= list(value.values())[0]:
                    applicable_dorms[dorm] = info
                    break
            elif category == input_category and input_category == "Amenities":
                has_result = True
                for input in input_value:
                    if value[input[0]] != input[1]:
                        has_result = False
                        break
                if has_result:
                    applicable_dorms[dorm] = info

    return applicable_dorms

def askContinue():
    print(" ")
    print("Type \"y\" (case-insensitive) if yes. Press Enter or anything otherwise.")
    if bool(input("Do you want to continue using Dorm Hunter? ").lower() == "y"):
        main()

def update_applicable_dorm(previous, current, done = False):
    previousList = list(previous.keys())
    currentList = list(current.keys())

    if done and len(currentList) != 0:
        dormitoryList(currentList)
        print("Results found! These dormitories are in your preferences: {0}".format(currentList))
        print(" ")
    elif len(currentList) > 1:
        print(" ")
        print("Current applicable dorms: {0}".format(currentList))
        print(" ")      
        return True
    elif len(currentList) == 1:
        dormitoryList(currentList)
        print("Only one result left. Check the result!")
        print(" ")
        return False
    else:
        dormitoryList(previousList)
        print("No results found. Check previous results")
        print(" ")
        return False
    
def main():
    method = None
    while method == None:
        method = ask()

    if method == 1:
        print(" ")
        dormName = input("Input name here: ")
        if not dormitoryList([dormName]):
            print("{0} not found in database.".format(dormName))
            askContinue()
        else:
            askContinue()
    elif method == 2:
        applicable_dorms = {}

        print(" ")
        print("1 - {0}, 2 - {1}, 3 - {2}, 4 - {3}, 5 - {4}".format(*database.locations))

        location = None
        while location not in range(1, len(database.locations) + 1):
            try:
                location = int(input("[Location] What is your preferred location? "))
                if location not in range(1, len(database.locations) + 1):
                    print(" ")
                    print("Please enter 1, 2, 3, 4, or 5 only!")
                    print(" ")
                    print("1 - {0}, 2 - {1}, 3 - {2}, 4 - {3}, 5 - {4}".format(*database.locations))
            except ValueError:
                print(" ")
                print("Please enter 1, 2, 3, 4, or 5 only!")
                print(" ")
                print("1 - {0}, 2 - {1}, 3 - {2}, 4 - {3}, 5 - {4}".format(*database.locations))

        placeholder_applicable_dorms = find_applicable_dorm("Location", database.locations[location - 1], dormitoryDatabase)

        if update_applicable_dorm(applicable_dorms, placeholder_applicable_dorms):
            rate = None
            while not type(rate) == int:
                try:
                    rate = int(input("[Rate] What is your maximum budget? "))
                    if rate < 0:
                        rate = None
                        print(" ")
                        print("Please enter positive integers only.")
                        print(" ")
                except ValueError:
                    print(" ")
                    print("Please enter positive integers only.")
                    print(" ")
            applicable_dorms = find_applicable_dorm("Rate", rate, placeholder_applicable_dorms)
        else:
            askContinue()
            return

        if update_applicable_dorm(placeholder_applicable_dorms, applicable_dorms):
            pax = None
            while not type(pax) == int:
                try:
                    pax = int(input("[Pax] What is your preferred maximum pax? "))
                    if pax < 0:
                        pax = None
                        print(" ")
                        print("Please enter positive integers only.")
                        print(" ")
                except ValueError:
                    print(" ")
                    print("Please enter positive integers only.")
                    print(" ")
            placeholder_applicable_dorms = find_applicable_dorm("Pax", pax, applicable_dorms)
        else:
            askContinue()
            return

        if update_applicable_dorm(applicable_dorms, placeholder_applicable_dorms):
            print("Type \"y\" (case-insensitive) if you prefer the following amenities. Press Enter or anything otherwise.")
            input_amenities = []

            for amenity in database.amenities:
                preferred = bool(input("[Amenities] {0}? ".format(amenity)).lower() == "y")
                if preferred:
                    input_amenities.append((amenity, preferred))

            applicable_dorms = find_applicable_dorm("Amenities", input_amenities, placeholder_applicable_dorms)
            update_applicable_dorm(placeholder_applicable_dorms, applicable_dorms, True)
            askContinue()
        else:
            askContinue()
    elif method == 3:
        dormitoryList()
        askContinue()
    elif method == 4:
        print(" ")
        print("1 - {0}, 2 - {1}, 3 - {2}, 4 - {3}".format(*database.locations[:4]))
        location = None
        while location not in range(1, len(database.locations)):
            try:
                location = int(input("[Location] What is your preferred location? "))
                if location not in range(1, len(database.locations)):
                    print(" ")
                    print("Please enter 1, 2, 3, or 4 only!")
                    print(" ")
                    print("1 - {0}, 2 - {1}, 3 - {2}, 4 - {3}".format(*database.locations[:4]))
            except ValueError:
                print(" ")
                print("Please enter 1, 2, 3, or 4 only!")
                print(" ")
                print("1 - {0}, 2 - {1}, 3 - {2}, 4 - {3}".format(*database.locations[:4]))

        print(" ")
        print("1 - {0}, 2 - {1}, 3 - {2}, 4 - {3}, 5 - {4}, 6 - {5}, 7 - {6}, 8 - {7}".format(*database.colleges))
 
        college = None
        while college not in range(1, len(database.colleges) + 1):
            try:
                college = int(input("[College] What is your college? "))
                if college not in range(1, len(database.colleges) + 1):
                    print(" ")
                    print("Please enter integers 1 - 8 only!")
                    print(" ")
                    print("1 - {0}, 2 - {1}, 3 - {2}, 4 - {3}, 5 - {4}, 6 - {5}, 7 - {6}, 8 - {7}".format(*database.colleges))
            except ValueError:
                print(" ")
                print("Please enter integers 1 - 8 only!")
                print(" ")
                print("1 - {0}, 2 - {1}, 3 - {2}, 4 - {3}, 5 - {4}, 6 - {5}, 7 - {6}, 8 - {7}".format(*database.colleges))

        loc_applicable_dorms = find_applicable_dorm("Location", database.locations[location - 1], dormitoryDatabase)
        distOptimizedDorms = {}
        if location == 1:
            for dorm, item in loc_applicable_dorms.items():
                for category, value in item.items():
                    if category == "Distance from Colleges":
                        distOptimizedDorms[dorm] = list(value.values())[college - 1]
        else:
            for dorm, item in loc_applicable_dorms.items():
                for category, value in item.items():
                    if category == "Distance from Gate":
                        distOptimizedDorms[dorm] = value + database.distanceOfCollegesFromGate[database.colleges[college - 1]]          

        distOptimizedDorms = sorted((distance, dorm) for (dorm, distance) in distOptimizedDorms.items())
        minDistance = distOptimizedDorms[0][0]
        minDorms = [dorm for distance, dorm in distOptimizedDorms if distance == minDistance]
        dormitoryList(minDorms)

        print("The distances are as follows: ")
        
        for distance, dorm in distOptimizedDorms:
            print("{0}: {1}m".format(dorm, distance))
        print(" ")
        print("The optimal dormitory for you is/are: {0}".format(", ".join(minDorms)))

        print(" ")
        print("Type \"y\" (case-insensitive) if yes. Press Enter or anything otherwise.")
        if bool(input("Do you want to filter these dormitories by your preferences? ").lower() == "y"):
            applicable_dorms = {}
            placeholder_applicable_dorms = loc_applicable_dorms
            if update_applicable_dorm(applicable_dorms, placeholder_applicable_dorms):
                rate = None
                while not type(rate) == int:
                    try:
                        rate = int(input("[Rate] What is your maximum budget? "))
                        if rate < 0:
                            rate = None
                            print(" ")
                            print("Please enter positive integers only.")
                            print(" ")
                    except ValueError:
                        print(" ")
                        print("Please enter positive integers only.")
                        print(" ")
                applicable_dorms = find_applicable_dorm("Rate", rate, placeholder_applicable_dorms)
            else:
                askContinue()
                return

            if update_applicable_dorm(placeholder_applicable_dorms, applicable_dorms):
                pax = None
                while not type(pax) == int:
                    try:
                        pax = int(input("[Pax] What is your preferred maximum pax? "))
                        if pax < 0:
                            pax = None
                            print(" ")
                            print("Please enter positive integers only.")
                            print(" ")
                    except ValueError:
                        print(" ")
                        print("Please enter positive integers only.")
                        print(" ")
                placeholder_applicable_dorms = find_applicable_dorm("Pax", pax, applicable_dorms)
            else:
                askContinue()
                return

            if update_applicable_dorm(applicable_dorms, placeholder_applicable_dorms):
                print("Type \"y\" (case-insensitive) if you prefer the following amenities. Press Enter or anything otherwise.")
                input_amenities = []

                for amenity in database.amenities:
                    preferred = bool(input("[Amenities] {0}? ".format(amenity)).lower() == "y")
                    if preferred:
                        input_amenities.append((amenity, preferred))

                applicable_dorms = find_applicable_dorm("Amenities", input_amenities, placeholder_applicable_dorms)
                update_applicable_dorm(placeholder_applicable_dorms, applicable_dorms, True)
                askContinue()
            else:
                askContinue()
        else:
            askContinue()
    else:
        print(" ")
        print("Thank you for using Dorm Hunter!")
        return
    
if __name__ == "__main__":
    main()