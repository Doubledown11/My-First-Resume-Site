// Function used to expand the div container on the home page to fit my entire screen.




function expandcontainer(Id) {
    var myDiv = document.getElementById(Id);
    myDiv.style.position = "fixed";
    myDiv.style.top = "0";
    myDiv.style.left = "0";
    myDiv.style.width = "100%";
    myDiv.style.height = "100%";
    myDiv.style.backgroundColor = "black";
    myDiv.style.color = "white";
    myDiv.innerHTML = "Expanded!";
}