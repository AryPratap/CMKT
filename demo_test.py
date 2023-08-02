from cmkt.tasks import *
from cmkt.preprocessing import *
from cmkt.metrics import *
from cmkt.data import *



#sentence = "Deepak ji, channel ko kitna fund diya hai congress ne? 2006 me ameithi rape case kyu nahi discuss kiya kabhi?"
sentence = "RAHUL jab dieting par hota hai toh green tea peeta hai."
#sentence = "Deepak ji, channel ko kitna fund diya hai congress ne? 2006 me ameithi rape case kyu nahi discuss kiya kabhi?"
#sentence = "4 din me 2 accidents, kuch to jhol hai, shayad politics ho rahi hai.."
sentence = "The ultimate twist Dulhan dandanate huye brings Baraat .... Dulha"
sentence = "laufed ... first u hav to correct ur english baad me sochna use !!!"
sentence = "@Mariam_Jamali Nice one but logo filhal KK ki jaga Pakistan ka lagwa do. Pic is good"


#Download cmtt datasets
print("Download cmtt datasets function")
lst = download_cmkt_datasets(["mt_hineng_Dhar_LR4NLP2018",
                              "lid_hineng_Mave_ACL2018",
                              "ner_hineng_Singh_ACL2018",
                              "ner_hineng_Singh_NEWS2018",
                              "pos_hineng_Singh_SocialNLP2018",
                              "mt_hineng_Srivastava_2021hinge",
                              "mt_hineng_lince",
                              "mt_hineng_Srivastava_WNUT2020",
                              "sarcasm_hineng_Swami_2018corpus",
                              "sentiment_hineng_Joshi_COLING2016",
                              "sentiment_hineng_Shete_2016",
                              "humor_hineng_Ankush_2018",
                              "sentiment_hineng_Patwa_SemEval2020",
                              "irony_hineng_Vijay_EMSASW2018",
                              "hatespeech_hineng_Bohra_PEOPLES2018"])
print(lst)


# mytoolkit = TaskToolKit('hineng')
# lid = mytoolkit.lid(model_name="XLM Roberta base")

# langTags = lid.getlangIds(sentence)
# ner = mytoolkit.ner(model_name="XLM Roberta base")
# nertags = ner.getNERTags(sentence)	
# for i in range(len(langTags)):
# 		if nertags[i][1] != 'O':
# 			langTags[i] = '8'
			
# print("Predicted langTags")
# print(lid.getLangTags(sentence))
# print()

# print("After formating")
# print(langTags)
# langTags = ['3','3','0','0','0','0','1','3','1','1','3','1','1','1','3','0','0','0']
#langTags = ['0', '3', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '3']
#langTags = ['0', '0', '0', '1', '1', '1', '0', '1', '3', '1']
#langTags = ['8', '1', '3', '0', '1', '1', '0', '1', '1', '8', '1', '3', '3', '1', '8', '0', '0', '1', '1', '0', '1', '1', '3']
# print("Total Tokens: ", len(langTags))
# print()
# lang1_words = 0
# for i in langTags:
# 	if i == '0':
# 		lang1_words = lang1_words + 1
# print("EN tokens: ", lang1_words)
# print()
# lang2_words = 0
# for i in langTags:
# 	if i == '1':
# 		lang2_words = lang2_words + 1
# print("HI tokens: ", lang2_words)
# print()	
# max_count = max(lang1_words,lang2_words)

# # total tokens 
# n = len(langTags)
# # language independent tokens
# u = len(langTags) - lang1_words - lang2_words

# if n>u:
# 	print("CMI: ", 100*(1 - (max_count/(n-u))))
# else:
# 	print("CMI: ", 0)
       
# lang1_words = 0
# for i in langTags:
# 	if i == '0':
# 		lang1_words = lang1_words + 1
				
# lang2_words = 0
# for i in langTags:
# 	if i == '1':
# 		lang2_words = lang2_words + 1
		
# # total number of words 
# n = len(langTags)
# # total languages 
# k = 3

# 			# language independent words
# lang3_words = n - lang1_words - lang2_words
# if lang3_words == 0:
# 	k = 2
		
# sigma_pj = (lang1_words/n)**2 + (lang2_words/n)**2 + (lang3_words/n)**2 

# print("M-INDEX: ", (1- sigma_pj)/((k-1)*sigma_pj)) 

# S = 0

# for i in range(len(langTags)-1):
# 	if langTags[i]!=langTags[i+1]:
# 		S = S+1
# print("I-Index:",S/(len(langTags)-1)) 
