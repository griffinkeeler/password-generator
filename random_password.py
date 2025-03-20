# The goal of this script is to generate a random password for the user.
# The password will be a compound word of two concatenated strings.

import random

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

# Generates a random verb from the verbs list.
random_verb = random.randint(0, (len(verbs) - 1))

# Generates a random noun from the nouns list.
random_noun = random.randint(0, (len(nouns) - 1))

# Generates a random number 10-100
random_number = random.randint(10, 99)

# A concatenation of verbs and nouns creates a random password.
random_password = verbs[random_verb] + '_' + nouns[random_noun] + str(random_number)

print(random_password)

