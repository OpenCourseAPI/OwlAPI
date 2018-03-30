## Examples

This is a list of examples to use the API. The examples are written in Javascript and Python.


### Basic GET requests

> Javascript
```
fetch(data, {
  headers: {
    'Accept': 'application/json'
  },
    method: 'GET',
  })
  .then(response => {
    return Promise.resolve(response.json());
  })
  .then(json => {
    console.log(json);
  });
```

> Python
```
import requests

r = requests.get(FACT_URL)
json = r.json()
print(json)
```
