# encoding=utf-8

import ahocorasick

def build_actree(wordlist):
	'''
		Aho-Corasick automaton for keyword matching
		build AC trie
	'''
	actree = ahocorasick.Automaton()
	for index, word in enumerate(wordlist):
		actree.add_word(word, (index, word))     #
	actree.make_automaton()
	return actree


def ac_detect(actree,text):
	
	region_wds = []
	for w1 in actree.iter(text):
		if len(w1) > 0:
			region_wds.append(w1[1][1])
	return region_wds