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
                entries = f.read().split("-"*40)
                for entry in entries:
                    if keyword.lower() in entry.lower():
                        print(entry.strip())
                        print(f"{'-'*40}")
                        found = True
                        break  # Show only the first match
                    if not found:
                        print(" No entry found with that keyword.\n")
        except FileNotFoundError:
            print(" No journal file found. Please add entries first.\n")

    def delete_all_entries(self):
        confirm = input(
            " Are you sure you want to delete all entries? (yes/no): "
        ).lower()
        if confirm == "yes":
            open("journal.txt", "w").close()
            print(" All entries deleted successfully.\n")
        else:
            print(" Deletion cancelled. Please confirm correctly.\n")

    def delete_one_entry(self):
        try:
            with open("journal.txt", "r") as f:
                entries = [e.strip() for e in f.read().split("-"*40) if e.strip()]
            if not entries:
                print(" No entries to delete.\n")
                return
            print(" Select an entry to delete:\n")
            # this code for given a number
            for i, entry in enumerate(entries, 1):
                print(f"Entry {i}:\n{entry}\n{'-'*40}")
            try:
                choice = int(input(" Enter the entry number to delete: "))
                if 1 <= choice <= len(entries):
                    entries.pop(choice - 1)
                    with open("journal.txt", "w") as f:
                        for entry in entries:
                            f.write(entry + "\n" + "-"*40 + "\n")
                    print("\n Selected entry deleted successfully.\n")
                else:
                    print(" Invalid entry number.\n")
            except ValueError:
                print(" Please enter a valid number.\n")
        except FileNotFoundError:
            print(" No journal file found. Please add entries first.\n")
   
m1 = Manager()

while True:
    print("========== Personal Journal Manager ==========")
    print("1. Add a new entry")
    print("2. View all entries")
    print("3. Search for an entry")
    print("4. Delete all entries")
    print("5. delete one entry")
    print("6. Exit")
    print("==============================================")

    try:
        option = int(input(" Please select an option (1-6): "))
        print()
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
                m1.delete_one_entry()# add extra function for one by one delete enrties
            case 6:
                print(" Exiting... Goodbye!")
                break
    except ValueError:
        print(" Invalid input! Please enter a number from 1 to 6.\n")





