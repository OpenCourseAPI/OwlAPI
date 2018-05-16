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

    var sections = document.querySelectorAll("h3");
    sections.forEach(section => {
      var waypointDown = new Waypoint({
        element: section,
        handler: function(direction) {
          if (direction == 'down')
            updateMenu(section.id);
        },
        offset: function() {
          return section.scrollTop + 3;
        }
      });
      var waypointUp = new Waypoint({
        element: section,
        handler: function(direction) {
          if (direction == 'up')
            updateMenu(section.id);
        },
        offset: function() {
          return section.scrollTop - 3;
        }
      });
    });

    var numbers = document.querySelectorAll('.token.number');
    numbers.forEach(n => {
      n.classList.add('punctuation');
      n.classList.remove('number');
    });

    document.querySelector('#footer').classList.remove('is-hidden');
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

function updateMenu(sectionID) {
  document.querySelectorAll('.menu-item a.is-active:not(.unselectable)')[0].classList.remove('is-active');
  document.querySelectorAll(`.menu-item a[href*=${sectionID}]:not(.unselectable)`)[0].classList.add('is-active');
}

function generate_data(type, url, data) {
  var input = (type == 'GET') ? `<input class="input is-medium" id="data" type="text" value="${url + data}">` :
                                `<textarea class="input" id="data">${data}</textarea>`

  return `
          <div class="field has-addons text">
            <p class="control">
              <a class="button is-medium is-static left" id="type">${type}</a>
            </p>
            <script type="form/url" data-url=${url}></script>
            <p class="control is-expanded">
              ${input}
            </p>
            <div class="control" onclick="request_submit(this.parentElement)">
              <a class="button is-medium is-dark has-text-white right faa-parent animated-hover" id="button">
                <span>Send</span>
                <span class="icon is-small has-text-white faa-pulse animated-hover">
                  <i class="fas fa-paper-plane"></i>
                </span>
              </a>
            </div>
            <div class="modal" id="modal" aria-hidden="true">
              <div class="modal-background" onclick="toggleModal(this.parentElement, false)"></div>
              <div class="modal-content"></div>
            </div>
          </div>
         `
}

function request_submit(field) {
  var type = field.querySelector('#type').innerHTML;
  var url = field.querySelector('script[type="form/url"]').dataset.url;
  var data = field.querySelector('#data').value;

  var modal = field.querySelector('#modal');
  var button = field.querySelector('#button');
  button.classList.add('is-loading');

  if (type == 'GET') {
    if (!data)
      data = " ";
    fetch(data, {
      headers: {
        'Accept': 'application/json, application/xml, text/plain, text/html, *.*'
      },
        method: 'GET',
      })
      .then(response => {
        button.classList.remove('is-loading');
        updateModal(modal, button, response.status == 200 ? response.json() : response.body);
      })
      .catch(err => {
        button.classList.remove('is-loading');
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
      .then(response => {
        button.classList.remove('is-loading');
        updateModal(modal, button, response.status == 200 ? response.json() : response.body);
      })
      .catch(err => {
        console.info(err + " url: " + url);
        button.classList.remove('is-loading');
    });
  }
}

function updateModal(modal, button, response) {
  var res = Promise.resolve(response);
  var modalContent = modal.querySelector('.modal-content');

  res.then(json => {
    modalContent.innerHTML = `<pre>${JSON.stringify(json, undefined, 2)}</pre>`;
    toggleModal(modal, true);
  });
}

function toggleModal(modal, state) {
  state ? modal.classList.add('is-active') : modal.classList.remove('is-active');

  // state ? document.body.parentElement.classList.add('scroll-lock') : document.body.parentElement.classList.remove('scroll-lock');
  //
  // state ? document.body.classList.add('scroll-lock') : document.body.classList.remove('scroll-lock');
}
