from cmtt.metrics import *

sent = "RAHUL jab dieting par hota hai toh green tea peeta hai."
metrics = Metrics(language="hineng")

# Total Available metrics
print("Total available metrics")
print(metrics.AvailableMetrics())

# Code-Mixing Index 
print("CMI: ",metrics.metrics(metrics="cmi", sentence=sent))
print()

# M-Index 
print("M-Index: ",metrics.metrics(metrics="M-Index", sentence=sent))
print()

#I-Index
print("I-Index: ",metrics.metrics(metrics="I-Index", sentence=sent))
print()

# Burstiness
print("burstiness: ",metrics.metrics(metrics="burstiness", sentence=sent))
print()

