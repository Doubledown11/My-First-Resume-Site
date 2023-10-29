var timer;

function startScrolling() {
    timer = setInterval(function() {
      var container = document.querySelector('.scrollable-container');
      container.scrollTop += 1;
      if (container.scrollTop >= container.scrollHeight - container.offsetHeight) {
        container.scrollTop = 0;
      }
    }, 20);
  }
  

function stopScrolling() {
  clearInterval(timer);
}
