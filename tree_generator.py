#this programme generate a set of decision trees for Hangman according to all the English words
# I have used Python tree class implemented by Joowani https://github.com/joowani/binarytree


from binarytree import tree, bst, convert, Node, pprint

print 'Start reading the dictionary file...'
with open('words.txt') as f:
    allWords = f.read().splitlines()

print 'There are '+str(len(allWords))+' words in the file'

maxlen = 0
for word in allWords:
	if len(word) > maxlen:
		maxlen = len(word)

print 'The longest word has '+str(maxlen)+' letters in it'

# # Generate a random binary tree and return its root
# my_tree = tree(height=5, balanced=False)

# # Generate a random BST and return its root
# my_bst = bst(height=5)


# # Pretty print the trees in stdout
# pprint(my_tree)
# pprint(my_bst)

# my_list = convert(my_bst)
# print my_list

treelist=[];wordlengthlist=[];

for n in xrange(maxlen):						 #Create a list of binary search trees and a list of lists of different length words
	treelist.append(bst(height=10))
	wordlengthlist.append([])

for word in allWords:
	wordlengthlist[len(word)-1].append(word)

print 'There are '+str(len(wordlengthlist[8]))+' Word with 9 letters'

def find_most_frequent_letter(length):
	count=[0]
	for n in xrange(26):
		count.append(0)

	for word in wordlengthlist[length-1]:  #find most frequent letter in 6 length word
		for letter in list(word):
			if letter.isalpha():    #to avoid the char <<'>>
				count[ord(letter) - 97] += 1

	print count, type(count)
	print 'the most frequent letter of length ',length,'is', chr(count.index(max(count))+97)

#list of 31 most common letter for different length
first_guess = ['A','A','A','A','S','E','E','E','E','E','E','E','I','I','I','I','I','I','I','I','I','I','I','I','I','I','I','I','I','I','I']

#Fill the 31 binary trees for different length
for i in xrange(31): 
	treelist[i].value = first_guess[i]
	


