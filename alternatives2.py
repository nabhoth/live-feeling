import pandas as pd
import numpy as np
import sys
import csv
from numpy import genfromtxt
import operator
import heapq

#d_cornerk	d_save	d_freek	d_goal	d_assist	d_foul	d_penalty	d_offside	
#   35        36	   37	   38	  39	      40	   41	       42	      
#d_steal	d_fight	a_offside	a_penalty	a_cornerk	a_oppscore	a_wescore
#  43	      44	   45	      46	        47	       48	        49
#param = 35
for param in range(35,50):
	print(param)
	similarity_score = []
	#user = np.delete(user, 0)
	#print(user)
	mydata = genfromtxt('alternatives.csv', delimiter=',', dtype = str, skip_header = 1)
	#print (mydata)

	#Find most similar user in terms of all parameters
	#print (type(mydata))
	for x in range(0, 57):
		data = genfromtxt('alternatives.csv', delimiter=',', dtype = str, skip_header = 1)
		user = data[x]
		data = np.delete(data, x, axis=0)
		#print ("Most similar users across all features")
		for row in data:
			count = 0
			matches = 0
			for item in row:
				if item == user[count]:
					#print (item, user[count])
					matches = matches + 1
				count = count + 1
			similarity_score.append(matches)

		#print (similarity_score)
		topthree = heapq.nlargest(3, range(len(similarity_score)), similarity_score.__getitem__)
		#print (topthree)

		#for y in topthree:
		#	print (similarity_score[y], user[param], data[y,param])
		'''
		if data[topthree[0],param] != "":
			print(data[topthree[0],param])
		elif data[topthree[1],param] != "":
			print(data[topthree[1],param])
		else:
			print (data[topthree[2],param])
		'''
		#Find most similar user in terms of not game situation related parameters
		#print ("Most similar users across non-game situation related features")
		similarity_score_ns = []
		user_ns = user[0:35]
		#print (user_ns)
		data_ns = data[:,0:35]
		for row in data_ns:
			count = 0
			matches = 0
			for item in row:
				if item == user_ns[count]:
					#print (item, user[count])
					matches = matches + 1
				count = count + 1
			similarity_score_ns.append(matches)

		#print (similarity_score)
		topthree_ns = heapq.nlargest(3, range(len(similarity_score_ns)), similarity_score_ns.__getitem__)
		#print (topthree_ns)
		#for y in topthree_ns:
		#	print (similarity_score_ns[y], user[param], data[y,param])
		#print(data[topthree_ns[0],param])
		'''
		if data[topthree_ns[0],param] != "":
			print(data[topthree_ns[0],param])
		elif data[topthree_ns[1],param] != "":
			print(data[topthree_ns[1],param])
		else:
			print (data[topthree_ns[2],param])
		'''
		#Find most similar user in terms of situation related parameters
		#print ("Most similar users across game situation related features")
		similarity_score_s = []
		user_s = user[35:]
		#print (user_s)
		data_s = data[:,35:]
		for row in data_s:
			count = 0
			matches = 0
			for item in row:
				if item == user_s[count]:
					#print (item, user[count])
					matches = matches + 1
				count = count + 1
			similarity_score_s.append(matches)

		#print (similarity_score)
		topthree_s = heapq.nlargest(3, range(len(similarity_score_s)), similarity_score_s.__getitem__)
		#print (topthree_s)
		#for y in topthree_s:
		#	print (similarity_score_s[y], user[param], data[y,param])
		#print(data[topthree_s[0],param])
		
		if data[topthree_s[0],param] != "":
			print(data[topthree_s[0],param])
		elif data[topthree_s[1],param] != "":
			print(data[topthree_s[1],param])
		else:
			print (data[topthree_s[2],param])
		
		#Find most similar user in terms of situation related parameters
		#print ("Most similar users across game situation related features")
		similarity_score = []
		similarity_score_ns = []
		similarity_score_s = []
