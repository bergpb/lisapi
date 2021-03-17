const url = location.pathname.split("/")[1]

$(function() {
  if (url == ""){
    return $('#dashboard').addClass('teal lighten-2');
  }
  return $('.sidenav a[href^="/' + url + '"]').addClass('teal lighten-2');
});

$(document).ready(function(){
  $('.sidenav').sidenav();
});

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

(function() {
  if('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
      navigator.serviceWorker.register('/sw.js').then(function(registration) {
        return registration;
      })
      .catch(function(err) {
        console.error('Unable to register service worker.', err);
      });
      navigator.serviceWorker.ready.then(function(registration) {
        if(!registration) {
          console.log('Fail to register service worker.')
        }
      });
    });
  }
})();
