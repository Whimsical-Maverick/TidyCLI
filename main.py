from organizer import organize_directory

directory_to_organize = input("Enter the complete location of the directory u want to organise: ")
moved = organize_directory(directory_to_organize)

if moved is None:
    print("-"*50 + "OPERATION ABORTED" + "-"*50)
elif moved == 0:
    print("-"*50 + "ALREADY RAN" + "-"*50)
else:
    print("-"*50 + f"SUCCESSFULLY ORGANIZED {moved} ITEMS" + "-"*50)