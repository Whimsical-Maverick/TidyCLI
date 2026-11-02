from organizer import organize_directory, undo_moves

while True:
    print("\n1) Organize  2) Undo  3) Exit")
    choice = input("Choose: ").strip()

    if choice == "3":
        print("Bye!")
        break
    if choice not in ("1", "2"):
        print("Invalid choice, try again.")
        continue

    directory = input("Enter the complete location of the directory: ").strip().strip('"')

    if choice == "1":
        moved = organize_directory(directory)
        if moved is None:
            print("-"*50 + "OPERATION ABORTED" + "-"*50)
        elif moved == 0:
            print("-"*50 + "ALREADY RAN" + "-"*50)
        else:
            print("-"*50 + f"SUCCESSFULLY ORGANIZED {moved} ITEMS" + "-"*50)
    else:
        n = undo_moves(directory)
        print("-"*50 + f"RESTORED {n} ITEMS" + "-"*50)