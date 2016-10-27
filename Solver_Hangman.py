#Hangman Solver

#Username: siyaofeng
#Password: daa9d0effc7021d4c9636094f211c748

import httplib
import json
from binarytree import tree, convert, heap, pprint
import pickle

#----------------------------------------------------------------------------------------------------------
# Build connection with server
conn = httplib.HTTPSConnection("hangman.leanapp.cn")

payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"username\"\r\n\r\nsiyaofeng\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"password\"\r\n\r\ndaa9d0effc7021d4c9636094f211c748\r\n-----011000010111000001101001--"

headers1 = {
    'content-type': "multipart/form-data; boundary=---011000010111000001101001",
    'authorization': "Basic c2l5YW9mZW5nOmRhYTlkMGVmZmM3MDIxZDRjOTYzNjA5NGYyMTFjNzQ4",
    'cache-control': "no-cache",
    'postman-token': "8acf63b3-68df-ff4a-3088-6c39a23c440a"
    }

conn.request("POST", "/login", payload, headers1)

res = conn.getresponse()
data = res.read()

r1 = json.loads(data)
myToken = r1["token"]
print 'This is my token', myToken

headers2 = {
    'content-type': "multipart/form-data; boundary=---011000010111000001101001",
    'authorization': "Basic c2l5YW9mZW5nOmRhYTlkMGVmZmM3MDIxZDRjOTYzNjA5NGYyMTFjNzQ4",
    'cache-control': "no-cache",
    'postman-token': "8acf63b3-68df-ff4a-3088-6c39a23c440a",
    'X-Token': myToken
    }

conn.request("GET", "/me", payload, headers2)

r2 = json.loads(conn.getresponse().read())
# print r2

#----------------------------------------------------------------------------------------------------------
#import the trees built from file
print "Loading the tree, this may take a few time"
resultfile = open('result.txt', 'r')
thelist = pickle.load(resultfile)
treelist = []

for i in thelist:
	treelist.append(convert(i))
#----------------------------------------------------------------------------------------------------------
# functions for playing

def guess_letter_ingame(gameid, roundid, guess):
	guessurl = "/game/"+str(gameid)+"/round/"+str(roundid)+"?guess="+guess
	conn.request("POST", guessurl, payload, headers2)

	return json.loads(conn.getresponse().read())



#----------------------------------------------------------------------------------------------------------
# start playing

#start a new game
conn.request("POST", "/game", payload, headers2)
res0 = json.loads(conn.getresponse().read())

# "get game info"
conn.request("GET", "/game", payload, headers2)
res1 = json.loads(conn.getresponse().read())
gameid = res1['games'][0]['id']  #gameid
print "Game ID is ",gameid



print "Guess start!"
for i in xrange(20):
	# "start a new round in gameid"
	conn.request("POST", "/game/"+str(gameid), payload, headers2)
	res2 = json.loads(conn.getresponse().read())
	roundid = res2["current_round_number"]
	print "Current round ID is ",roundid


	# "get the round info in gameid"
	conn.request("GET", "/game/"+str(gameid)+"/round/"+str(roundid), payload, headers2)
	res3 = json.loads(conn.getresponse().read())



	word_length = len(res3['word'])
	previous_count = word_length

	node_tree = treelist[word_length-1]
	while res3["status"] == "in progress":
		count = 0
		letter_guess = node_tree.value

		res3 = guess_letter_ingame(gameid,roundid,letter_guess)
		res3 = res3["round"]
		print res3["word"]

		for i in res3["word"]:  #count the _ in the word to determine right or wrong guess
			if i == '_':
				count += 1

		if node_tree.left == None: #in case the tree reach max height
			print "Unfortunatly, max height reached"
			for i in range(res3['life']): #guess all a to pass this round
				temp = guess_letter_ingame(gameid,roundid,'a')

		if count == previous_count:  	#wrong guess
			node_tree = node_tree.left
		else:							#right guess
			node_tree = node_tree.right

		previous_count = count
	

# Show the final score
conn.request("GET", "/game/"+str(gameid), payload, headers2)
res4 = json.loads(conn.getresponse().read())
print "Guess finished, your final score is ", res4["score"]










