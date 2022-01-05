import matplotlib.pyplot as plt
from sklearn.metrics import PrecisionRecallDisplay
import numpy as np
import json
import requests
import pandas as pd
import sys


qrel = ["query1.txt", "query2.txt", "query3.txt", "query4.txt", "query5.txt"]
qrels_file="query1.txt"
query_urls =[
    "http://localhost:8983/solr/movies/select?defType=edismax&debugQuery=true&indent=true&q.op=OR&stopwords=true&qs=3&ps=2&tie=0.1&q=toys%20that%20have%20life&qf=Title%5E8%20Rated%5E3%20Director%5E5%20Writer%5E5%20Actors%5E5%20Plot%5E10%20Language%5E2%20Country%5E1%20Awards%5E5%20Production%5E5%20Overview%5E10%20Reviews%5E9&pf=Title%5E3%20Plot%5E5%20Overview%5E5%20Reviews%5E4&bq=Awards%3Aoscar%5E7%20Awards%3Anom*%5E6%20Reviews%3Agood%5E7%20Reviews%3Aexcelent%5E7%20Reviews%3Abest%5E7%20Reviews%3Arecommend%5E7",
    "http://localhost:8983/solr/movies/select?defType=edismax&debugQuery=true&indent=true&q.op=OR&stopwords=true&qs=3&ps=2&tie=0.1&q=kid%20on%20trip%20to%20see%20santa%20claus&qf=Title%5E8%20Rated%5E3%20Director%5E5%20Writer%5E5%20Actors%5E5%20Plot%5E10%20Language%5E2%20Country%5E1%20Awards%5E5%20Production%5E5%20Overview%5E10%20Reviews%5E9&pf=Title%5E3%20Plot%5E5%20Overview%5E5%20Reviews%5E4&bq=Awards%3Aoscar%5E7%20Awards%3Anom*%5E6%20Reviews%3Agood%5E7%20Reviews%3Aexcelent%5E7%20Reviews%3Abest%5E7%20Reviews%3Arecommend%5E7",
    "http://localhost:8983/solr/movies/select?defType=edismax&debugQuery=true&indent=true&q.op=OR&stopwords=true&qs=3&ps=2&tie=0.1&q=ogre%20voiced%20by%20Mike%20Myers%20meets%20wifes%20parents&qf=Title%5E8%20Rated%5E3%20Director%5E5%20Writer%5E5%20Actors%5E5%20Plot%5E10%20Language%5E2%20Country%5E1%20Awards%5E5%20Production%5E5%20Overview%5E10%20Reviews%5E9&pf=Title%5E3%20Plot%5E5%20Overview%5E5%20Reviews%5E4&bq=Awards%3Aoscar%5E7%20Awards%3Anom*%5E6%20Reviews%3Agood%5E7%20Reviews%3Aexcelent%5E7%20Reviews%3Abest%5E7%20Reviews%3Arecommend%5E7",
    "http://localhost:8983/solr/movies/select?defType=edismax&debugQuery=true&indent=true&q.op=OR&stopwords=true&qs=3&ps=2&tie=0.1&q=rat%20learns%20how%20to%20cook&qf=Title%5E8%20Rated%5E3%20Director%5E5%20Writer%5E5%20Actors%5E5%20Plot%5E10%20Language%5E2%20Country%5E1%20Awards%5E5%20Production%5E5%20Overview%5E10%20Reviews%5E9&pf=Title%5E3%20Plot%5E5%20Overview%5E5%20Reviews%5E4&bq=Awards%3Aoscar%5E7%20Awards%3Anom*%5E6%20Reviews%3Agood%5E7%20Reviews%3Aexcelent%5E7%20Reviews%3Abest%5E7%20Reviews%3Arecommend%5E7"
    "http://localhost:8983/solr/movies/select?defType=edismax&debugQuery=true&indent=true&q.op=OR&stopwords=true&qs=3&ps=2&tie=0.1&q=animals%20ice%20sid&qf=Title%5E8%20Rated%5E3%20Director%5E5%20Writer%5E5%20Actors%5E5%20Plot%5E10%20Language%5E2%20Country%5E1%20Awards%5E5%20Production%5E5%20Overview%5E10%20Reviews%5E9&pf=Title%5E3%20Plot%5E5%20Overview%5E5%20Reviews%5E4&bq=Awards%3Aoscar%5E7%20Awards%3Anom*%5E6%20Reviews%3Agood%5E7%20Reviews%3Aexcelent%5E7%20Reviews%3Abest%5E7%20Reviews%3Arecommend%5E7"
]
SCHEMA=-1

query_url = ""
rel_filename = ""

''''
if len(sys.argv) < 3:
    print("Query not specified")
else:
    if 4 < int(sys.argv[1]) < 1:
        print("Query is not valid")
        sys.exit()
    rel_filename = qrels_file[int(sys.argv[1]) - 1]
    query_url = query_urls[int(sys.argv[1]) - 1]
    '''
print(len(rel_filename))

# Read qrels to extract relevant documents
relevant = list(map(lambda el: el.strip(), open("query1.txt").readlines()))
# Get query results from Solr instance
results = requests.get("http://localhost:8983/solr/movies/select?defType=edismax&debugQuery=true&indent=true&q.op=OR&stopwords=true&qs=3&ps=2&tie=0.1&q=toys%20that%20have%20life&qf=Title%5E8%20Rated%5E3%20Director%5E5%20Writer%5E5%20Actors%5E5%20Plot%5E10%20Language%5E2%20Country%5E1%20Awards%5E5%20Production%5E5%20Overview%5E10%20Reviews%5E9&pf=Title%5E3%20Plot%5E5%20Overview%5E5%20Reviews%5E4&bq=Awards%3Aoscar%5E7%20Awards%3Anom*%5E6%20Reviews%3Agood%5E7%20Reviews%3Aexcelent%5E7%20Reviews%3Abest%5E7%20Reviews%3Arecommend%5E7").json()['response']['docs']


df = pd.DataFrame(['relevant','results'])
with open('mytable.tex','w') as tf:
    tf.write(df.to_latex())


# METRICS TABLE
# Define custom decorator to automatically calculate metric based on key
metrics = {}
metric = lambda f: metrics.setdefault(f.__name__, f)

@metric
def ap(results, relevant):
    """Average Precision"""
    precision_values = [
        len([
            doc 
            for doc in results[:idx]
            if doc['id'] in relevant 
        ]) / idx 
        for idx in range(1, len(results))
    ]
    return sum(precision_values)/len(precision_values)

@metric
def p10(results, relevant, n=10):
    """Precision at N"""
    return len([doc for doc in results[:n] if doc['id'] in relevant])/n 

def calculate_metric(key, results, relevant):
    return metrics[key](results, relevant)

# Define metrics to be calculated
evaluation_metrics = {
    'ap': 'Average Precision',
    'p10': 'Precision at 10 (P@10)'
}

# Calculate all metrics and export results as LaTeX table
df = pd.DataFrame([['Metric','Value']] +
    [
        [evaluation_metrics[m], calculate_metric(m, results, relevant)]
        for m in evaluation_metrics
    ]
)

with open('results.tex','w') as tf:
    tf.write(df.to_latex())


# PRECISION-RECALL CURVE
# Calculate precision and recall values as we move down the ranked list
precision_values = [
    len([
        doc 
        for doc in results[:idx]
        if doc['id'] in relevant 
    ]) / idx 
    for idx, _ in enumerate(results, start=1)
]

recall_values = [
    len([
        doc for doc in results[:idx]
        if doc['id'] in relevant
    ]) / len(relevant)
    for idx, _ in enumerate(results, start=1)
]

precision_recall_match = {k: v for k,v in zip(recall_values, precision_values)}

# Extend recall_values to include traditional steps for a better curve (0.1, 0.2 ...)
recall_values.extend([step for step in np.arange(0.1, 1.1, 0.1) if step not in recall_values])
recall_values = sorted(set(recall_values))

# Extend matching dict to include these new intermediate steps
for idx, step in enumerate(recall_values):
    if step not in precision_recall_match:
        if recall_values[idx-1] in precision_recall_match:
            precision_recall_match[step] = precision_recall_match[recall_values[idx-1]]
        else:
            precision_recall_match[step] = precision_recall_match[recall_values[idx+1]]

disp = PrecisionRecallDisplay([precision_recall_match.get(r) for r in recall_values], recall_values)
disp.plot()
plt.savefig('precision_recall.pdf')


