COLOR_NAMES = {'AliceBlue': '#f0f8ff', 'Black': '#000000', 'Chartreuse1': '#7fff00',
                'Cornsilk4': '#8b8878', 'DarkOrchid4': '#68228b', 'DeepPink3': '#cd1076',
                'Aquamarine4': '#458b74', 'Bisque2': '#eed5b7', 'Blue2': '#0000ee',
               'Burlywood4': '#8b7355'}
list_key = ["AliceBlue", "Black", "Chartreuse1", "Cornsilk4", "DarkOrchid4", "DeepPink3", "Aquamarine4", "Bisque2", "Blue2", "Burlywood4"]
print(list_key)
color = input("Enter color name: ").title()
while color != "":
    if color in COLOR_NAMES:
        print(color, "is", COLOR_NAMES[color])
    else:
        print("Invalid color")
    color = input("Enter color name: ").title()
