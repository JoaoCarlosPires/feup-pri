# feup-pri

## How to start Solr with the schema and collections uploaded

1. Start by build the docker image with:

```console
docker build . -t movies
```

2. Next, run the container using: 
   
```console
docker run -p 8983:8983 movies
```

3. Open http://localhost:8983 to use Solr **OR** run the query.py script using ```python3 query.py``` and inserting the text query right after (e.g. "toys that have life").

## Reference links

https://solr.apache.org/guide/8_11/the-dismax-query-parser.html

https://solr.apache.org/guide/8_11/the-extended-dismax-query-parser.html
