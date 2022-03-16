import random
import getpass

# sentence that will later have to guess, when running through terminal you cannot see the input.
sen = getpass.getpass(prompt="choose a sentence:  ")

# line 11 makes a sentence to compare later with answer given by user.
# line 12 splits the sentence for making words disappear later.
# line 13 splits the sentence again for later use because the first sentence split is altered, thus we don't have the
# original array anymore.
sen_for_later = sen
sen_split = sen.split()
sen_split_for_later = sen_split

# line 16 is a variable that says how many words are in the given sentence.
sen_split_amn = len(sen_split)

# line 20 asks user how many words he wants to take out (these are chosen randomly).
# line 21 turns that amount into an int.
amn_take_out = input("choose amount of words you want to take out: ")
amn_take_out_int = int(amn_take_out)

where_arr = []

# this is a loop that determines randomly what word will be removed,
# and how many times according to the previous user input.
for f in range(0, amn_take_out_int):
    # line 25 chooses the word that will be erased randomly,
    what_wrd_replace = random.randint(0, sen_split_amn)

    # lines 33-38 determines how long the word that will be erased is, makes a loop that is the length of the word,
    # and inside the loop we add "_ " to show the amount of characters in the word.
    len_word = len(sen_split[what_wrd_replace])
    len_word_int = int(len_word)
    len_word_in_str = ""

    for g in range(0, len_word_int):
        len_word_in_str += "_ "

    # lines 41 & 42 replace the word with the previously created string of underscores.
    sen_split[what_wrd_replace] = len_word_in_str
    where_arr.append(what_wrd_replace)

print(sen_split)

guess = input("write the full sentence: ")

# lines 49-54 check to see if the user's guess was correct or not, and giving an output of if it was correct or not.
if guess == sen_for_later:
    print("congrats, guess is correct")
    print(sen)
else:
    print("guess incorrect")
    print(sen)
