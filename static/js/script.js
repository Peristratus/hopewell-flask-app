

$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $('.dropdown-trigger').dropdown();
    $('.collapsible').collapsible();
    $('.tooltipped').tooltip();
    $('select').formSelect();
    $('.datepicker').datepicker({
        format: "dd mmmm, yyyy",
        yearRange: [1930,2021],
        showClearBtn: true,
        i18n: {
            done: "Select"
        }

     });
  });