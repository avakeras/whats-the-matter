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

    i = 0
    sumC = 0
    sumH = 0
    for i in range(len(mol)):
        if mol[i] == "C":
            if mol[i + 1].isnumeric() == True:
                sumC += int(mol[i + 1])
            else:
                sumC += 1
        if mol[i] == "H" and mol[i] != mol[-1]:
            if mol[i + 1].isnumeric() == True:
                sumH += int(mol[i + 1])
            else:
                sumH += 1     
        i += 1    

    def prefix(sumC):
        if sumC == 1:
            return (" methan")
        if sumC == 2:
            return ("n ethan")
        if sumC == 3:
            return (" propan")
        if sumC == 4:
            return (" butan")
        if sumC == 5:
            return (" pentan")
        if sumC == 6:
            return (" hexan")
        if sumC == 7:
            return (" heptan")
        if sumC == 8:
            return (" octan")
        if sumC == 9:
            return (" nonan")
        
    def statement(sumC):
        return ("This is a" + prefix(sumC))
        
    if mol[-2] == "H" and mol[-1] == "O": 
       print(statement(sumC) + "al molecule!") #aldehyde
       break
    if mol[-2] == "O" and mol[-1] == "H": 
        if mol[-3] != "O":
            print(statement(sumC) + "ol molecule!") #alcohol
            break
        else:
            print(statement(sumC) + "oic acid molecule!") #carboxylic acid
            break

    if "O" in mol:
        if mol[mol.find("O") - 1] == "O" or mol[mol.find("O") + 1] == "O":
            print("This molecule is an ester!") #ester
            break
        elif mol[mol.find("O") - 1] == "C":
            print(statement(sumC) + "one molecule!") #ketone
            break
        else:
            print("This molecule is an ether!") #ether
            break

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

