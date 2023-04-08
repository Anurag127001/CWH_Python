speed = int(input("Enter the current speed of your vehicle : "))
if 0.1 < speed <=15:
    print("Keep vehicle on First gear")
elif 15 < speed <=25:
    print("Keep vehicle on Second gear")
elif 25 < speed <=35:
    print("Keep vehicle on Third gear")
elif 35 < speed <=45:
    print("Keep vehicle on Fourth gear")
elif 45 < speed:
    print("Keep vehicle on Fifth gear")
else:
    print("Keep your vehicle Neutral")

''' To Make Automatic gear suggester for new learners ; print statements will be shown on digital display, and input will be automatically taken from speedometer of the vehicle'''