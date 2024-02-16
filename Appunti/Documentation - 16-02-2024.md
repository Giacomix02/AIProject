# 1. Classificazione di Topics in base ad una domanda: trained on Yahoo Answers
## 2. Astratto
Il progetto presentato ha come obiettivo la presentazione di una dimostrazione del modello di Machine Learning *classification*. 
Tale presentazione vede l'assegnazione di topics di Yahoo Answers all'input proposto all'AI. 
Infine un CSP problem sarà usato per eventualmente filtrare le assegnazioni effettuate.

## 3. Introduzione
Dopo aver valutato le opzioni proposte per la realizzazione del progetto per l'esame, abbiamo scelto di creare un semplice classificatore di topics basato sulle domande e risposte di Yahoo! Answers, ricadendo quindi nel domain di *Recommender Systems or Personal Assistant Agents*.
il codice usato per l'allenamento, ottimizzazione, testing del modello, e la generazione dei grafici interessati è nel file TopicsClassification.ipynb 
il codice usato per la modifica del dataset si trova []

## 4. Materiali e metodi
- come materiale usato per allenare il modello Machine Learning è stato usato e modificato un dataset che raggruppa 1.4M domande e risposte di Yahoo! Answers, si trova al seguente link: https://huggingface.co/datasets/yahoo_answers_topics/viewer/yahoo_answers_topics/train?p=1
- Per lo sviluppo e allenamento del modello Machine Learning sono stati usati gli strumenti della libreria python *sklearn* per l'allenamento e il file *NLTKVectorizer.py* per vettorializzare il contenuto del dataset e l'input per la predizione, tale file è fornito dal tutorial al link: https://reslan-tinawi.github.io/2020/05/26/text-classification-using-sklearn-and-nltk.html ed è stato trattato come materiale di riferimento per e durante lo svolgimento del progetto.
- Per l'interfaccia grafica è stato usato typescript affiancato dal framework *Tauri*.
- Per connettere interfaccia grafica con il modello ML è stato usato il web framework in python *Bottle*, il quale crea un server locale in cui far eseguire le predizioni del modello.
## 5. Esperimenti e risultati
Prima dell'allenamento del modello abbiamo ritenuto opportuno modificare il dataset in modo da unire il campo question_title con il campo question_content così da uniformare il materiale per l'allenamento. 
In quanto a bilanciamento del dataset, abbiamo trovato una maggior quantità di parole nel topic [] 
in quanto a splitting del dataset, esso è stato già reso disponibile all'origine diviso in un dataset di testing, e di training.

per l'allenamento e predizione abbiamo creato una pipeline la quale effettuerà 2 operazioni:
1. vettorializzazione dei dati, trasformando parole in de facto vettori numerici, in modo da essere commestibili per il modello
2. allenamento: abbiamo ritenuto l'algoritmo logistic regression(1) come ottimale per il training del modello.
(parlare del tuning, magari lo faremo con parametri ristretti invece di non farlo)
(parlare dei risultati ottenuti con dataset non modificato e modificato, magari mostrando i grafici delle error matrix e confusion matrix)


(1) controllare se  logistic regression è effettivamente ottimale

## 6. Conclusione




[] = informazione mancante