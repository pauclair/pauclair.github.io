<script type = "text/javascript">
   function loadHTMLDb() {
      if (localStorage.planning) {
         var planning = document.getElementById("planning")
         planning.innerHTML = localStorage.planning
      }
   }

   function saveHTMLDb() {
      var planning = document.getElementById("planning")
      localStorage.planning = planning.innerHTML
   }

   function book(event) {
      bookedClassIndex = event.target.className.indexOf(" booked")
      if (bookedClassIndex !== -1) {
         className = event.target.className.substring(0, bookedClassIndex)
         event.target.setAttribute("class", className)
         return
      }
      if (event.target.nodeName == "TD" && event.target.className != "noday") {
         className = event.target.className + " booked"
         event.target.setAttribute("class", className)
      }
   }

   function cpyToHtmlTextContent() {
      var planning = document.getElementById("planning")
      var HtmlTextContent = document.getElementById("HtmlTextContent")
      HtmlTextContent.innerHTML = planning.innerHTML
      HtmlTextContent.focus()
      HtmlTextContent.select()
      this.saveHTMLDb()
   }
</script>


