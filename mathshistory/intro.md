# Produce biographical information from a corpus of biographical notes

The aim of this project is to extract biographical information from the biographical notes published on the [MacTutor website](https://mathshistory.st-andrews.ac.uk/Biographies/chronological) and, at the same time, experimenting with different NLP approaches to achieve this goal.

These texts are published under Creative Commons License 4.0 BY SA (cf. [Copyright Information on the original website](https://mathshistory.st-andrews.ac.uk/Miscellaneous/copyright/)) and can thus be used for the present project.

The aim is to first identify named entities and link them to LOD resources like DBPaedia and Wikidata.

Then to retrieve temporal relationships and biographical information expressend in the texts in form of relations among entities, and store it in form of Linked Open Data using the [SDHSS ontology ecosystem](https://sdhss.org).


## Data acquisition, transformation, exploration

### maths_explore.ipynb

Explore the chronological list of mathematicians and prepare data acquisition

### maths_import.ipynb

Import the texts into a PostgreSQL database 

Then produce valid XML in order to be able to operate on the different parts and tags.

### explore_db_texts.ipynb 


Explore the imported textual data: lenght, distribution, etc.

### db_produce_summaries.ipynb

Extract summaries in view of experimenting topic modeling and clustering


### get_persons_uris_dbpedia.ipynb

Linke the existing persons to DBpedia getting their URIs


<br/>


## Spacy and the Universe Plugins

Explore the functionality of the main library and its many extensions

### spacy_explore.ipynb

NLP treatement with Spacy and result stored in dedicated tables of the database (to be improved, adding vectors)


### coreference_resolver_neuralcoref.ipynb

Tested and not adopted

### spacy_coreference_resolver_spacy.ipynb

This notebook explores the own Spacy coreference resolver.


### coreference_resolver_coreferee_crossLingual.ipynb




<br/>



## Proof of Concept


### db_produce_spacy_model.ipynb

Create a data model using Spacy and store the result in a PostgreSQL database

### db_add_coreferee_resolved_texts.ipynb

Add coreferenced texts produced with Coreferee to the database


### get_persons_uris_wikidata.ipynb

Linke named entities to Wikidata using SPACY plugins



### explore_db_cooccurrences_analysis.ipynb

First exploration of frequent terms cooccurrences (to be improved)

### explore_db_entities_relationships.ipynb

Basic exploration of the NLP features in order to leverage them for entities' relationships extraction


### explore_db_named_entities_and_verbs.ipynb

More specific analysis of named entities and verbs frequency, and the semantic structure of specific relationships, with focus on the structure: "study at University of..."

### get_uris.ipynb

Link main persons to DBPaedia URIs

### explore_db_nlp_vectors.ipynb

Explore queries using vector similarities and distances (postgreSQL extension _pgvector_)

<br/>


## Results

<br/>


### explore_db_relation_extraction_synctactic_dependencies.ipynb

Initial results are promising, but the diversity of linguistic expressions for the same semantic content requires the construction of overly complex algorithms. Other methods, e.g. using LLM, should be tried out first.

<br/>

### spacy_openai_relation_extraction.ipynb

Two way of using the OpenAI API for information extraction were testes: 
 * produce sentences then apply Spacy model and extract relationships 
 * use ChatGPT to extract triples (and thus relationships) 