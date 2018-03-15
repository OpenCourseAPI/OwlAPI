document.addEventListener('DOMContentLoaded', function(){
  whenAvailable('#interact', forms => {
    [].forEach.call(forms, f => {
      var type = f.firstChild.dataset.requestType;
      var url = f.firstChild.dataset.requestUrl;
      var data = f.firstChild.dataset.requestBody;

      var el = document.createElement("div");
      el.innerHTML = generate_data(type, url, data);

      f.replaceChild(el, f.firstChild);
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

function generate_data(type, url, data) {
  var input = (type == 'GET') ? `<input class="input is-medium" id="data" type="text" value="${url + data}">` :
                                `<textarea class="input" id="body">${data}</textarea>`

  return `
          <div class="field has-addons text">
            <p class="control">
              <a class="button is-medium is-static" id="type">${type}</a>
            </p>
            <script type="form/url" data-url=${url}></script>
            <p class="control is-expanded">
              ${input}
            </p>
            <div class="control">
              <a class="button is-medium is-light is-inverted"
                 onclick="request_submit(event)">
                Submit
              </a>
            </div>
            <div class="modal" id="modal">
              <div class="modal-background" onclick="toggleModal(this.parentElement, false)"></div>
              <div class="modal-content"></div>
            </div>
          </div>
         `
}

function request_submit(event) {
  var field = event.target.parentElement.parentElement;
  var type = field.querySelector('#type').innerHTML;
  var url = field.querySelector('script[type="form/url"]').dataset.url;
  var data = (type == 'GET') ? field.querySelector('#data').value : field.querySelector('#body').innerHTML; ;

  var modal = field.querySelector('#modal');

  if (type == 'GET') {
    if (!data)
      data = " ";
    fetch(data, {
        method: 'GET',
      })
      .then(response => { updateModal(modal, response) })
      .catch(function(err) {
        console.info(err + " url: " + body);
    });
  }
  else if (type = 'POST') {
    fetch(url, {
        headers: {
          'Accept': 'application/json, application/xml, text/plain, text/html, *.*',
          'Content-Type': 'application/json'
        },
        method: 'POST',
        body: data
      })
      .then(response => { updateModal(modal, response) })
      .catch(function(err) {
        console.info(err + " url: " + url);
    });
  }
}

function updateModal(modal, response) {
  var res = Promise.resolve(response.json());
  var modalContent = modal.querySelector('.modal-content');

  res.then(json => {
    modalContent.innerHTML = `<pre>${JSON.stringify(json, undefined, 2)}</pre>`;
    toggleModal(modal, true);
  });
}

function toggleModal(modal, state) {
  state ? modal.classList.add('is-active') : modal.classList.remove('is-active');
}
