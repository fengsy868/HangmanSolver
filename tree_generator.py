#this programme generate a set of decision trees for Hangman according to all the English words
# I have used Python tree class implemented by Joowani https://github.com/joowani/binarytree

import pickle
from binarytree import tree, bst, convert, heap, Node, pprint

print 'Start reading the dictionary file...'
with open('words.txt') as f:
    allWords = f.read().splitlines()

print 'There are '+str(len(allWords))+' words in the file'

maxlen = 0
for word in allWords:
	if len(word) > maxlen:
		maxlen = len(word)

print 'The longest word has '+str(maxlen)+' letters'

treelist=[];wordlengthlist=[];
height_tree = 18
for n in xrange(maxlen):						 #Create a list of binary search trees and a list of lists of different length words
	treelist.append(heap(height=height_tree, max=True))
	wordlengthlist.append([])

for word in allWords:
	wordlengthlist[len(word)-1].append(word)

print 'There are '+str(len(wordlengthlist[8]))+' Word with 9 letters'

#This function aims at find the (rank)th frequent letter in a word's list
def find_most_frequent_letter(wordlist,rank):
	count=[0]
	for n in xrange(26):
		count.append(0)

	for word in wordlist:  #find most frequent letter in 6 length word
		for letter in list(word):
			if letter.isalpha():    #to avoid the char <<'>>
				count[ord(letter) - 97] += 1

	new = count[:]	#copy the rank list 
	for i in xrange(rank-1):
		new.remove(max(new))	#delete the most biggest number in new list

	return chr(count.index(max(new))+97) #return the (rank)th frequent letter in wordlist


# These twofunction used to delete word do/dont contains certain letter from the wordlist
def generate_new_list_with_letter_correct(letter, wordlist):
	temp_list= []
	for word in wordlist:
		if letter in word:
			temp_list.append(word.replace(letter,''))
	wordlist[:] = []

	for word in temp_list:
		wordlist.append(word)




def generate_new_list_with_letter_wrong(letter, wordlist):
	temp_list = []
	for word in wordlist:
		if letter in word:
			temp_list.append(word)

	for word in temp_list:
		wordlist.remove(word)
	
# main iteration function to fill the tree
def fill_the_tree(node,wordlist,deepth,height):
	
	if deepth == height+1:
		return deepth-1
	
	local_wordlist1 = wordlist[:] #this for wrong guess
	local_wordlist2 = wordlist[:] #this for correct guess





	#get the value for left node, wrong guess
	generate_new_list_with_letter_wrong(node.value, local_wordlist1)

	node.left.value = find_most_frequent_letter(local_wordlist1, 1)   #left node contains the next most frequent letter if guess is wrong
	deepth = fill_the_tree(node.left, local_wordlist1, deepth+1, height)
	

	#get the value for right node, correct guess
	generate_new_list_with_letter_correct(node.value, local_wordlist2)
	node.right.value = find_most_frequent_letter(local_wordlist2, 1)
	deepth = fill_the_tree(node.right, local_wordlist2, deepth+1, height)
	
	return deepth-1

#list of 31 most common letter for different length
first_guess = ['a','a','a','a','s','e','e','e','e','e','e','e','i','i','i','i','i','i','i','i','i','i','i','i','i','i','i','i','i','i','i']

find_most_frequent_letter(wordlengthlist[12],1)

# Fill the 31 binary trees for different length
for i in xrange(31): 
	print 'Building the tree for word length ',i
	treelist[i].value = first_guess[i]
	wordlist = wordlengthlist[i]
	fill_the_tree(treelist[i], wordlist, 1, height_tree)


final_list = []
for tree in treelist:
	final_list.append(convert(tree))

resultfile = open('result.txt', 'w')
pickle.dump(final_list, resultfile)







