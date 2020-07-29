const isMobileDevice = /Mobi/i.test(window.navigator.userAgent);

window.$docsify = {
  name: 'Owl API',
  repo: 'OpenCourseAPI/OwlAPI',
  homepage: 'introduction.md',
  basePath: '/docs/',
  maxLevel: 3,
  loadSidebar: true,
  subMaxLevel: 3,
  auto2top: true,
  alias: {
    '/.*/_sidebar.md': '/_sidebar.md',
  },
  plugins: [
    apiPlayground,
  ],
};

let codejars = {};
let idCounter = 0;

// Custom docsify plugin to create API playgrounds
function apiPlayground(hook) {
  // Invoked each time after the Markdown file is parsed
  hook.afterEach(function(html, next) {
    // Captures array in <!-- playground:api [...] -->
    const regex = /<!-- playground:api ([\s\S]*?) -->/gi;

    next(html.replace(regex, (match, capture) => {
      const [method, url, body, defaultData = ''] = JSON.parse(capture);
      const sample = defaultData ? Prism.highlight(
        JSON.stringify(defaultData, undefined, 2),
        Prism.languages.json,
        'json',
      ) : '[send the request]';
      const initialInfo = `${defaultData ? ' (sample)' : ''}`;

      idCounter++;

      return `
        <div class="playground" id="playground-${idCounter}">
          <div class="box">
            <div class="split-row">
              <span class="method">${method}</span>
              <input value="${method === 'GET' ? url + body : url}"></input>
              <button onclick="sendRequest('${method}', ${idCounter})">
                Send
              </button>
            </div>
            <div class="split-view">
              ${method === 'POST'
                ? `
                  <div class="left-pane">
                    <span class="method">BODY</span>
                    <div class="editor lang-json" data-id="${idCounter}">${JSON.stringify(body, undefined, 2)}</div>
                  </div>
                ` : ''}
              <div class="right-pane">
                <div class="info">
                  <span class="status">RESPONSE</span>
                  <span class="data">${initialInfo}</span>
                </div>
                <pre class="response" data-lang="json">
                  <code class="lang-json">${sample}</code>
                </pre>
              </div>
            </div>
          </div>
        </div>
      `;
    }));
  });

  hook.doneEach(() => {
    // Destroy previous editors
    // TODO: verify this is the right hook to destroy
    Object.values(codejars).forEach((editor) => {
      editor.destroy();
    });
    codejars = {};
    // Create new editors
    document.querySelectorAll('.editor').forEach((el) => {
      codejars[el.dataset.id] = CodeJar(el, Prism.highlightElement);
    });
  });
}

// Send an API request
async function sendRequest(method, id) {
  const playground = document.getElementById(`playground-${id}`);
  const urlInput = playground.querySelector('input');
  const info = playground.querySelector('.info .data');
  const display = playground.querySelector('code');

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
      display.textContent = 'Error: Unable to parse JSON body\n' + err;
      return;
    }

    // Send POST request
    response = await fetch(urlInput.value, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body,
    });
  }

  const { status, statusText } = response;
  info.innerHTML = status + (statusText ? ` - ${statusText}` : '');

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
