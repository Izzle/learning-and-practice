# NOTICE: This code is intended for broadening my personal understanding of topics in information security;
#  this code is for EDUCATIONAL purposes only (and may be incorrect at that). I am simply trying to
#  teach myself computer security principals so I can one day get a career in the IT security field
#  and to increase my understanding of computer science in general.

# A "rainbow table" is dictionary full of known hashes for commonly used passwords.
# For example: the md5 hash for "password" is 5f4dcc3b5aa765d61d8327deb882cf99
# The password would be the key and the hash would be the value.

# pseudocode because I haven't figured out why I can't store a hash value in a dictionary (I know that would be a hash of a hash)
# Im very novice at python and this is meant to be more of an outline

allPasswordz from wordlist.txt # Need to store a word list into a variable
passwordz in allPasswordz      # Need to slice up each password individually
    rainbow{passwordz} = hash(passwordz) # Iterate each password into a dictionary and generate its hash as the value

