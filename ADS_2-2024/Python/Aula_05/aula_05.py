# Data input
age = int(input("Type a valid age in positive integer: "))

# If age is less than 0, print "Not born".
if age < 0:
    print("Not born.")
# If not, verify other condition.
else:
    # If age is less than 16, print "Do not vote".
    if age < 16:
        print("Do not vote.")
    # If not, verify other condition.
    else:
        # If age is less than 18, print "Optional vote".
        if age < 18:
            print("Optional vote.")
        # If not, verify other condition.
        else:
            # If age is less than 61, verify other conditions in if block.
            if age < 61:
                # If age equals 37, print "Wins prize and don't vote".
                if age == 37:
                    print("Wins prize and don't vote.")
                # If not, print "Mandatory vote".
                else:
                    print("Mandatory vote.")
            # If not is less than 61, verify other condition.
            else:
                # If age equals 74, print "Mandatory vote, and wins prize".
                if age == 74:
                    print("Mandatory vote, e ganha brinde.")
                # If not, print "Optional vote".
                else:
                    print("Optional vote.")