
$(function() {
   $('form').submit(function() {
      if(!$("form input[type=file]").val()) {
         alert('You must select a file!');
         return false;
      }
   });
});
