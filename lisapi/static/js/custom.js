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

let url = location.pathname.split("/")[1]

$(function() {
  if (url != ''){
      $('.sidenav a[href^="/' + url + '"]').addClass('teal lighten-5');
  }
});