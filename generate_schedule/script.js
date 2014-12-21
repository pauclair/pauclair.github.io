<div class="row">
  <div class="large-12 columns">
     <a href="#" id="save" class="button postfix">Save</a>
  </div>
</div>

<script src="js/vendor/jquery.js" type="text/javascript"></script>
<script src="js/foundation.min.js" type="text/javascript"></script>
<script src="js/foundation-datepicker.js" type="text/javascript"></script>

 <script>
 $(function() {
    if (localStorage.planning) {
       $(planning)[0].innerHTML = localStorage.planning;
    }           
 });
 $(function() {
    var cell = $('td');    
    $(cell).click(function() {
       if (!$(this).hasClass("noday")) {
          if ($(this).hasClass("booked")) {
     			$(this).removeClass("booked")          
          } else {
    			$(this).addClass("booked")
          }
       }
    });
 });
 </script>
 <script>
 $(function() {
    var planning = $('#planning');
    var saveButton = $('#save');    
    $(saveButton).click(function() {
		localStorage.planning = $(planning)[0].innerHTML;
    });
 });
 </script>
 
<script type="text/javascript">
   $(document).foundation();
</script>