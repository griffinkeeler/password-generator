import random

# The goal of this script is to generate a random password for the user.

# The password will be a compound word of two concatenated strings.

# A list of verbs.
verbs = [
    'running', 'walking', 'jogging', 'flying',
    'crying', 'yelling', 'lying', 'dancing',
    'writing', 'thinking', 'talking', 'singing',
    'singing', 'singing'
    ]


# Counts the number of times a verb appears in the list. 
# TODO: Turn into function. 
for i in range(0 ,len(verbs)):
    print(verbs[i])
    verb_num = verbs.count(verbs[i])
    print(verb_num)

# A list of nouns.
nouns = [
    'chicken', 'pig', 'clown', 'dinosaur',
    'robot', 'dragon', 'viking', 'athlete',
    'grandpa', 'turtle', 'magician', 'actor'
]

# Generates a random verb from the verbs list.
random_verb = random.randint(0, (len(verbs) - 1))

# Generates a random noun from the nouns list.
random_noun = random.randint(0, (len(nouns) - 1))

# Generates a random number 10-100
random_number = random.randint(10, 100)

# A concatenation of verbs and nouns creates a random password.
random_password = verbs[random_verb] + '_' + nouns[random_noun] + str(random_number)


print(random_password)
