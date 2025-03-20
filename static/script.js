document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');

    form.addEventListener('submit', (e) => {
        const valor = parseFloat(form.valor.value);
        const descricao = form.descricao.value.trim();

        if (valor <= 0) {
            alert('O valor deve ser maior que zero!');
            e.preventDefault();
        }

        if (descricao.length < 2) {
            alert('A descrição deve ter pelo menos 2 caracteres!');
            e.preventDefault();
        }
    });
});