from cmtt.metrics import *

sentence = "RAHUL jab dieting par hota hai toh green tea peeta hai."

# Code-Mixing Index 
print("CMI: ",cmi(sentence))
print()

# M-Index 
print("M-Index: ",M_Index(sentence))
print()

#I-Index
print("I-Index: ",I_index(sentence))
print()

# Burstiness
print("Burstiness: ", burstiness(sentence))
