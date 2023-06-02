#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp



with open("Day_24/Mail Merge Project Start/Input/Names/invited_names.txt") as names:
    for name in names.readlines():
        recipient = name.strip()
        with open("Day_24/Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter:
            for line in letter.readlines():
                with open(f"Day_24/Mail Merge Project Start/Output/ReadyToSend/letter_to_{recipient}.txt", mode="a") as prepared:
                    if "[name]" in line:
                        prepared.write(line.replace("[name]", recipient))
                    else:
                        prepared.write(line)



