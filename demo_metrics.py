from cmtt.metrics import *

sent = "RAHUL jab dieting par hota hai toh green tea peeta hai."
metrics = Metrics(language="hineng")

# Total Available metrics
print("Total available metrics")
print(metrics.AvailableMetrics())

# Code-Mixing Index 
print("CMI: ",metrics.metrics(name="cmi", sentence=sent))
print()

# M-Index 
print("M-Index: ",metrics.metrics(name="M-Index", sentence=sent)) #name 
print()

#I-Index
print("I-Index: ",metrics.metrics(name="I-Index", sentence=sent))
print()

# Burstiness
print("burstiness: ",metrics.metrics(name="burstiness", sentence=sent))
print()

