function showAlert(message) {
    var alert = document.getElementById('alert');
    var alertText = document.getElementById('text');

    text.textContent = message;
    alert.style.opacity = '1';

    setTimeout(function () {
        closeAlert();
      }, 8000);
  }

  // Função para fechar o alerta
  function closeAlert() {
    var alert = document.getElementById('alert');
    alert.style.opacity = '0';
  }