var getUrl = '/email';
var getParams = {
  credentials: "include",
  method: "GET"
}

var token = "";

fetch(getUrl, getParams)
.then(text=> text.text())
.then(res=> doPost(res));

function doPost(res) {
  token = res.match(/csrf" value="(.*)"/)[1]
  var Url = '/email/change-email';
  var params = {
    credentials: "include",
    body: "email=aaa@mail.com&csrf="+token,
    method:"POST"
  }

  fetch(Url, params)
  .then(data=> {return data})
  .then(res=> {console.log(res)})
}
