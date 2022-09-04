# feup-pri

## How to start Solr with the schema and collections uploaded

### 1. Start by build the docker image with:

```console
docker build . -t movies
```

### 2. Next, run the container using: 
   
```console
docker run -p 8983:8983 movies
```

### 3. Open http://localhost:8983 to use Solr 

### **OR**

### 3. Type on the console:

```console
make solr-gui
```

### and then open [templates/search.html](templates/search.html) on your browser to use the GUI.

---

**Note:** If you don't have ``Flask``, ``googletrans`` or ``sparqlwrapper`` installed, just type

```console
make setup
```

on the console to install all the dependencies.

---

## Reference links

https://solr.apache.org/guide/8_11/the-dismax-query-parser.html

https://solr.apache.org/guide/8_11/the-extended-dismax-query-parser.html
