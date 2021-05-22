$(document).ready(function () {
    $(".sidenav").sidenav();
    $('.tooltipped').tooltip();
});

 document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, options);
  });