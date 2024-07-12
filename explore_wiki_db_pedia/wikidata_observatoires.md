


### Propriétés des observatoires

    PREFIX wikibase: <http://wikiba.se/ontology#>
    PREFIX wdt: <http://www.wikidata.org/prop/direct/>
    PREFIX wd: <http://www.wikidata.org/entity/>
    PREFIX bd: <http://www.bigdata.com/rdf#>

    SELECT ?p ?propLabel ?eff
    WHERE {
    SERVICE <https://query.wikidata.org/sparql> {
    {
        select ?p  (count(*) as ?eff)
        where {
            ?item wdt:P31 wd:Q62832;
            ?p ?o.
            }
        GROUP BY ?p 
        }
    ?prop wikibase:directClaim ?p .

    SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
    }                       } 
    ORDER BY DESC(?eff)



### Insérer les données

    PREFIX wikibase: <http://wikiba.se/ontology#>
    PREFIX wdt: <http://www.wikidata.org/prop/direct/>
    PREFIX wd: <http://www.wikidata.org/entity/>
    PREFIX bd: <http://www.bigdata.com/rdf#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    CONSTRUCT { ?item rdfs:label ?itemLabel.
            ?item a wd:Q62832.
            ?item wdt:P17 ?country.
            ?country rdfs:label ?countryLabel.}

    WHERE {  
        SERVICE <https://query.wikidata.org/sparql> 

        
        {
            SELECT ?item ?itemLabel ?country ?countryLabel
            WHERE {
                ?item wdt:P31 wd:Q62832.
                OPTIONAL {?item wdt:P17 ?country.}
                OPTIONAL {
                    SERVICE wikibase:label { bd:serviceParam wikibase:language "en".}
                }
        }
    }
    } 

#### INSERT

Exécuter la requête suivante sur ce point d'accès local _/personal_db/update_

Noter que si on veut effacer les mêmes triplets il suffit d'exécuter la même requête avec l'instruction _DELETE_

Noter que les données ont été mises dans un graphe dédié. Son URI est construite en ajoutant à la notion de localhost le nom du dataset et celle de la source.



    PREFIX wikibase: <http://wikiba.se/ontology#>
    PREFIX wdt: <http://www.wikidata.org/prop/direct/>
    PREFIX wd: <http://www.wikidata.org/entity/>
    PREFIX bd: <http://www.bigdata.com/rdf#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    WITH <http://localhost.org/personal_db/wikidata>
    INSERT { ?item rdfs:label ?itemLabel.
             ?item a wd:Q62832.            
            ?item wdt:P17 ?country.
            ?country rdfs:label ?countryLabel.}

    WHERE {  
        SERVICE <https://query.wikidata.org/sparql> 
        {
            SELECT ?item ?itemLabel ?country ?countryLabel
            WHERE {
                ?item wdt:P31 wd:Q62832;
                    wdt:P17 ?country.
        SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
        }
    }
    } 


### Explorer les données produites


    PREFIX wikibase: <http://wikiba.se/ontology#>
    PREFIX wdt: <http://www.wikidata.org/prop/direct/>
    PREFIX wd: <http://www.wikidata.org/entity/>
    PREFIX bd: <http://www.bigdata.com/rdf#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    SELECT ?country ?countryLabel (count(*) as ?eff)
        WHERE {
                GRAPH <http://localhost.org/personal_db/wikidata>
                {
                ?item a wd:Q62832;
                    wdt:P17 ?country.
                ?country rdfs:label ?countryLabel.
                }
    }
    GROUP BY ?country ?countryLabel
    ORDER BY DESC(?eff) 
