
#              PR6   file opreters


from datetime import datetime


class Manager:
    def __init__(self):
        pass

    def add_entry(self):
        now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        entry = input("Enter your journal entry: ")
        with open("journal.txt", "a") as f:
            f.write(f"Date: {now}\n")
            f.write(f"Entry: {entry}\n")
            f.write(f"{'-'*40}\n")
        print(" Journal entry added successfully.\n")

    def view_all_entry(self):
        try:
            with open("journal.txt", "r") as f:
                content = f.read()
                if content.strip() == "":
                    print("No journal entries found.\n")
                else:
                    print(" All Journal Entries:\n")
                    print(content)
        except FileNotFoundError:
            print(" No 'journal.txt' file found.\n")

    def search_entry(self):
        keyword = input(" Enter keyword to search: ")
        found = False
        try:
            with open("journal.txt", "r") as f:
                entries = f.read().split("----------------------------------------")
                for entry in entries:
                    if keyword.lower() in entry.lower():
                        print(entry.strip())
                        print(f"{'-'*40}")
                        found = True
            if not found:
                print(" No entry found with that keyword.\n")
        except FileNotFoundError:
            print(" No journal file found. Please add entries first.\n")

    def delete_all_entries(self):
        confirm = input(
            "⚠ Are you sure you want to delete all entries? (yes/no): "
        ).lower()
        if confirm == "yes":
            open("journal.txt", "w").close()
            print(" All entries deleted successfully.\n")
        else:
            print(" Deletion cancelled. Please confirm correctly.\n")


# Main program starts here
m1 = Manager()

while True:
    print("========== Personal Journal Manager ==========")
    print("1. Add a new entry")
    print("2. View all entries")
    print("3. Search for an entry")
    print("4. Delete all entries")
    print("5. Exit")
    print("==============================================")

    try:
        option = int(input(" Please select an option (1-5): "))
        print()  # for spacing
        match option:
            case 1:
                m1.add_entry()
            case 2:
                m1.view_all_entry()
            case 3:
                m1.search_entry()
            case 4:
                m1.delete_all_entries()
            case 5:
                print(" Exiting... Goodbye!")
                break
            case _:
                print(" Invalid option. Please choose between 1-5.\n")
    except ValueError:
        print(" Invalid input! Please enter a number from 1 to 5.\n")
