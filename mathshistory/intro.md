# Produce biographical information from a corpus of biographical notes

The aim of this project is to extract biographical information from the biographical notes published on the [MacTutor website](https://mathshistory.st-andrews.ac.uk/Biographies/chronological) experimenting with different NLP approaches.

These texts are published under Creative Commons License 4.0 BY SA (cf. [Copyright Information on the original website](https://mathshistory.st-andrews.ac.uk/Miscellaneous/copyright/)) and can thus be used for the present project.

The aim is to first identify named entities and link them to LOD resources like DBPaedia and Wikidata.

Then to retrieve temporal relationships and biographical information expressend in the texts in form of relations among entities, and store it in form of Linked Open Data using the [SDHSS ontology ecosystem](https://sdhss.org).


## Data acquisition and transformation

### explore.ipynb

Explore the chronological list of mathematicians and prepare data import

### import.ipynb

Import the texts into a PostgreSQL database 

Then produce valid XML in order to be able to operate on the different parts and tags.

### explore_db_texts.ipynb 

( !!! reprendre)

Explore the imported textual data: lenght, distribution, etc.


### get_persons_uris_dbpedia.ipynb

Linke the existing persons to DBpedia getting their URIs




## Spacy and the Universe Plugins

Explore the functionality of the main library and its many extensions

### spacy_explore.ipynb

NLP treatement with Spacy and result stored in dedicated tables of the database (to be improved, adding vectors)


### coreference_resolver_neuralcoref.ipynb

Tested and not adopted

### coreference_resolver_spacy.ipynb

Spacy coref resolver, I wasn't able to make it work, Python dependencies issue.


### coreference_resolver_coreferee_crossLingual.ipynb







## Proof of Concept

### spacy_postgres_produce.ipynb

Create a data model using Spacy and store the result in a PostgreSQL database


### cooccurrences_analysis.ipynb

First exploration of terms cooccurrences (to improve)

### produce_summaries.ipynb

Extract summaries in view of experimenting topic modeling and clustering

### get_uris.ipynb

Link main persons to DBPaedia URIs