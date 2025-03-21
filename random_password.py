# The goal of this script is to generate a random password for the user.
# The password will be a compound word of two concatenated strings.
import random
import FreeSimpleGUI as sg

# Returns a list of repeated words in the
# inputted list.
def check_duplicates(word_list):
    repeated_words = []
    for i in range(0 ,len(word_list)):
        verb_num = word_list.count(word_list[i])
        if verb_num > 1:
            repeated_words.append(word_list[i])
    return repeated_words

# A list of verbs.
verbs = [
    'running', 'walking', 'jogging', 'flying',
    'crying', 'yelling', 'lying', 'lying',
    'dancing', 'writing', 'thinking', 'talking',
    'singing', 'working', 'driving', 'stomping'
    ]

# A list of nouns.
nouns = [
    'chicken', 'pig', 'clown', 'dinosaur',
    'robot', 'dragon', 'viking', 'athlete',
    'grandpa', 'turtle', 'magician', 'actor',
    'grandma', 'uncle', 'tree', 'bobblehead'
    ]

# Function that generates and returns a random password.
def random_password():
    # Generates a random verb from the verbs list.
    random_verb = random.randint(0, (len(verbs) - 1))

    # Generates a random noun from the nouns list.
    random_noun = random.randint(0, (len(nouns) - 1))

    # Generates a random number 10-100
    random_number = random.randint(10, 99)

    # A concatenation of verbs and nouns creates a random word.
    random_word = verbs[random_verb] + '_' + nouns[random_noun] + str(random_number)

    return random_word

# The layout for the GUI.
layout = [[sg.Output(size=(30, 10))],
         [sg.Button('Generate')],
         [sg.Button('Exit')]]
window = sg.Window('Title', layout)

# While loop allowing the user to
# generate multiple passwords, or
# exit the program.
while True:
    event, values = window.read()
    if event == 'Exit':
        break
    if event == 'Generate':
        print(random_password())





