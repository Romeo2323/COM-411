
# SectionA 1

print("--------------------------")
print("Disneyland Review Analyser")
print("--------------------------")
# SectionA 2

def load_data(file_path):
    with open (file_path):
         csv_reader = csv.reader(csv_file)
         next (csv_reader)

         for line in csv_reader:
             record.append(line)
    print("Data has completed processing")

# SectionA 3
menu = {
    '[A]': "View Data",
    '[B]': "Visualise Data",
    '[C]': "Exit",
}

# Making menu
while True:
    print("Menu")
    for key, value in menu.items():
        print(f"{key}: {value}")
    users_choice = input("Please Enter An Option: ").upper()











