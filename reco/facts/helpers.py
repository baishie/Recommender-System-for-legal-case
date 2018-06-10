from smart_open import smart_open
import gensim
import nltk
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
from gensim.models import KeyedVectors
import os
import numpy as np

directory = r'C:\Users\Danilo Marinduque\Desktop\THESIS\RECO SYSTEM\reco'
# googleEmb = os.path.join(directory, 'GoogleNews-vectors-negative300.bin')
trainedEmb = os.path.join(directory, 'model_trained.bin')
class SendHelp():

	def toString(self, arr):
		ts = np.array_str(arr)
		return ts

	def loadGoogleEmb(self):
		wv = KeyedVectors.load_word2vec_format(googleEmb, binary=True, limit=1200000)
		wv.init_sims(replace=True)
		return wv

	def loadTrained(self):
		mod = KeyedVectors.load_word2vec_format(trainedEmb, binary=True)
		return mod

	def wordAve(self, wv, words):
		all_words, mean = set(), []
		for word in words:
			if isinstance(word, np.ndarray):
				mean.append(word)
			elif word in wv.vocab:
				mean.append(wv.vectors_norm[wv.vocab[word].index])
				all_words.add(wv.vocab[word].index)
		if not mean:
			logging.warning("cannot compute similarity with no input %s", words)
			return np.zeros(wv.layer1_size,)

		mean = gensim.matutils.unitvec(np.array(mean).mean(axis=0)).astype(np.float32)
		return mean

	def word_averaging(self, model, words):
	    all_words, mean = set(), []
	    
	    for word in words:
	        if isinstance(word, np.ndarray):
	            mean.append(word)
	        elif word in model.wv.vocab:
	            mean.append(model.wv.vectors[model.wv.vocab[word].index])
	            all_words.add(model.wv.vocab[word].index)

	    if not mean:
	        logging.warning("cannot compute similarity with no input %s", words)
	        return np.zeros(wv.trainables.layer1_size,)

	    mean = gensim.matutils.unitvec(np.array(mean).mean(axis=0)).astype(np.float32)
	    return mean

	def tokenizeCase(self, text):
	    tokens = []
	    for sent in nltk.sent_tokenize(text, language='english'):
	        for word in nltk.word_tokenize(sent, language='english'):
	            if len(word) < 2:
	                continue
	            tokens.append(word)
	    return tokens





