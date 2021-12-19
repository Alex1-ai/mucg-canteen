

var images = ["static/images/jollofrice5.jpg",
             "static/images/jollof4.jpg",
             "static/images/jollofrice6.jpg",
             "static/images/SuyaRice2.jpg",
             "static/images/jollofrice2.jpg"]


var imageHead = document.getElementById("image-head");

alert("Hello I am already installed");
var i = 0;
setInterval(function() {
      imageHead.style.background-image = "url(" + images[i] + ")";
      i = i + 1;
      if (i == images.length) {
        i =  0;
      }
}, 4);