## Simple data request

The best way to get started using OwlAPI is to see a basic example. With Javascript, there are many ways to make web requests. In this example, we aim to make a simple interface to the OwlAPI with an interactable module similar to the one seen on the main docs page. We will be hitting OwlAPI's [`/single`](https://opencourse.dev/#get-single) endpoint to retrieve a single entry from the database. It is the most basic interaction you can make to the API.

```
<!DOCTYPE html>
<html>
  <head>
    <title>OwlAPI interface</title>
    <meta name="viewport" content="initial-scale=1.0">
    <meta charset="utf-8">
    <style>
      body, html {
        display: grid;
        grid-template-rows: auto;
      }
      span, button, input, pre {
        font: 1.2em monospace;
      }
      input {
        width: 25vw;
        border: 0;
        border-bottom: 1px dashed black;
      }
      .content {
        margin:0 auto;
      }
    </style>
  </head>
  <body>
    <div id="input" class="content">
      <button onclick="submitRequest(this.parentElement)">GET</button>
      <span>https://opencourse.dev/fh/single</span>
      <input id="data" type="text" value="?dept=CS&course=2C">
    </div>
    <pre id="output" class="content"></pre>
  </body>
  <script>
    function submitRequest(input) {
      var data = input.querySelector('#data');
      var output = document.querySelector('#output');

      var url = new URL("https://opencourse.dev/fh/single" + data.value);

      fetch(url, {
          method: 'GET'
        })
        .then(response => {
          return Promise.resolve(response.json());
        })
        .then(json => {
          console.log(json);
          output.innerHTML = JSON.stringify(json, null, 2);
        })
        .catch(err => {
          console.log(err);
      });
    }
  </script>
</html>
```
[Try Example](/#)

### Overview

In this example, we have an input field where we can enter in valid query parameters to the [`/single`](https://opencourse.dev/#get-single) endpoint. Upon hitting the `GET` button, the JavaScript code uses the [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) to make a request to [opencourse.dev](https://opencourse.dev) with the query params attached. Upon receiving a response, it pretty prints the JSON data to the output container.

### HTML template

Firstly, let's cover the HTML template used in this example. In order to use HTML5, we establish the doctype via `<!DOCTYPE html>`.

Most current browsers will render content that is declared with this DOCTYPE in "standards mode" which means that your application should be more cross-browser compliant. The DOCTYPE is also designed to degrade gracefully; browsers that don't understand it will ignore it, and use "quirks mode" to display their content.

We are using a barebones `<body>` for simple input and output. It has a text field to enter in the request parameters for the `GET`, and a button to submit the request:
```
<body>
  <div id="input" class="content">
    <button onclick="submitRequest(this.parentElement)">GET</button>
    <span>https://opencourse.dev/single</span>
    <input id="data" type="text" value="?dept=CS&course=2C">
  </div>
  <pre id="output" class="content"></pre>
</body>
```

On the `<button>`, there is an [`onclick`](https://developer.mozilla.org/en-US/docs/Web/API/GlobalEventHandlers/onclick) event handlwer which upon clicking it, will call the function `submitRequest()` (covered later). An input field is initialized with a default `value` and can be changed freely.
A `<pre>` container will hold our output from the web request.

### CSS style
Now, let's cover the CSS used to format our template. It uses

The `<style>` in this example is simple:
```
<style>
  body, html {
    display: grid;
    grid-template-rows: auto;
  }
  span, button, input, pre {
    font: 1.2em monospace;
  }
  input {
    width: 25vw;
    border: 0;
    border-bottom: 1px dashed black;
  }
  .content {
    margin:0 auto;
  }
</style>
```

It employs the use of [CSS Grid](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout) Layout tools to center and display content nicely. Some additional styling is given to the font selection and size of the body's text.

### JavaScript code

In this example, we want to make a request based on the input field's query parameter string. We do this by using the Fetch API's [`fetch()`](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/fetch) to keep things framework agnostic and it's simplicity of use.

Upon receiving a response back from the server, we want to display the JSON data back to the user in a success. In the case of a failure, we want to display an error message back to the user.

The method `sumbitRequest()` is given as follows:
```
function submitRequest(input) {
  var data = input.querySelector('#data');
  var output = document.querySelector('#output');

  var url = new URL("https://opencourse.dev/single" + data.value);

  fetch(url, {
      method: 'GET'
    })
    .then(response => {
      return Promise.resolve(response.json());
    })
    .then(json => {
      console.log(json);
      output.innerHTML = JSON.stringify(json, null, 2);
    })
    .catch(err => {
      console.log(err);
  });
}
```

When `sumbitRequest()` is called, we pass in the `#input` element as a parameter. Then, using the [`querySelector`](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector) Document method, we extract the data from the `#data` input and prepare the `#output` container for content injection.

Next, we create a new URL from the data and use `fetch()` with `method: 'GET'` to make a request. The `.then()` and `.catch()` methods might be new to you, and they are something known as [Promise prototypes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/prototype). Using asynchronous operations like web requests require use of Promises to account for timing while getting data from an external source.

- [`.then()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/then) allows us to do something with the data after it has come back from the server, and can be chained with itself to perform additionally processing on the data.

- [`.catch()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/catch) operates in a similar fashion, allowing us to detect some errors that might occur during request process. It should be noted that `.catch()` will only raise on network errors; a HTTP status of `404` will not make `.catch()` trigger.

Upon recieving a valid response from the web server, we can now format our content into the `#output` container. We first convert the `JSON` data into a string format using [`JSON.stringify()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify). The parameters used here will format the JSON into a format that is easy to read for humans. Finally, We set the [`innerHTML`](https://developer.mozilla.org/en-US/docs/Web/API/Element/innerHTML) of the output container to the output string we generated.

### Conclusion

With this basic code, you should be able to successfully make `GET` requests to OwlAPI's `/single` endpoint using `Fetch API`; it provides a consistent method to make web requests easy, and can be used to make `POST` requests used advanced usage of OwlAPI. You can read more about making advanced queries and filters in the next section.
