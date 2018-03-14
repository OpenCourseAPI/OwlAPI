document.addEventListener('DOMContentLoaded', function(){
  var forms = document.querySelectorAll('script[type="form/interact"]');

  whenAvailable('script[type="form/interact"]', function(forms) {
    [].forEach.call(forms, f => {
      var type = f.dataset.requestType;
      var url = f.dataset.requestUrl;
      var body = f.dataset.requestBody;

      var el = document.createElement("div");
      el.innerHTML = generate_data(type, url, body);

      f.parentNode.replaceChild(el, f);
    });

    var numbers = document.querySelectorAll('.token.number');

    numbers.forEach(n => {
      n.classList.add('punctuation');
      n.classList.remove('number');
    });
  });

}, false);

function whenAvailable(name, callback) {
    var interval = 10; // ms
    window.setTimeout(function() {
        var forms = document.querySelectorAll(name);
        if (forms.length) {
            callback(forms);
        } else {
            window.setTimeout(arguments.callee, interval);
        }
    }, interval);
}

function generate_data(type, url, body) {
  var input = (type == 'GET') ? `<input class="input is-medium" id="body" type="text" value="${url + body}">` :
                                `<textarea class="textarea is-small" id="body" rows="1">${body}</textarea>`

  return `
          <div class="field has-addons text">
            <script type="form/url" data-url=${url}></script>
            <p class="control">
              <a class="button is-medium is-static" id="type">${type}</a>
            </p>
            <p class="control is-expanded">
              ${input}
            </p>
            <div class="control">
              <a class="button is-medium is-light is-inverted"
                 onclick="request_submit(event)">
                Submit
              </a>
            </div>
          </div>
         `
}

function request_submit(event) {
  var field = event.target.parentElement.parentElement;
  var type = field.querySelector('#type').innerHTML;
  var url = field.querySelector('script[type="form/url"]').dataset.url;
  var body = field.querySelector('#body');

  body = (type == 'GET') ? body.value : body.innerHTML;

  var baseUrl = "http://floof.li";

  if (type == 'GET') {
    if (!body)
      body = " ";
    fetch(baseUrl + body, {
        method: 'GET',
        redirect: 'follow',
      })
      .then(response => {
          //
      })
      .catch(function(err) {
          console.info(err + " url: " + baseUrl);
    });
  }
  else if (type = 'POST') {
    fetch(baseUrl + url, {
        headers: {
          'Content-Type': 'application/json'
        },
        method: 'POST',
        redirect: 'follow',
        body: body
      })
      .then(response => {
          //
      })
      .catch(function(err) {
          console.info(err + " url: " + baseUrl);
    });
  }
}
