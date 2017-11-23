# Exercise 59: Pickle
# Serializing and Deserializing a byte stream
#
# Useful for anything that requires a lot of processing and
# ends in an object that you will use again. We save the
# byte stream to a file and can access it again when needed.

import pickle


def pickling_out():
    example_dict = {1: "6", 2: "8", 3: "r", 4: "lala"}

    pickle_out = open("dict.pickle", "wb")  # wb = writing bytes
    pickle.dump(example_dict, pickle_out)
    pickle_out.close()


def pickling_in():
    pickle_in = open("dict.pickle", "rb")  # rb = read bytes
    example_dict = pickle.load(pickle_in)

    # Proof that it works and prints usable data
    print("Proof it works:", example_dict)
    print(example_dict[3])


pickling_out()
pickling_in()
