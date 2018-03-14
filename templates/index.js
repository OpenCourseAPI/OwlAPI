document.addEventListener('DOMContentLoaded', function(){
  var forms = document.querySelectorAll('script[type="form/interact"]');

  [].forEach.call(forms, f => {
    var type = f.dataset.requestType;
    var url = f.dataset.requestUrl;
    var body = f.dataset.requestBody;

    var el = document.createElement("div");
    el.innerHTML = generate_data(type, url, body);

    f.parentNode.replaceChild(el, f);
  });
}, false);

function generate_data(type, url, body) {
  var input = (type == 'GET') ? `<input class="input is-medium" id="body" type="text" value="${url + body}">` :
                                `<textarea class="textarea" id="body">${body.replace(/`/g,'')}</textarea>`

  return `
          <div class="field has-addons">
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
  // window.location.href = baseUrl;

  fetch(baseUrl + url, { method: type, redirect: 'follow'})
    .then(response => {
        // HTTP 301 response
    })
    .catch(function(err) {
        console.info(err + " url: " + baseUrl);
  });
}
