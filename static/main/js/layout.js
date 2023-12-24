/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown if the user clicks outside of it
window.onclick = function (event) {
if (!event.target.classList.contains('dropbtn') && !event.target.classList.contains('input-group-text')) {
      const dropdowns = document.getElementsByClassName("dropdown-content");
      let i;
      for (i = 0; i < dropdowns.length; i++) {
          const openDropdown = dropdowns[i];
           
    }
  }
}

window.addEventListener('scroll', function() {
      const header = document.getElementById('header');
      if (window.pageYOffset > 0) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }
    });
    window.addEventListener('resize', function() {
      var footer = document.querySelector('.site-footer');
      var bodyHeight = document.body.offsetHeight;
      var windowHeight = window.innerHeight;

      if (bodyHeight < windowHeight) {
        footer.style.position = 'fixed';
      } else {
        footer.style.position = 'static';
      }
});