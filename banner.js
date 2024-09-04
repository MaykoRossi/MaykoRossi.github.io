let slideIndex = 0;
const slides = document.querySelectorAll('.slide');

// Função para mostrar os slides
function mostrarSlides(index) {
    const offset = -index * 100;
    document.querySelector('.slides-container').style.transform = `translateX(${offset}%)`;
}

// Função para mudar os slides manualmente
function mudarSlide(n) {
    slideIndex += n;
    if (slideIndex >= slides.length) slideIndex = 0;
    if (slideIndex < 0) slideIndex = slides.length - 1;
    mostrarSlides(slideIndex);
}

// Função para rotacionar automaticamente os slides
function rotacaoAutomatica() {
    slideIndex++;
    if (slideIndex >= slides.length) slideIndex = 0;
    mostrarSlides(slideIndex);
}

// Iniciar a rotatividade automática
setInterval(rotacaoAutomatica, 4000); // 4 segundos

// Mostrar o slide inicial
mostrarSlides(slideIndex);
