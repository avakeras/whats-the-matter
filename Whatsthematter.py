#Welcome to Whatsthematter!

# Does not work with amines or amides, halogenoalkanes, nor molecules with more than one functional group (including double and triple bonds).
# Cannot print specific names for esters or ethers due to potential side chains and more complicated nomenclature.
# Ensure all letters of the strucutral formula are in uppercase. 

while True:
    mol = input("Enter the molecular formula for an organic compound:")

    if mol == "":
        print("Where's your molecule? Try again!")
        continue

    if "C" not in mol:
        print("This is not an organic molecule :( Try again!")
        continue

    # Counts number of carbon and hydrogen molecules
    sumC = sumH = 0
    for i in range(len(mol)):
        if mol[i] == "C":
            sumC += int(mol[i + 1]) if mol[i + 1].isnumeric() else 1
        elif mol[i] == "H" and (i + 1 < len(mol)) and mol[i + 1].isnumeric():
            sumH += int(mol[i + 1])
        elif mol[i] == "H":
            sumH += 1

    # Assigns proper prefix based on number of carbon molecules
    def prefix(sumC):
        prefixes = ["", " methan", "n ethan", " propan", " butan", " pentan", " hexan", " heptan", " octan", " nonan"]
        return prefixes[sumC] if 1 <= sumC <= 9 else ""
        
    def statement(sumC):
        return ("This is a" + prefix(sumC))
        
    # Identifies functional groups with -OH ending
    if mol.endswith("OH"):
        if mol[-3:] == "O":
            print(statement(sumC) + "oic acid molecule!")  # carboxylic acid
        else:
            print(statement(sumC) + "ol molecule!")  # alcohol
        break

    # Identifies functional group with -HO ending
    if mol.endswith("HO"):
        print(statement(sumC) + "al molecule!")  # aldehyde
        break

    # Identifies other functional groups containing "O"
    if "O" in mol:
        o_pos = mol.find("O")
        if mol[o_pos - 1] == "O" or mol[o_pos + 1] == "O":
            print("This molecule is an ester!")  # ester
        elif mol[o_pos - 1] == "C":
            print(statement(sumC) + "one molecule!")  # ketone
        else:
            print("This molecule is an ether!")  # ether
        break

    # If no functional groups present, assigns the molecule as an alkane, alkene, or alkyne
    # Doesn't work for sums of C and H over 9
    # Doesn't work for molecules with more than one double / triple bond
    if sumC == (sumH/2): #alkene
        print("This is a" + prefix(sumC).replace(prefix(sumC)[-2], "e")+ "e molecule!")
        break
    if sumC == ((sumH+2) / 2): #alkyne
        print("This is a" + prefix(sumC).replace(prefix(sumC)[-2], "y")+ "e molecule!")
        break
    if sumC == ((sumH-2) / 2): #alkane
        print("This is a" + prefix(sumC) + "e molecule!")
        break
    if sumC == 6 and sumH == 6: #benzene
        print("This is a benzene molecule!")
        break

