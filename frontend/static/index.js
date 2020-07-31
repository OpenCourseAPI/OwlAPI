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

// CodeJar editors currently rendered on the page
let codejars = {};

/**
 * Custom docsify plugin to create API playgrounds
 *
 * Usage - Add a comment as such in your .md file:
 * <!-- playground:api [<method>, <url>, <body>, <sample>] -->
 *
 * Note: the comment can span multiple lines.
 *
 * @param {string} method Type of method (currently "GET" or "POST")
 * @param {string} url The URL to hit
 * @param {string|Object} body URL search params for "GET", or JSON body for "POST"
 * @param {string|Object} sample (optional) Sample data to show
 *
 * @example <!-- playground:api ["GET", "/cars", "?year=2018" -->
 * @example <!-- playground:api ["GET", "/cars", "?year=2020", [{ "name": "Something" }]] -->
 * @example <!-- playground:api ["POST", "/cars/edit", { "id": 2342 }, { "status": "success" }] -->
 */
function apiPlayground(hook) {
  let idCounter = 0;

  // Perform cleanup
  hook.beforeEach((content) => {
    // Destroy previous editors
    Object.values(codejars).forEach((editor) => {
      editor.destroy();
    });
    codejars = {};
  });

  // Invoked each time after the Markdown file is parsed
  hook.afterEach((html, next) => {
    // Captures array in <!-- playground:api [...] -->
    const regex = /<!-- playground:api ([\s\S]*?) -->/gi;

    // Replace "magic" comment with HTML for API playground
    next(html.replace(regex, (match, capture) => {
      const [method, endpoint, body, sampleData = ''] = JSON.parse(capture);

      const url = method === 'GET' ? endpoint + body : endpoint;
      const info = sampleData ? ' (sample)' : '';
      // If sample data is provided, apply Prism.js syntax highlighting
      const sample = sampleData ? Prism.highlight(
        JSON.stringify(sampleData, undefined, 2),
        Prism.languages.json,
        'json',
      ) : '[send the request]';

      idCounter++;

      return `
        <div class="playground" id="playground-${idCounter}">
          <div class="send-request-row">
            <span class="label">${method}</span>
            <input class="url" value="${url}"></input>
            <button onclick="sendRequest('${method}', ${idCounter})">
              Send
            </button>
          </div>
          <div class="split-view">
            ${method === 'POST'
              ? `
                <div class="pane post-body">
                  <span class="label">BODY</span>
                  <div class="editor lang-json" data-id="${idCounter}">${JSON.stringify(body, undefined, 2)}</div>
                </div>
              ` : ''}
            <div class="pane">
              <div class="info">
                <span class="label">RESPONSE</span>
                <span class="data">${info}</span>
              </div>
              <pre class="response-data" data-lang="json">
                <code class="lang-json">${sample}</code>
              </pre>
            </div>
          </div>
        </div>
      `;
    }));
  });

  hook.doneEach(() => {
    // Create new editors
    document.querySelectorAll('.editor').forEach((el) => {
      codejars[el.dataset.id] = CodeJar(el, Prism.highlightElement);
    });
  });
}

// Send an API request
// TODO: add loading indication (animation, icon, etc.)
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
