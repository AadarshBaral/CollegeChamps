
// modal windows

'use strict';

// window.fbAsyncInit = function() {
//   FB.init({
//     appId            : 'your-app-id',
//     autoLogAppEvents : true,
//     xfbml            : true,
//     version          : 'v11.0'
//   });
// };

// // social share
// var title = $( ".blog-title" ).first().text();
// var pageURL = $(location).attr("href");
// $("#share").jsSocials({
  
//   url: pageURL,
//   text: title,
//   showLabel: true,
//   shares: [
//    {share  : "twitter" ,label : 'Share',showCount: true,} ,
//     { share: "facebook", label : 'Share' ,showCount: true} ]
// });

//for all queryselectors.
// const modal = document.querySelector('.modal')

// const overlay = document.querySelector('.overlay')
// const btnCloseModal= document.querySelector('.close-modal')
// const btnsOpenModal = document.querySelectorAll('.show-modal')


// // function to remove the modal
// const openModal = function(){
//     modal.classList.remove('off')
//     overlay.classList.remove('off')
  
    
// }
// const closeModal = function(){
//   modal.classList.add('off')
//   overlay.classList.add('off')

// }
// // for elements having same classes
// //if we had same elements but with different classes or id's we would not have done this. Instead we would have just targeted the single class and add a eventlistener.
// for (let i = 0; i < btnsOpenModal.length; i++){
//   btnsOpenModal[i].addEventListener('click',openModal)

// }
// btnCloseModal.addEventListener('click', closeModal);
// overlay.addEventListener('click',closeModal)


// //keypress events

// document.addEventListener('keydown',function(e){
//     if(e.key === 'Escape' && !modal.classList.contains('hidden')){
    
//         closeModal();
      
//     }
// })





























const toggleButton = document.getElementsByClassName("toggle-btn")[0];
const toggleButton1 = document.getElementsByClassName("toggle-btn1")[0];

const navbarLinks = document.getElementsByClassName("nav-links")[0];

toggleButton.addEventListener("click", () => {
 
  navbarLinks.classList.toggle("active");
  toggleButton.classList.toggle("hide");
  toggleButton1.classList.toggle("act");
});
toggleButton1.addEventListener("click", () => {
  console.log("click");
  navbarLinks.classList.toggle("active");
  toggleButton1.classList.toggle("act");
  toggleButton.classList.toggle("hide");
});




const slider = document.querySelector('.gallery');
let isDown = false;
let startX;
let scrollLeft;

slider.addEventListener('mousedown', e => {
  isDown = true;
  slider.classList.add('active');
  startX = e.pageX - slider.offsetLeft;
  scrollLeft = slider.scrollLeft;
});
slider.addEventListener('mouseleave', _ => {
  isDown = false;
  slider.classList.remove('active');
});
slider.addEventListener('mouseup', _ => {
  isDown = false;
  slider.classList.remove('active');
});
slider.addEventListener('mousemove', e => {
  if (!isDown) return;
  e.preventDefault();
  const x = e.pageX - slider.offsetLeft;
  const SCROLL_SPEED = 3;
  const walk = (x - startX) * SCROLL_SPEED;
  slider.scrollLeft = scrollLeft - walk;
});



// Social share
