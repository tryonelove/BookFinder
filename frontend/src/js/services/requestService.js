async function makeRequest(requestType, URL, data) {
  console.log(data)
  let response = await fetch(`http://localhost:5000${URL}`, {
    method: `${requestType}`,
    mode: 'cors',
    headers: {
      'Content-Type': 'application/json'
    },
    body:  JSON.stringify(data),
  });
  console.log(response.url);
  return await response.json();
}

class RequestService {
  get(URL, data) {
    return makeRequest("GET", URL, data);
  }
  post(URL, data) {
    return makeRequest("POST", URL, data);
  }
}

export default new RequestService();
