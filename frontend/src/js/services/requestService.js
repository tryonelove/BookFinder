async function makeRequest(requestType, URL, data) {
  const response = await fetch(`http://192.168.56.101:5000${URL}`, {
    method: `${requestType}`,
    body: JSON.stringify(data),
  });
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
