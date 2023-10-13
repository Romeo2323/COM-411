


print("how many apples should I remove?")

apples = int (input())
count = 1

while count <= apples:

    count = count+1
    print("Removed apples.")


print("How many obstacles should I avoid?")

obstacles = int (input())
count = 1

while count <= obstacles:

    print(f"Avoiding...Done! {count} obstacles avoided")
    count = count + 1
print("All obstacles have been avoided.")

print("How many bars should be charged?")

bars = int (input())
count = 1

while count <= bars:
    print(f"Charging: {'█'*count}")
    count +=1





