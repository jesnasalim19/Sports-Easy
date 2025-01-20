// Wait for the DOMContentLoaded event to ensure the DOM is fully loaded before executing the script
document.addEventListener("DOMContentLoaded", function() {
    // Initialize Owl Carousel
    var customCarousel = document.querySelector(".custom-carousel");
    if (customCarousel) {
        owlCarousel(customCarousel, {
            autoWidth: true,
            loop: true
        });

        // Adding click event listener to carousel items
        var carouselItems = document.querySelectorAll(".custom-carousel .item");
        carouselItems.forEach(function(item) {
            item.addEventListener("click", function() {
                // Removing 'active' class from all items except the clicked one
                carouselItems.forEach(function(item) {
                    if (!item.classList.contains("active")) {
                        item.classList.remove("active");
                    }
                });
                // Toggling 'active' class on the clicked item
                this.classList.toggle("active");
            });
        });
    }
});

// Owl Carousel function (simulation)
function owlCarousel(element, options) {
    // Simulated owlCarousel function for demonstration purposes
    console.log("Owl Carousel initialized on element:", element);
    console.log("Options:", options);
}   