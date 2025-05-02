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

const criarGrafico = (ctxId, dados) => {
    const categorias = Object.keys(dados);
    const valores = Object.values(dados);

    new Chart(document.getElementById(ctxId), {
        type: 'pie',
        data: {
            labels: categorias,
            datasets: [{
                data: valores,
                backgroundColor: [
                    '#4caf50',
                    '#2196f3',
                    '#f44336',
                    '#ff9800',
                    '#9c27b0',
                    '#00bcd4',
                    '#8bc34a'
                ]
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'bottom',
                }
            }
        }
    });
};

if (receitas && Object.keys(receitas).length > 0) {
    criarGrafico('graficoReceitas', receitas);
}
if (despesas && Object.keys(despesas).length > 0) {
    criarGrafico('graficoDespesas', despesas);
}