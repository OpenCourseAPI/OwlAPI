const isMobileDevice = /Mobi/i.test(window.navigator.userAgent);

window.$docsify = {
  name: 'Owl API',
  maxLevel: 3,
  subMaxLevel: 3,
  basePath: '/docs/',
  loadSidebar: true,
  plugins: [
    apiPlayground,
    apiPlaygroundHide,
  ],
};

const codejars = {};
let idCounter = 0;

function apiPlaygroundHide(hook) {
  // Invoked each time before parsing the Markdown file.
  hook.beforeEach(function(content) {
    const regex = /<!-- playground:hide-start -->([\s\S]*?)<!-- playground:hide-end -->/gim;
    return content.replace(regex, '');
  });
}

function apiPlayground(hook) {
  // Invoked each time after the Markdown file is parsed.
  hook.afterEach(function(html, next) {
    const regex = /<!-- playground:api ([\s\S]*?) -->/gi;

    next(html.replace(regex, (match, capture) => {
      const [method, url, body, defaultData = ''] = JSON.parse(capture);
      const sample = defaultData ? Prism.highlight(
        JSON.stringify(defaultData, undefined, 2),
        Prism.languages.json,
        'json',
      ) : '';

      idCounter++;

      return `
        <div class="playground">
          <div class="box">
            <div class="split-row">
              <span class="method">${method}</span>
              <input id="url-input-${idCounter}" value="${method === 'GET' ? url + body : url}"></input>
              <button onclick="sendRequest('${method}', ${idCounter})">
                Send
              </button>
            </div>
            <div>
              ${method === 'POST'
                ? `<div class="editor lang-json" data-id="${idCounter}">${JSON.stringify(body, undefined, 2)}</div>`
                // ? `<textarea rows="10" id="body-input-${idCounter}">${JSON.stringify(body, undefined, 2)}</textarea>`
                : ''}
            </div>
            <pre class="response" data-lang="json">
              <code id="response-${idCounter}" class="lang-json">${sample}</code>
            </pre>
          </div>
        </div>
      `;
    }));
  });

  hook.ready(() => {
    document.querySelectorAll('.editor').forEach((el) => {
      codejars[el.dataset.id] = CodeJar(el, Prism.highlightElement);
    });
  });
}

async function sendRequest(method, id) {
  const urlInput = document.getElementById(`url-input-${id}`);
  // const bodyInput = document.getElementById(`body-input-${id}`);
  const display = document.getElementById(`response-${id}`);

  let response;

  if (method === 'GET') {
    // Send GET request
    response = await fetch(urlInput.value);
  } else if (method === 'POST') {
    // Get JSON body from codejar editor
    const body = codejars[id].toString();

    // Validate JSON body
    try {
      JSON.parse(body);
    } catch (err) {
      display.textContent = 'Error: Unable to parse JSON\n' + err;
      return;
    }

    // Send POST request
    response = await fetch(urlInput.value, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body,
      // body: bodyInput.value,
    });
  }

  let data = await response.text();

  // Try parsing response as JSON, and fall back to just text
  try {
    data = JSON.stringify(JSON.parse(data), undefined, 2);
    display.textContent = data;
    // Only syntax highlight if the device is not a mobile
    // or the data is sufficiently small
    if (!isMobileDevice || data.length < 4000) {
      Prism.highlightElement(display);
    }
  } catch (err) {
    display.textContent = data;
  }
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
