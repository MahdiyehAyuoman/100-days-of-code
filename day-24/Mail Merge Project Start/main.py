#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

def read_file_starting_letter(file_path):
    with open(file_path, "r") as f:
        return str(f.read())

def read_file_name(file_path):
    with open(file_path, "r") as name:
        return name.readlines()


def write_email_file(file_path, data):
    with open(file_path, 'w') as output:
           return output.write(data)

starting_letter = read_file_starting_letter('7. Mail Merge Project Start\Mail Merge Project Start\Input\Letters\starting_letter.txt')

## Manage with invited_names data to make a lists of names
invited_names = read_file_name('7. Mail Merge Project Start//Mail Merge Project Start//Input//Names//invited_names.txt')
names_list = []
for line in invited_names:
    name = line.split()
    names_list.append(name)

## Loop for change the names from invited_names data to starting_letter data
for name in names_list:
    # print(name)
    name = str(name).strip("[' ']")
    email = starting_letter.replace('[name]', name)
    print(email)
    output = write_email_file((f"7. Mail Merge Project Start\Mail Merge Project Start\Output\ReadyToSend\letter_for_{name}.txt"), email)

