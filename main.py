import random
from random import randint

# db = {"апельсин": "orange", "яблоко": "apple", "картофель": "potato", "сок": "juice", "пингвин": "penguin",
#       "черепаха": "turtle", "молоко": "milk", "коробка": "box", "дверь": "door", "окно": "window",
#       "ручка": "pen", "небо": "sky", "банан": "banana", "дерево": "tree", "мяч": "ball",
#       "книга": "book", "бумага": "paper", "тростник": "cane", "корабль": "ship", "стакан": "glass"}


# db
# file of scores def write_score
# with open("file_of_scores.txt", "w") as f:
#     f.write('')
db_sentence = {"right": "You guessed ____, you spent 6 tries",
               "choose": "____ variance follow",
               "name": "my ____ is Max",
               "eated": "I ____ apple",
               "buys": "My friend ____ a black phone"}

def load_db():
    """load database from txt file
    path_db - path to txt file"""
    path_db = "db_ru_en.txt" # for Andy and Andemir
    db = {}
    with open(path_db, "r") as f:
        k = f.read()
    c = k.split('\n')
    for i in c:
        kluch = i.split('-')[0]
        znach = i.split('-')[1]
        db[kluch] = znach
    return db

def write_score(name, point):
    """
    :param name: name player
    :param point: score
    :return: None
    """
    path = "file_of_scores.txt"
    with open(path, "r") as f:
        d = f.readlines()
    is_add = False
    for i in range(len(d)):
        if name in d[i]:
            new_point = int(d[i].split("-")[1]) + point
            d[i] = name + " - " + str(new_point) + "\n"
            is_add = True
            break

    if not is_add:
        text = name + " - " + str(point) + "\n"
        d.append(text)

    text = ""
    for line in d:
        text += line

    with open(path, "w") as f:
        f.write(text)

def show_helps(letters, word):
    show = []
    for i in range(len(db[word])):
        show.append('_ ')
    for x in letters:
        show[x] = db[word][x]
    show_letters = ""
    for i in show:
        show_letters += i
    return show_letters

def guess_word(word):
    """guess correct answer by word
    mode 2"""
    max_XP = 10
    help_letters = []
    while True:
        print(word, "in english")
        answer = input("")
        if answer == db[word]:
            print("Excellent! You guessed right, you spent", str(10 - max_XP + 1), "tries")
            return max_XP
        else:
            ran = randint(0, len(db[word])-1)
            if ran in help_letters:
                ran = randint(0, len(db[word])-1)
            help_letters.append(ran)
            print("Sorry, but you didn't guess right:( Try again")
            print(show_helps(help_letters, word))
            if max_XP > 0:
                max_XP -= 1

def guess_word_by_variance(word):
    """mode 1"""
    max_XP = 5
    print(word, "in english, choose variance follow")
    some_words = random.sample(list(db.values()), 4)
    some_words[randint(0, 3)] = db[word]
    print(some_words)
    while True:
        answer = input()
        if answer == db[word] or answer == str(some_words.index(db[word]) + 1):
            print("Excellent! You guessed right, you spent", str(5 - max_XP + 1), "tries")
            return max_XP
        else:
            print("Sorry, but you didn't guess right:( Try again")
            max_XP -= 1

def guess_word_by_sentence(word):
  XP = 0
  print("choose the correct option for this sentence: ", db_sentence[word])
  some_words = random.sample(list(db_sentence.keys()), 4)
  if word in some_words:
    print(some_words)
  else:
    some_words[randint(0, 3)] = word
    print(some_words)
  while True:
    answer = input(': ')
    if answer == word or answer == str(some_words.index(word) + 1):
      XP += 5
      print("Congratulation! You guessed right, you spent", str(XP), "tries")
      break
    else:
      print("Sorry, but you didn't guess right:( Try again")
  return XP

if __name__ == "__main__":
    print("Hello! what's your name?")
    name = input(" ")
    XP = 0
    db = load_db()
    while True:
        print("""what mode do you prefer?
        write 1 if guess word by variance, write 2 if guess word by letters, write 3 if guess word by sentence
         write exit to close program
        """)
        mode = input()
        if mode == '1':
            tasks = random.sample(db.keys(), 5)
            for word in tasks:
                XP += guess_word_by_variance(word)
        elif mode == '2':
            tasks = random.sample(db.keys(), 5)
            for word in tasks:
                XP += guess_word(word)
        elif mode == '3':
            tasks = random.sample(db_sentence.keys(), 5)
            for word in tasks:
                XP += guess_word_by_sentence(word)
        elif mode == "exit":
            break
        print("Congratulations! You scored {} XP".format(XP))

    write_score(name, XP)
