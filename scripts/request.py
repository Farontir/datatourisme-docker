import requests
import json
import pandas as pandas

query = """
{
  poi(size: 100) {
    results {
      _uri
      rdfs_label {
        value
        lang
      }
      offers {
        _uri
        rdf_type
        schema_priceSpecification {
          schema_minPrice
          schema_maxPrice
        }
      }
    }
  }
}
"""

url = 'http://localhost:8080/'
r = requests.post(url, json={'query': query})

f = open("result.json", "w")

if r.status_code == 200:
  f.write(json.dumps(r.json(), indent=2))
f.close()
