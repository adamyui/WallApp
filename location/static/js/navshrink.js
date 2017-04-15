// ;(function(){
//   var c = document.getElementById('glow');
//   var v = document.getElementById('click');
//   function addAnim() {
//     c.classList.add('animated')
//     v.removeEventListener('click', addAnim);
//   };

//   v.addEventListener('click', addAnim);
// })();




// document.getElementById('icon-click').onclick = function(){
//     element.style.webkitAnimationName = 'example';
//   .
// };


//GRAB LOCATION//
3

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);

    } else { 
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
}

function showPosition(position) {
    // x.= position.coords.longitude;
    // y.= position.coords.latitude; 


    document.getElementById('longitude').value = position.coords.longitude;
    document.getElementById('latitude').value = position.coords.latitude;
    // x =  position.coords.longitude;
    // y =  position.coords.latitude;
}