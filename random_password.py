import random

# The goal of this script is to generate a random password for the user.

# The password will be a compound word of two concatenated strings.

# A list of verbs.
verbs = [
    'running', 'walking', 'jogging', 'flying',
    'crying', 'yelling', 'lying', 'dancing'
    ]

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

# A concatenation of verbs and nouns creates a random password.
random_password = verbs[random_verb] + '_' + nouns[random_noun]


print(random_password)
