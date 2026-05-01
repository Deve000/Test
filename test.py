print("Hello, World!")

name = input("\nWhat name would you like me to use? ")
print(f"\nGot it. Hi there, {name}!")

print("\nMenu:")
print("1. Enter world")
print("2. Exit world")

choice = int(input("\nWhat would you like to do today? "))

if choice == 1:
    print("\n>> Entering world, please standby...")
elif choice == 2:
    print("\n>> Exiting world, see you again!")
else:
    print("Choice unavailable, please choose again~")