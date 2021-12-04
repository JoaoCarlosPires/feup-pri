PYTHON = python3

.PHONY: setup collect-data analyse-data get-json

setup:
    pip install matplotlib
    pip install numpy
    pip install typing-extensions

collect-data: get-tmdb-data get-omdb-data remove-incomplete get-tmdb-reviews

get-tmdb-data:
    @echo "Getting TMDB popular animation movies information..."
    python tmdb-movies.py

get-omdb-data:
    @echo "Getting OMDB popular animation movies information..."
    python omdb-movies.py

remove-incomplete:
    @echo "Removing movies from TMDB without match in OMDB..."
    python remove-incomplete.py

get-tmdb-reviews:
    @echo "Getting TMDB popular animation movies reviews..."
    python tmdb-reviews.py

analyse-data:
    @echo "Analysing full movie dataset..."
    python data-analysis.py

get-json:
    @echo "Generating JSON file with whole movie dataset..."
    python generate-json.py