from django.shortcuts import render
from django.http import HttpResponse
from . models import Case
from django.views.generic import View
from facts.forms import SubmitForm
import pickle
from . import helpers
import numpy as np

class IndexView(View):
	tempName = 'facts/index.html' 
	clf_orig = pickle.load( open( "categorizer_orig.pkl", "rb" ) )
	clf_google =  pickle.load( open( "categorizer_google.pkl", "rb" ) )
	newHelp = helpers.SendHelp()
	# googleMod = newHelp.loadGoogleEmb()
	loadTrained = newHelp.loadTrained()

	def get(self, request):
		form = SubmitForm()
		return render(request, self.tempName, {'form':form})

	def post(self, request):
		form = SubmitForm(request.POST)
		if form.is_valid():
			text = form.cleaned_data['facts']
			toks = self.newHelp.tokenizeCase(text)
			##googlemod
			# word_ave = self.newHelp.wordAve(self.googleMod,toks)
			# prediction = self.clf_google.predict([word_ave])
			# query = np.array_str(prediction).strip("[]''")

			# print((query))

			##modtrained
			word_ave = self.newHelp.word_averaging(self.loadTrained,toks)
			prediction = self.clf_orig.predict([word_ave])
			query = np.array_str(prediction).strip("[]''")
			print((query))
			# query = "parricide"
			# my_filter = {u'tag': [query]}
			name = "CASE NAME"
			numb = "CASE DOCKET"
			link = "SOURCE"
			my_object = Case.objects.filter(tag=query)
			article = "Classification: "+query
			cont = {
				'article' : article,
				'name' : name,
				'numb' : numb,
				'link' : link,
				'my_object' : my_object,
				'form' : form,
			}


			return render(request, self.tempName, cont)

