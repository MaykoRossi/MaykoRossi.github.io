// Função para alternar o menu
function toggleMenu() {
    const navList = document.querySelector('.nav-list');
    if (navList) {
        navList.classList.toggle('active');
        console.log('Botão de menu clicado. Classe "active" alternada.');
    } else {
        console.error('Erro: navList não encontrado.');
    }
}
