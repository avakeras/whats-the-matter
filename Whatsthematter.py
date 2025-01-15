#Welcome to Whatsthematter!

# Does not work with amines or amides, halogenoalkanes, nor molecules with more than one functional group (including double and triple bonds).
# Cannot print specific names for esters or ethers due to potential side chains and more complicated nomenclature.
# Ensure all letters of the strucutral formula are in uppercase, as this is how structural formulae are written.
# Feel free to try this with condensed formulae too!

class WhatsTheMatter:
    def __init__(self, mol):
        self.mol = mol
        self.sumC = 0
        self.sumH = 0
        
    mol = input("Enter the molecular formula for an organic compound:")

    # Counts number of carbon and hydrogen molecules
    sumC = sumH = 0
    for i in range(len(mol)):
        if mol[i] == "C":
            sumC += int(mol[i + 1]) if mol[i + 1].isnumeric() else 1
        elif mol[i] == "H" and (i + 1 < len(mol)) and mol[i + 1].isnumeric():
            sumH += int(mol[i + 1])
        elif mol[i] == "H":
            sumH += 1

    # Assigns prefix based on carbon chain length
    def prefix(sumC):
        prefixes = ["", " methan", "n ethan", " propan", " butan", " pentan", " hexan", " heptan", " octan", " nonan"]
        return prefixes[sumC] if 1 <= sumC <= 9 else ""

    # Makes a statement so I don't need to keep writing it
    def statement(prefix, sumC):
        return ("This is a" + prefix(sumC))

    # Troubleshooting stuff
    if mol == "" or "C" not in mol:
        print("Where's your molecule? Try again!")
        
    # Identifies functional groups with -OH ending
    elif mol.endswith("OH"):
        if mol[-3] == "O":
            print(statement(prefix, sumC) + "oic acid molecule!")  # Carboxylic acids
        else:
            print(statement(prefix, sumC) + "ol molecule!")  # Alcohols

    # Identifies functional group with -HO ending
    elif mol.endswith("HO"):
        print(statement(prefix, sumC) + "al molecule!")  # Aldehydes

    # Identifies other functional groups containing "O"
    elif "O" in mol:
        o_pos = mol.find("O")
        if mol[o_pos - 1] == "O" or mol[o_pos + 1] == "O":
            print("This molecule is an ester!")  # Esters
        elif mol[o_pos - 1] == "C":
            print(statement(prefix, sumC) + "one molecule!")  # Ketones
        else:
            print("This molecule is an ether!")  # Ethers

    # If no functional groups present, assigns the molecule as an alkane, alkene, or alkyne
    # Doesn't work for sums of C and H over 9
    # Doesn't work for molecules with more than one double / triple bond
    elif sumC == (sumH/2): # Alkenes
        print("This is a" + prefix(sumC).replace(prefix(sumC)[-2], "e")+ "e molecule!")
    elif sumC == ((sumH+2) / 2): # Alkynes
        print("This is a" + prefix(sumC).replace(prefix(sumC)[-2], "y")+ "e molecule!")
    elif sumC == ((sumH-2) / 2): # Alkanes
        print("This is a" + prefix(sumC) + "e molecule!")    
    elif sumC == 6 and sumH == 6: # Benzene
        print("This is a benzene molecule!")
    else: 
        print("Either you did not type an organic molecule, or the one you typed is not compatible with WhatsTheMatter. Try again!")
