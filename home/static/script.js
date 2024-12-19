let currentIndex = 0;
const slides = document.querySelectorAll('.slides');
const totalSlides = slides.length;

function showSlide(index) {
    slides.forEach((slide, i) => {
        slide.style.opacity = i === index ? '1' : '0';
    });
}

function nextSlide() {
    currentIndex = (currentIndex + 1) % totalSlides;
    showSlide(currentIndex);
}

setInterval(nextSlide, 3000); 


showSlide(currentIndex);



let currentSlideIndex = 0;
const slideElements = document.querySelectorAll('.slides2');
const totalSlidesCount = slideElements.length;

function displaySlide(index) {
    slideElements.forEach((slide, i) => {
        slide.style.opacity = i === index ? '1' : '0';
    });
}

function advanceSlide() {
    currentSlideIndex = (currentSlideIndex + 1) % totalSlidesCount;
    displaySlide(currentSlideIndex);
}

setInterval(advanceSlide, 3000); // Change image every 3 seconds

// Initial display
displaySlide(currentSlideIndex);




// ---------------------------------------------------------------------------------------------------------------


var password = document.getElementById("password"),
    confirm_password = document.getElementById("confirm_password");

function validatePassword() {
    if (password.value != confirm_password.value) {
        confirm_password.setCustomValidity("Passwords don't match");
    } else {
        confirm_password.setCustomValidity('');
    }
}

password.onchange = validatePassword;
confirm_password.onkeyup = validatePassword;



