function showToast(text, type){
  swal({});
  const toast = swal.mixin({
    toast: true,
    position: 'top-end',
    showConfirmButton: false,
    timer: 3000
  });
  toast({
    type: type,
    title: text
  });
}

function showSwLink(title, type, showCancel, textConfirm, colorConfirm, link){
  swal({
    title: title,
    type: type,
    showCancelButton: showCancel,
    confirmButtonText: textConfirm,
    confirmButtonColor: colorConfirm,
  }).then((result) => {
    if (result.value){
      window.location.href = link;
    }
  });
}

function sidenavSelect(path){
  let color = 'teal lighten-5';
  switch (path) {
    case '/':
        $('#dashboard').addClass(color);
        break;
    case '/control':
        $('#control_pins').addClass(color);
        break;
    case '/list':
        $('#list_pins').addClass(color);
        break;
    case '/change_password':
        $('#change_password').addClass(color);
        break;
    case '/logout':
        $('#logout').addClass(color);
        break;
    case '/login':
        $('#login').addClass(color);
        break;
    case '/about':
        $('#about').addClass(color);
        break;
  }
}
