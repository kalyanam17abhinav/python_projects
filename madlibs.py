#making madlibs project using string concatenation
#string concat = add strings
# youtube = "make me a youtuber"
# print(youtube)

# example:
# adj = input("adjective: ")
# verb1 =input("verb 1: ")
# verb2 =input("verb 2: ")
#
# madlib =(f"When he saw Julian coming {adj}, he knocked on the young man and {verb1} to prevent any mishap and then slowly {verb2} too fast")
#
# print(madlib)

print("### MADLIBS GAME ###")
print("1. Space Comedy\n2. Fantasy Mystery\n3. Superhero Romance\n4. Historical Sci-Fi\n5. Apocalyptic Humor")
choice = input("Enter the selected number: ")

if(choice=='1'):
    name = input("Enter a name: ")
    adjective1 = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    exclamation = input("Enter an exclamation: ")
    plural_noun = input("Enter a plural noun: ")
    emotion = input("Enter an emotion: ")
    verb = input("Enter a verb: ")
    random_object = input("Enter a random object: ")
    adjective2 = input("Enter another adjective: ")
    ridiculous_situation = input("Enter a ridiculous situation: ")

    # Filling the template
    story = f"Captain {name} accidentally pressed the {adjective1} button, launching the spaceship straight into a {noun} field.\n '{exclamation}!' shouted the crew, while the alien {plural_noun} laughed in {emotion}.\n To fix the issue, the team had to {verb} with a {random_object}.\n '{name}, you’re the {adjective2} captain we’ve ever had,' joked the robot.\n 'Well,' {name} said, 'at least it’s not {ridiculous_situation}.'"

    print(story)

elif(choice=='2'):
    place = input("Enter a place: ")
    adjective1 = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    name = input("Enter a name: ")
    object1 = input("Enter an object: ")
    adjective2 = input("Enter another adjective: ")
    exclamation = input("Enter an exclamation: ")
    noun2 = input("Enter another noun: ")
    creature = input("Enter a creature: ")
    verb = input("Enter a verb: ")
    plot_twist = input("Enter a plot twist: ")

    # Filling the template
    story = f"In the enchanted forest of {place}, a {adjective1} creature left behind a {noun1} as a clue. \
    The wizard {name} deciphered it using a {object1}, revealing the {adjective2} truth. \
    '{exclamation},' gasped the knights, 'it leads to the {noun2} of secrets!' \
    But as they approached, the {creature} blocked their way, demanding {verb}. \
    '{name},' whispered the mage, 'this is no ordinary {object1}; it’s {plot_twist}!'"

    print(story)

elif(choice=='3'):
    name = input("Enter a name: ")
    occupation = input("Enter an occupation: ")
    adjective1 = input("Enter an adjective: ")
    superpower = input("Enter a superpower: ")
    place1 = input("Enter a place: ")
    villain = input("Enter a villain: ")
    place2 = input("Enter another place: ")
    adjective2 = input("Enter another adjective: ")
    love_interest = input("Enter a love interest's name: ")
    verb = input("Enter a verb: ")
    exclamation = input("Enter an exclamation: ")  # Added exclamation input
    superhero_name = input("Enter the superhero's name: ")  # Added superhero name input

    # Filling the template with user input in a single string formatting
    story = (
        f"{name} was just a {occupation} until a {adjective1} accident gave them the power of {superpower}. "
        f"By day, they saved {place1} from {villain}, but by night, they couldn’t stop thinking about {name}. "
        f"'{exclamation},' they thought, 'how do I tell them I’m {superhero_name}?' "
        f"A chance encounter at the {place2} revealed their {adjective2} secret. "
        f"'{name},' said {love_interest}, 'I’ve always known, and I still {verb} you.'"
    )

    print(story)

elif(choice=='4'):
    year = input("Enter a year: ")
    adjective = input("Enter an adjective: ")
    name = input("Enter a name: ")
    historical_era = input("Enter a historical era: ")
    famous_figure = input("Enter a famous figure: ")
    future_object = input("Enter a future object: ")
    exclamation = input("Enter an exclamation: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    random_device = input("Enter a random device: ")
    major_event = input("Enter a major historical event: ")

    # Filling the template
    story = f"In {year}, an experiment involving a {adjective} machine sent {name} to {historical_era}. There, they met {famous_figure}, who was astonished by their {future_object}. '{exclamation},' exclaimed the crowd, mistaking them for a {noun}. To get back, {name} had to {verb} using a {random_device}. '{name},' said the historian, 'you’ve just rewritten {major_event}!'"

    print(story)

elif(choice=='5'):
    adjective1 = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    creature = input("Enter a creature: ")
    exclamation1 = input("Enter an exclamation: ")
    name1 = input("Enter a name: ")
    random_object = input("Enter a random object: ")
    adjective2 = input("Enter another adjective: ")
    hobby = input("Enter a hobby: ")
    absurd_solution = input("Enter an absurd solution: ")
    exclamation2 = input("Enter another exclamation: ")
    simple_annoyance = input("Enter a simple annoyance: ")

    # Filling the template
    story = f"""
    The apocalypse started when a {adjective1} {noun} went viral, turning everyone into {creature}.
    '{exclamation1},' screamed {name1}, grabbing their {random_object} to defend themselves.
    In the chaos, {name1} found a {adjective2} group of survivors obsessed with {hobby}.
    '{name1},' said their quirky leader, 'our only hope is {absurd_solution}.'
    '{exclamation2},' groaned {name1}, 'I miss the days of {simple_annoyance}.'
    """

    print(story)

else:
    print("enter valid choice")
