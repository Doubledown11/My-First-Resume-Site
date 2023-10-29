// Will change the name of this page to: js-scroll


// Below is the css class object we are trying to move/grow. line2 = scroll element.
const jsScroll = document.getElementById('.js-scroll');

// Offset that determines when the line should be moved, when scrolling down.
const offset_down = 5;

// Offset that determines when the line should be moved, when scrolling up.
const offset_up = 60; // Set to 60px from the top.

// Const value that determines where the user is relative to the document.
var scrollPosition = document.documentElement.clientHeight;

jsScroll.forEach((line2) => {
    line2.style.top = "1000px";
})





const handleScrollAnimation = () => {
    if (elementInView(line2, offset_down)) {
        displayScrollElement();
    } else {
        hideScrollElement();
    }
};



// Add an event listener for the scroll event.
window.addEventListener('scroll', () => {

    if (scrollPosition > offset_down) {
        line2.style.top = "1000px";
    } else {
        line2.style.top = "50px"
    }
});




/* Below is the func that measures the distance the user 
has moved on the page, and determines if is within the range of the line growing function. */

// Start to move the line back to top = 50px, when the user's viewport has reached 60px from the top.
const elementInView = (el, scrollOffset = 0) => {
    const elementTop = el.getBoundingClientRect().top;

    return (
        elementTop <= 
        ((window.innerHeight || document.documentElement.clientHeight) - scrollOffset)
    )
}
// Above function returns true when the \
// element (el) has scrolled by scrollOffset px into the page.

//Applies scrolled to the js-scroll css class.
const displayScrollElement = () => {
    scrollElement.classList.add('scrolled');
}


const hideScrollElement = () => {
    scrollElement.classList.remove('scrolled');
}



// scroll(); // What was this for?