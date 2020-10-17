# -------------------------------------------------------------------------
# Predicts if a song will enter on Spotify's Top 50 based on user inputs
#
# (C) 2020 Carlos Vicente S Araujo, Manaus, Brazil
# Released under GNU Public License (GPL)
# email vicente@icomp.ufam.edu.br
# ------------------------------------------------------------------------

import subprocess
import sys
import random

try:
	import joblib
except ImportError: # Installs joblib if gets an import error
	subprocess.check_call([sys.executable, "-m", "pip", "install", 'joblib'])
finally:
	import joblib 

try:
	import sklearn # SciKit-Learn is not used on this code, but it's used on the saved model, so it's going to be imported anyway when open the model.
		       # I put this import here to avoid an import error when open the model.
except ImportError: # Installs scikit-learn if gets an import error
	subprocess.check_call([sys.executable, "-m", "pip", "install", 'scikit-learn'])
finally:
	import sklearn 

def help():
	
	# This function only prints helpful information for the user

	print("\nCreated by MSc. Carlos Vicente - https://www.linkedin.com/in/carlosvsaraujo/")
	print("An explicit music is one that has curse words or language that is sexual, violent or offensive")
	print("Energetic tracks are the ones that feel fast, loud, and noisy. For example, death metal has high energy, while a Bach prelude has low energy.")
	print("If your song only has vocal sounds like 'Ooh' and 'Aah' also consider it as an instrumental track.")
	print("If your song was recorded live without audience consider it as non-live.\n")

def predict(model):
	"""
	Predicts if a song will become popular based on user inputs

	This function requires some inputs about a song and returns the probability of this song to appears on Spotify's Top 50 Global ranking

	Parameters
	----------
	model : estimator
	A SciKit-Learn estimator trained with the same inputs that are requested as user inputs in this function

	Returns
	-------
	prob : float
	The probability of a song appears on Top 50 based on user inputs 

	"""

	song=[] # An empty array to store data from the song

	song.append(random.randint(1,100)) # As the model requests an ID, I'm creating a random one here. 
				                       # The base model makes a feature selection, so it's unlikely that this feature has an influence on the classification

	print("\nFor the following questions, type 0 when False and 1 when True.\n")

	aux = input("Is your music explicit? ") # This represents the explicit flag of Spotify API. API documentation: https://developer.spotify.com/documentation/
	while aux!= '0' and aux!= '1': # If the user do not put 0 or 1 as input, we keep requesting the info until he put a valid one. This step is make for all inputs
	    print("Please, type 0 when False and 1 when True.")
	    aux=input("Is your music explicit? ")
	song.append(aux)

	aux = input("Is your music dancing? ") # This represents the danceability feature of Spotify API. All the features were binarized during the model train process
	while aux!= '0' and aux!= '1':
	    print("Please, type 0 when False and 1 when True.")
	    aux=input("Is your music dancing? ")
	song.append(aux)

	aux = input("Has your song a high energy? ") # Spotify's API energy feature
	while aux!= '0' and aux!= '1':
	    print("Please, type 0 when False and 1 when True.")
	    aux=input("Has your song a high energy? ")
	song.append(aux)

	aux = input("Is your music a Rap song? ") # Based on Spotify's API speechiness feature
	while aux!= '0' and aux!= '1':
	    print("Please, type 0 when False and 1 when True.")
	    aux=input("Is your music a Rap song? ")
	song.append(aux)

	aux = input("Is your music acoustic? ") # Spotify's API acousticness feature
	while aux!= '0' and aux!= '1':
	    print("Please, type 0 when False and 1 when True.")
	    aux=input("Is your music acoustic? ")
	song.append(aux)

	aux = input("Is your music instrumental? ") # Spotify's API instrumentalness feature
	while aux!= '0' and aux!= '1':
	    print("Please, type 0 when False and 1 when True.")
	    aux=input("Is your music instrumental? ")
	song.append(aux)

	aux = input("Is your music live? ") # Based on Spotify's API liveness feature
	while aux!= '0' and aux!= '1':
	    print("Please, type 0 when False and 1 when True.")
	    aux=input("Is your music live? ")
	song.append(aux)

	aux = input("Is your music happy? ") # Spotify's API valence feature
	while aux!= '0' and aux!= '1':
	    print("Please, type 0 when False and 1 when True.")
	    aux=input("Is your music happy? ")
	song.append(aux)

	prob=model.predict_proba([song]) # Makes the prediction process
	prob=prob[0][1] # Just keeps the probability of appears on Top 50

	return prob

model = joblib.load(open('model.sav', 'rb')) # Opens an estimator saved on a file
mode = input("Type 'help' for help, 'predict' for prediction or 'exit' to exit\n") 
while mode!= 'exit': # Keeps the program running until exit is typed
	if mode=='help':
	    help()
	if mode=='predict':
	    prob=predict(model)
	    print("\nThe probability of your song to appear in Spotify's Top 50 Global is", "{0:.2%}".format(prob),"\n") # Prints the probability of appears in Top 50 in percentage format
	mode = input("Type 'help' for help, 'predict' for prediction or 'exit' to exit\n")
