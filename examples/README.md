## Examples

This documentation is designed for people new to JavaScript programming and making API requests. It is designed to let you quickly start exploring and developing applications with MyPortal data.

### Hello, World

The best way to get started using OwlAPI is to see a basic example. With Javascript, there are many ways to make web requests. In this example we use the `Fetch API` to make requests to [floof.li](https://floof.li). You can read more about `Fetch` [here](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/fetch).

In this example, we aim to make a simple interface to the OwlAPI with an interactable module similar to the one seen on the main docs page.

```
<!DOCTYPE html>
<html>
  <head>
    <title>OwlAPI interface</title>
    <meta name="viewport" content="initial-scale=1.0">
    <meta charset="utf-8">
    <style>
      body, html {
        height: 100%;
        display: grid;
      }
      .content {
        margin: auto;
      }
    </style>
  </head>
  <body>
    <div class="content">
      <div id="input">
        <button onclick="submitRequest(this.parentElement)">GET</button>
        <span>http://floof.li/single</span>
        <input id="data" type="text" value="?dept=CS&course=2C">
      </div>
      <div id="output"></div>
    </div>
  </body>
  <script>
    function submitRequest(input) {
      var data = input.querySelector('#data').value;

      var url = new URL("http://floof.li/single" + data);

      fetch(url, {
          method: 'GET'
        })
        .then(response => {
          return Promise.resolve(response.json());
        })
        .then(data => {
          console.log(JSON.stringify(data));
        })
        .catch(err => {
          console.log(err);
      });
    }
  </script>
</html>
```