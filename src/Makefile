PYTHON = python3

.PHONY: setup collect-data analyse-data get-json

setup:
	pip install matplotlib
	pip install numpy
	pip install typing-extensions
	pip install Flask
	pip install sparqlwrapper
	pip install googletrans==3.1.0a0

collect-data:
	get-tmdb-data get-omdb-data remove-incomplete get-tmdb-reviews

get-tmdb-data:
	@echo "Getting TMDB popular animation movies information..."
	$(PYTHON) tmdb-movies.py

get-omdb-data:
	@echo "Getting OMDB popular animation movies information..."
	$(PYTHON) omdb-movies.py

remove-incomplete:
	@echo "Removing movies from TMDB without match in OMDB..."
	$(PYTHON) remove-incomplete.py

get-tmdb-reviews:
	@echo "Getting TMDB popular animation movies reviews..."
	$(PYTHON) tmdb-reviews.py

analyse-data:
	@echo "Analysing full movie dataset..."
	$(PYTHON) data-analysis.py

get-json:
	@echo "Generating JSON file with whole movie dataset..."
	$(PYTHON) generate-json.py

solr-gui:
	@echo "Importing lemmas..."
	$(PYTHON) lexemes.py -c movies
	@echo "Starting GUI..."
	$(PYTHON) query.py
	@echo "Open templates/search.html to use the GUI."