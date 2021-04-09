invited_names_path = './input/names/invited_names.txt' # Path to  invitation list file

letter_path = './input/letters/meeting_invitation.txt' # Path to  invitation letter file

invited_names = []
output_letters = './output/'    # Path to  store the generated letters

with open(invited_names_path) as reader:
        invited_names = reader.readlines()

with open(letter_path) as reader:
        letter = reader.read()


new_invited_names = []
for name in invited_names:
    new_invited_names.append(name.strip('\n'))


new_letter = ''

for name in new_invited_names:
    new_letter = letter.replace('[name]', name)
    file_name = name + ".txt"
    with open(output_letters + file_name, 'w') as writer:
        writer.write(new_letter)


print("Task Successful.  Please check the output folder to find the generated mails.")