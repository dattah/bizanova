function myFunction(x) {
    if (x.matches) { // If media query matches
        // document.body.style.backgroundColor = "yellow";
        $("table").removeClass('table-responsive')
    } else {
        // document.body.style.backgroundColor = "pink";
        $("table").addClass('table-responsive')
    }
}

var x = window.matchMedia("(min-width: 768px)")
myFunction(x) // Call listener function at run time
x.addListener(myFunction) // Attach listener function on state changes