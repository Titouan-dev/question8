from pprint import pprint
import nltk
import deepl
import tika
nltk.download('stopwords')
from Questgen import main
qg = main.QGen
payload = {
            "input_text": "RNA can be extracted, but this is more complicated because it is a fragile molecule. It is degraded by the ubiquitous RNAs. They are activated by the lysis of cells and potentially the degradation of RNA. In the lysis buffer we use guanidine isothiocyanate which blocks RNAses. We also use protein denaturing agents such as DTT or beta mercaptoethanol."
        }
output = qg.predict_mcq(payload)
pprint(output)