// Variáveis globais
var file = null;

// Requisição AJAX para subir um arquivo ao servidor
function uploadFile() {

  // Prepara os parâmetros de entrada com o formdata
  var formData = new FormData();

  // Desabilitando o botão de enviar
  let button = document.querySelector(".btn");
  //let demo = document.getElementById("demo").innerHTML="<div class="spinner-border text-primary" role="status"><span class="sr-only">Loading...</span></div>";

  button.disabled = true;
  button.innerText = "PROCESSANDO...";



  formData.append("fileNumber", $("#fileNumber").val());
  formData.append("uploadedFile", file, file.name);

  var parameters = {
    fileNumber: document.getElementById("fileNumber").value,
    uploadedFile: file,
  };

  // Recebe o token csrf que deve ser enviado junto à requisição post
  const csrftoken = getCookie('csrftoken');

  $.ajax({
    method: 'POST',
    headers: { 'X-CSRFToken': csrftoken },
    processData: false,
    contentType: false,
    cache: false,
    url: '/ajax/uploadFile/',
    data: formData,
    dataType: 'multipart/form-data',
    success: function (response) {
      console.log('SUCESSO: ' + response.message);

    },
    error: function (message) {
      //Console.error(JSON.stringify(message));
      console.log(button);
      alert("Arquivo enviado com sucesso.");
      button.disabled = false;
      button.innerText = "ENVIAR O ARQUIVO";
    }
  });
}

// Função necessária para recuperar o token csrf
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

// Evento que ocorre quando um arquivo é realizado o upload de um arquivo
$('input[type=file]').on('change', prepareUpload);
function prepareUpload(event) {
  file = event.target.files[0];
}


// Função necessária para recuperar o token csrf
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

// Evento que ocorre quando um arquivo é realizado o upload de um arquivo
$('input[type=file]').on('change', prepareUpload);
function prepareUpload(event) {
  file = event.target.files[0];
}
