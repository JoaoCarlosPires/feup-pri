from types import resolve_bases
from urllib.request import urlopen
import json
from flask import Flask, request, render_template

app = Flask(__name__)
  
@app.route('/',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
      text = request.form['user_query']
    else:
      text = request.args.get('user_query')

    if text != '':
        # Get user query / search
        user_input = text.replace(" ", "%20")

        # Base url
        query = "http://localhost:8983/solr/movies/select?"

        # Filters and parameters
        query += "defType=edismax"
        query += "&indent=true"
        query += "&q.op=OR"
        query += "&stopwords=true"
        query += "&qs=3"
        query += "&ps=2"
        query += "&tie=0.1"

        query += "&q=" + user_input

        query += "&qf="
        fields_to_search = [["Title", "8"], 
                            ["Rated", "3"],
                            ["Director", "5"],
                            ["Writer", "5"],
                            ["Actors", "5"],
                            ["Plot", "10"],
                            ["Language", "2"],
                            ["Country", "1"],
                            ["Awards", "5"],
                            ["Production", "5"],
                            ["Overview", "10"],
                            ["Reviews", "9"]]
        for field in fields_to_search:
            query += field[0] + "%5E" + field[1]
            if (fields_to_search.index(field) != (len(fields_to_search)-1)):
                query += "%20"

        query += "&pf="
        phrase_fields = [["Title", "3"], 
                        ["Plot", "5"],
                        ["Overview", "5"],
                        ["Reviews", "4"]]
        for p_field in phrase_fields:
            query += p_field[0] + "%5E" + p_field[1]
            if (phrase_fields.index(p_field) != (len(phrase_fields)-1)):
                query += "%20"

        query += "&bq="
        boost_fields = [["Awards", "oscar", "7"],
                        ["Awards", "nom*", "6"],
                        ["Reviews", "good", "7"],
                        ["Reviews", "excellent", "7"],
                        ["Reviews", "best", "7"],
                        ["Reviews", "recommend*", "7"]]
        for boost in boost_fields:
            query += boost[0] + "%3A" + boost[1] + "%5E" + boost[2]
            if (boost_fields.index(boost) != (len(boost_fields)-1)):
                query += "%20"

        # Get JSON response
        response = urlopen(query)
        json_response = json.loads(response.read())

        return render_template('results.html', json=json_response['response']['docs'])
    else:
        return render_template('search.html')

if __name__ == '__main__':
   app.run(debug = True)

