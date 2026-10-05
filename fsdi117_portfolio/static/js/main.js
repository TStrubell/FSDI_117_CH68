document.addEventListener("scroll", () => {
    const hero = document.querySelector(".hero-parallax");
    if (!hero) return;

    const scrollPosition = window.scrollY;
    hero.style.backgroundPositionY = `${scrollPosition * 0.4}px`;
});
