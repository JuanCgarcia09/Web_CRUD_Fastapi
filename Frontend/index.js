var alo;
function enviar(){
  $.ajax({
    url: "http://127.0.0.1:8000/users",
  })
  .done(function (msg) {
           creartabla(msg);
       });
          //   $.ajax({   
          //     type: "POST",
          //     dataType: "html",
          //     data: {
          //       "grant_type": null,
          //       "username": "Juancgarcia",
          //       "password": "123456",
          //       "scopes": [],
          //       "client_id": null,
          //       "client_secret": null
          //     }, 
          //     cache: false,  
          //     url: "http://127.0.0.1:8000/basicauth/login"
          // })
          //   .done(function (msg) {
          //       creartabla();
          //   });
}
function creartabla(mensaje){
  var result = [];

  for(var i in mensaje)
      result.push([mensaje [i]]);
  console.log(result[0][0].name);
  let tabla = $('.tabla')
  tabla.html('')
  tabla.append("<table>" +
      "<thead>" +
      "<tr>" +
      "<th>Usuarioid</th>" +
      "<th>Nombre</th>" +
      "<th>URL</th>" +
      "<th>Edad</th>" +
      "</tr>" +
      "</thead>" +
      "<tbody id='res'>" +
      "</tbody>" +
      "</table>")
  for (let i of result) {
      $('#res').append("<tr>" +
          "<td>" + i[0].id + "</td>" +
          "<td>" + i[0].name + "</td>" +
          "<td>" + i[0].url + "</td>" +
          "<td>" + i[0].age + "</td>" +
          "</tr>"
      )
  }
  window.location("#close")
}
