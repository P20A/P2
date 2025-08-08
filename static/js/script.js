// ------------------slider starts------------------------------
const slider_imgs = document.querySelectorAll('.slider_img');
const slider_dots = document.querySelectorAll('.slider_dot');
const btn_l = document.querySelector('#btn_l');
const btn_r = document.querySelector('#btn_r');
let i=0;
function next(){
    slider_imgs[i].classList.remove('slider_show');
    slider_dots[i].classList.remove('active_slider_dot');
    if(i<slider_imgs.length-1){i++;}
    else{i=0;}
    slider_dots[i].classList.add('active_slider_dot');
    slider_imgs[i].classList.add('slider_show');
};

btn_r.addEventListener('click', next)
btn_l.addEventListener('click', function(){
    slider_imgs[i].classList.remove('slider_show');
    slider_dots[i].classList.remove('active_slider_dot');
    if(i>0){i--;}
    else{i=slider_imgs.length-1;}
    slider_dots[i].classList.add('active_slider_dot');
    slider_imgs[i].classList.add('slider_show');
});
setInterval(next,5000);
// ------------------slider ends------------------------------

// ------------------bars starts------------------------------
const barsDiv = document.querySelector('.bars-div');
const barsMenu = document.querySelector('.bars-menu');
barsDiv.addEventListener('click' , function(){
    barsMenu.classList.toggle('bars-menu-active');
})
