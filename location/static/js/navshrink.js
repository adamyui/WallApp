

//GRAB LOCATION//
// getLocation()

// function getLocation() {
//     if (navigator.geolocation) {
//         navigator.geolocation.getCurrentPosition(showPosition);

//     } else { 
//         x.innerHTML = "Geolocation is not supported by this browser.";
//     }
// }

// function showPosition(position) {

//     document.getElementById('longitude').value = position.coords.longitude;
//     document.getElementById('latitude').value = position.coords.latitude;
    
// }

function disable_ani(){
  var ye = document.getElementById('lastbolt');
  ye.style.webkitAnimationPlayState = 'paused';
  var y = document.getElementById('boltrow1');
  y.style.webkitAnimationPlayState = 'paused';
  var yaa = document.getElementById('boltrow2');
  yaa.style.webkitAnimationPlayState = 'paused';
  var yb = document.getElementById('boltrow3');
  yb.style.webkitAnimationPlayState = 'paused';

  var yc = document.getElementById('boltrow4');
  yc.style.webkitAnimationPlayState = 'paused';




}
function enable_ani(){
  var ea = document.getElementById('lastbolt');
  ea.style.webkitAnimationPlayState = 'running';
  var ya = document.getElementById('boltrow1');
  ya.style.webkitAnimationPlayState = 'running';
  var aa = document.getElementById('boltrow2');
  aa.style.webkitAnimationPlayState = 'running';
  var ba = document.getElementById('boltrow3');
  ba.style.webkitAnimationPlayState = 'running';
  var ca = document.getElementById('boltrow4');
  ca.style.webkitAnimationPlayState = 'running';
}










