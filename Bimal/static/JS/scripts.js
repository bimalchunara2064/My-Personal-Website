document.addEventListener("DOMContentLoaded", function () {
    const menuBtn = document.getElementById("menuBtn");
    const navMenu = document.querySelector(".nav-menu");

    if (menuBtn && navMenu) {
        menuBtn.addEventListener("click", function () {
            navMenu.classList.toggle("active");
        });
    }

    /* =========================================
       INDEX JAVASCRIPT
    ========================================= */
    const heroImage = document.querySelector(".hero-image");

    if (heroImage) {
        heroImage.addEventListener("mouseenter", function () {
            const image = heroImage.querySelector("img");
            if (image) {
                image.style.transform = "scale(1.05)";
            }
        });

        heroImage.addEventListener("mouseleave", function () {
            const image = heroImage.querySelector("img");
            if (image) {
                image.style.transform = "scale(1)";
            }
        });
    }

    /* =========================================
       FOOTER JAVASCRIPT
    ========================================= */
    const socialIcons = document.querySelectorAll(".social-icon");

    socialIcons.forEach(function (icon) {
        icon.addEventListener("click", function () {
            this.classList.add("social-clicked");

            setTimeout(() => {
                this.classList.remove("social-clicked");
            }, 300);
        });
    });

    /* =========================================
       ABOUT JAVASCRIPT
    ========================================= */
    const skillBars = document.querySelectorAll(".skill-progress");

    const animateSkills = () => {
        skillBars.forEach(function (bar) {
            const width = bar.getAttribute("data-width");
            if (width) {
                bar.style.width = width;
            }
        });
    };

    const imageBox = document.querySelector(".about-image-box");

    if (imageBox) {
        imageBox.addEventListener("mouseenter", function () {
            imageBox.classList.add("image-hovered");
        });

        imageBox.addEventListener("mouseleave", function () {
            imageBox.classList.remove("image-hovered");
        });
    }

    if ("IntersectionObserver" in window) {
        const observer = new IntersectionObserver(function (entries, observerInstance) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    animateSkills();
                    observerInstance.disconnect();
                }
            });
        }, {
            threshold: 0.2
        });

        const skillsSection = document.querySelector(".skills-container");

        if (skillsSection) {
            observer.observe(skillsSection);
        }
    } else {
        animateSkills();
    }

    /* =========================================
       SERVICES JAVASCRIPT
    ========================================= */
    const serviceCards = document.querySelectorAll(".service-card");

    if ("IntersectionObserver" in window && serviceCards.length) {
        const cardObserver = new IntersectionObserver(function (entries, observerInstance) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add("show");
                    observerInstance.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.15
        });

        serviceCards.forEach(function (card) {
            card.classList.add("service-hidden");
            cardObserver.observe(card);
        });
    }

    const processItems = document.querySelectorAll(".process-item");

    if ("IntersectionObserver" in window && processItems.length) {
        const processObserver = new IntersectionObserver(function (entries, observerInstance) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add("process-show");
                    observerInstance.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.15
        });

        processItems.forEach(function (item) {
            item.classList.add("process-hidden");
            processObserver.observe(item);
        });
    }

    /* =========================================
       CONTACT JAVASCRIPT
    ========================================= */
    const form = document.getElementById("contactForm");

    if (form) {
        const firstName = document.getElementById("firstName");
        const lastName = document.getElementById("lastName");
        const email = document.getElementById("email");
        const phone = document.getElementById("phone");
        const message = document.getElementById("message");
        const submitBtn = document.getElementById("submitBtn");

        const firstNameError = document.getElementById("firstNameError");
        const lastNameError = document.getElementById("lastNameError");
        const emailError = document.getElementById("emailError");
        const phoneError = document.getElementById("phoneError");
        const messageError = document.getElementById("messageError");

        function showError(input, errorElement, messageText) {
            input.classList.add("input-error");
            input.classList.remove("input-success");
            errorElement.textContent = messageText;
            errorElement.classList.add("show");
        }

        function clearError(input, errorElement) {
            input.classList.remove("input-error");

            if (input.value.trim() !== "") {
                input.classList.add("input-success");
            }

            errorElement.textContent = "";
            errorElement.classList.remove("show");
        }

        form.addEventListener("submit", function (event) {
            let valid = true;

            if (firstName && firstName.value.trim().length < 2) {
                showError(firstName, firstNameError, "Please enter your first name.");
                valid = false;
            } else if (firstName) {
                clearError(firstName, firstNameError);
            }

            if (lastName && lastName.value.trim().length < 2) {
                showError(lastName, lastNameError, "Please enter your last name.");
                valid = false;
            } else if (lastName) {
                clearError(lastName, lastNameError);
            }

            const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (email && !emailPattern.test(email.value.trim())) {
                showError(email, emailError, "Please enter a valid email address.");
                valid = false;
            } else if (email) {
                clearError(email, emailError);
            }

            const phonePattern = /^[0-9+\-\s()]{7,20}$/;
            if (phone && !phonePattern.test(phone.value.trim())) {
                showError(phone, phoneError, "Please enter a valid phone number.");
                valid = false;
            } else if (phone) {
                clearError(phone, phoneError);
            }

            if (message && message.value.trim().length < 10) {
                showError(message, messageError, "Message must contain at least 10 characters.");
                valid = false;
            } else if (message) {
                clearError(message, messageError);
            }

            if (!valid) {
                event.preventDefault();
                return;
            }

            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.textContent = "Sending...";
            }
        });

        if (firstName) {
            firstName.addEventListener("input", function () {
                if (this.value.trim().length >= 2) {
                    clearError(this, firstNameError);
                }
            });
        }

        if (lastName) {
            lastName.addEventListener("input", function () {
                if (this.value.trim().length >= 2) {
                    clearError(this, lastNameError);
                }
            });
        }

        if (email) {
            email.addEventListener("input", function () {
                const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                if (emailPattern.test(this.value.trim())) {
                    clearError(this, emailError);
                }
            });
        }

        if (phone) {
            phone.addEventListener("input", function () {
                const phonePattern = /^[0-9+\-\s()]{7,20}$/;
                if (phonePattern.test(this.value.trim())) {
                    clearError(this, phoneError);
                }
            });
        }

        if (message) {
            message.addEventListener("input", function () {
                if (this.value.trim().length >= 10) {
                    clearError(this, messageError);
                }
            });
        }
    }

    /* =========================================
       JOURNEY SLIDER
    ========================================= */
    const slider = document.getElementById("journeySlider");
    const cards = document.querySelectorAll(".journey-card");

    if (slider && cards.length) {
        const nextBtn = document.getElementById("journeyNext");
        const prevBtn = document.getElementById("journeyPrev");
        const currentText = document.getElementById("journeyCurrent");
        const progress = document.getElementById("journeyProgress");

        let currentIndex = 0;

        function getCardWidth() {
            const card = cards[0];
            const style = window.getComputedStyle(slider);
            const gap = parseFloat(style.columnGap) || 25;
            return card.offsetWidth + gap;
        }

        function updateUI() {
            if (currentText) {
                currentText.textContent = String(currentIndex + 1).padStart(2, "0");
            }

            if (progress) {
                const percentage = ((currentIndex + 1) / cards.length) * 100;
                progress.style.width = percentage + "%";
            }
        }

        function goToSlide(index) {
            if (index < 0) {
                index = cards.length - 1;
            }

            if (index >= cards.length) {
                index = 0;
            }

            currentIndex = index;
            slider.scrollTo({
                left: currentIndex * getCardWidth(),
                behavior: "smooth"
            });
            updateUI();
        }

        if (nextBtn) {
            nextBtn.addEventListener("click", function () {
                goToSlide(currentIndex + 1);
            });
        }

        if (prevBtn) {
            prevBtn.addEventListener("click", function () {
                goToSlide(currentIndex - 1);
            });
        }

        document.addEventListener("keydown", function (event) {
            if (event.key === "ArrowRight") {
                goToSlide(currentIndex + 1);
            }

            if (event.key === "ArrowLeft") {
                goToSlide(currentIndex - 1);
            }
        });

        let isDragging = false;
        let startX = 0;
        let startScroll = 0;

        slider.addEventListener("mousedown", function (event) {
            isDragging = true;
            startX = event.pageX;
            startScroll = slider.scrollLeft;
            slider.style.cursor = "grabbing";
        });

        slider.addEventListener("mousemove", function (event) {
            if (!isDragging) return;

            const distance = event.pageX - startX;
            slider.scrollLeft = startScroll - distance;
        });

        slider.addEventListener("mouseup", function () {
            isDragging = false;
            slider.style.cursor = "grab";
        });

        slider.addEventListener("mouseleave", function () {
            isDragging = false;
            slider.style.cursor = "grab";
        });

        let touchStart = 0;

        slider.addEventListener("touchstart", function (event) {
            touchStart = event.touches[0].clientX;
        });

        slider.addEventListener("touchend", function (event) {
            const touchEnd = event.changedTouches[0].clientX;
            const difference = touchStart - touchEnd;

            if (Math.abs(difference) > 50) {
                if (difference > 0) {
                    goToSlide(currentIndex + 1);
                } else {
                    goToSlide(currentIndex - 1);
                }
            }
        });

        updateUI();
    }
});

/* photo page javascript */
const photos = [

    {
        image: "images/photo1.jpg",
        title: "School Event"
    },

    {
        image: "images/photo2.jpg",
        title: "Web Development"
    },

    {
        image: "images/photo3.jpg",
        title: "School Memory"
    },

    {
        image: "images/photo4.jpg",
        title: "Personal Photo"
    },

    {
        image: "images/photo5.jpg",
        title: "Special Event"
    },

    {
        image: "images/photo6.jpg",
        title: "Coding Project"
    }

];


let currentIndex = 0;


/* OPEN PHOTO */

function openPhoto(index) {

    currentIndex = index;

    updatePhoto();

    document
        .getElementById("lightbox")
        .classList.add("show");

    document.body.style.overflow = "hidden";
}


/* CLOSE */

function closePhoto() {

    document
        .getElementById("lightbox")
        .classList.remove("show");

    document.body.style.overflow = "auto";
}


/* UPDATE */

function updatePhoto() {

    document.getElementById(
        "lightboxImage"
    ).src = photos[currentIndex].image;


    document.getElementById(
        "lightboxTitle"
    ).textContent = photos[currentIndex].title;


    document.getElementById(
        "downloadPhoto"
    ).href = photos[currentIndex].image;
}


/* NEXT */

function nextPhoto() {

    currentIndex++;

    if (currentIndex >= photos.length) {
        currentIndex = 0;
    }

    updatePhoto();
}


/* PREVIOUS */

function previousPhoto() {

    currentIndex--;

    if (currentIndex < 0) {
        currentIndex = photos.length - 1;
    }

    updatePhoto();
}


/* KEYBOARD */

document.addEventListener(
    "keydown",
    function(event) {

        if (event.key === "Escape") {
            closePhoto();
        }

        if (event.key === "ArrowRight") {
            nextPhoto();
        }

        if (event.key === "ArrowLeft") {
            previousPhoto();
        }

    }
);


/* FILTER */

const filters =
    document.querySelectorAll(".filter");

const cards =
    document.querySelectorAll(".photo-card");


filters.forEach(function(filter) {

    filter.addEventListener(
        "click",
        function() {

            filters.forEach(function(btn) {
                btn.classList.remove("active");
            });

            this.classList.add("active");

            const category =
                this.getAttribute("data-filter");


            cards.forEach(function(card) {

                if (
                    category === "all" ||
                    card.dataset.category === category
                ) {

                    card.style.display = "block";

                } else {

                    card.style.display = "none";

                }

            });

        }
    );

});


/* SEARCH */

document
    .getElementById("search")
    .addEventListener(
        "input",
        function() {

            const value =
                this.value.toLowerCase();


            cards.forEach(function(card) {

                const title =
                    card.dataset.title.toLowerCase();

                if (title.includes(value)) {

                    card.style.display = "block";

                } else {

                    card.style.display = "none";

                }

            });

        }
    );



/* service training section */
document.addEventListener("DOMContentLoaded", function () {

    /* ===============================
       PAYMENT QR TAB SYSTEM
    =============================== */

    const paymentTabs = document.querySelectorAll(".payment-tab");
    const paymentPanels = document.querySelectorAll(".payment-panel");

    paymentTabs.forEach(function (tab) {

        tab.addEventListener("click", function () {

            // Remove active from all buttons
            paymentTabs.forEach(function (item) {
                item.classList.remove("active");
            });

            // Hide all QR panels
            paymentPanels.forEach(function (panel) {
                panel.classList.add("hidden");
            });

            // Active selected button
            tab.classList.add("active");

            // Show selected payment panel
            const targetId = tab.getAttribute("data-target");
            const targetPanel = document.getElementById(targetId);

            if (targetPanel) {
                targetPanel.classList.remove("hidden");
            }

        });

    });



    /* ===============================
       SMOOTH SCROLL
    =============================== */

    const scrollLinks = document.querySelectorAll(
        'a[href^="#"]'
    );

    scrollLinks.forEach(function (link) {

        link.addEventListener("click", function (event) {

            const targetId = link.getAttribute("href");

            if (targetId === "#") {
                return;
            }

            const target = document.querySelector(targetId);

            if (target) {

                event.preventDefault();

                target.scrollIntoView({
                    behavior: "smooth",
                    block: "start"
                });

            }

        });

    });



    /* ===============================
       COURSE CARD ANIMATION
    =============================== */

    const courseCards =
        document.querySelectorAll(".course-item");

    courseCards.forEach(function (card) {

        card.addEventListener("mouseenter", function () {

            card.style.transform =
                "translateY(-6px)";

        });

        card.addEventListener("mouseleave", function () {

            card.style.transform =
                "translateY(0)";

        });

    });



    /* ===============================
       ONLINE STATUS ANIMATION
    =============================== */

    const onlineDot =
        document.querySelector(".online-dot");

    if (onlineDot) {

        setInterval(function () {

            onlineDot.classList.toggle(
                "online-pulse"
            );

        }, 1000);

    }



    /* ===============================
       ENROLL BUTTON LOADING
    =============================== */

    const enrollButtons =
        document.querySelectorAll(".course-enroll");

    enrollButtons.forEach(function (button) {

        button.addEventListener("click", function () {

            button.style.opacity = "0.7";

            button.innerHTML =
                "Opening Enrollment...";

        });

    });



    /* ===============================
       PAYMENT SCREENSHOT PREVIEW
    =============================== */

    const screenshotInput =
        document.querySelector(
            'input[type="file"]'
        );

    if (screenshotInput) {

        screenshotInput.addEventListener(
            "change",
            function () {

                const file =
                    screenshotInput.files[0];

                if (!file) {
                    return;
                }

                if (!file.type.startsWith("image/")) {

                    alert(
                        "Please upload a valid payment screenshot image."
                    );

                    screenshotInput.value = "";

                    return;
                }

                if (file.size > 5 * 1024 * 1024) {

                    alert(
                        "Image size must be less than 5 MB."
                    );

                    screenshotInput.value = "";

                    return;
                }

            }
        );

    }



    /* ===============================
       FORM SUBMIT PROTECTION
    =============================== */

    const enrollmentForm =
        document.querySelector(".enroll-form");

    if (enrollmentForm) {

        enrollmentForm.addEventListener(
            "submit",
            function () {

                const submitButton =
                    enrollmentForm.querySelector(
                        ".submit-btn"
                    );

                if (submitButton) {

                    submitButton.disabled = true;

                    submitButton.innerHTML =
                        "Submitting...";

                }

            }
        );

    }



    /* ===============================
       SCROLL REVEAL
    =============================== */

    const revealElements =
        document.querySelectorAll(
            ".course-item, .feature, .visual-card"
        );

    const observer =
        new IntersectionObserver(
            function (entries) {

                entries.forEach(function (entry) {

                    if (entry.isIntersecting) {

                        entry.target.classList.add(
                            "show-element"
                        );

                        observer.unobserve(
                            entry.target
                        );

                    }

                });

            },
            {
                threshold: 0.15
            }
        );


    revealElements.forEach(function (element) {

        element.classList.add(
            "hidden-element"
        );

        observer.observe(element);

    });

});


