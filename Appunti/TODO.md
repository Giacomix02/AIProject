**GRAFICI E CONTROLLI DA FARE SUL DATASET PRIMA DEL TRAINING**

- **Imputations**       ==> non servono imputations, le missing values della colonna question_content verranno gestire come se il testo è uguale alla domanda posta
- **Data correlation**  ==> si potrebbe fare una correlazione tra lunghezza tra domanda e risposta per ogni topic (?)
- **Data distribution** ==> FATTO! per il dati del training set
- **Outliers**          ==> non servono , non ci sono outliers
- **Data balancing**    ==> non serve i dati sono bilanciati: le domande per numero di topic sono bilanciati
- **Descriptive statistics** ==> da fare

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


Project output: 
- progetto
- feature matrix del testo vettorializzato
- word clouds delle parole

Dataset versions:
- 1: base
- 2: topics convertiti da numero a stringa, e join tra colonne question_title e question_content
- 3: rimozione di stop-words