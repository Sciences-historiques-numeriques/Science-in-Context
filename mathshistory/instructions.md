# Environments, dependencies and technical instructions




## Managing dependencies

* Execute in the mathshistory folder

```
conda env export --from-history > environment.yml
```

* Add a date in the name of the environment, the last one, the more recent one is the one to be used to crate a new one
* You will add there manually the pip libraries with the structure:
```

```


## Conda Pip Spacy environment

This environment has to be created in order to be able to use spacy extensions 
that are not available in Conda

```
conda create -n py310_pip_spacy python=3.10 pip ipykernel

conda activate py310_pip_spacy

pip install crosslingual-coreference

python -m spacy download en_core_web_lg

### https://github.com/explosion/spacy-transformers
pip install 'spacy[transformers]'
python -m spacy download en_core_web_trf  ### n'a pas de vecteur mais plus précis

pip install coreferee
python -m coreferee install en

pip insall itables
pip install pandas psycopg2

pip install neuralcoref
pip install neuralcoref --use-pep517

pip install spacyopentapioca

pip install spacy-entity-linker
python -m spacy_entity_linker "download_knowledge_base"


```

### Using the environment

Activate the environment in Jupyter La

```
conda activate py310_pip_spacy
jupyter kernelspec list
python -m ipykernel install --user --name py310_pip_spacy
```
