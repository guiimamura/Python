// 1. Definição dos três valores de entrada (Exemplo do teste)
let a = 3;
let b = 1;
let c = 2;

// Variáveis para guardar a ordem correta
let menor, meio, maior;

// 2. Lógica de comparação usando estruturas condicionais
if (a <= b && a <= c) {
    menor = a;
    if (b <= c) {
        meio = b;
        maior = c;
    } else {
        meio = c;
        maior = b;
    }
} else if (b <= a && b <= c) {
    menor = b;
    if (a <= c) {
        meio = a;
        maior = c;
    } else {
        meio = c;
        maior = a;
    }
} else {
    menor = c;
    if (a <= b) {
        meio = a;
        maior = b;
    } else {
        meio = b;
        maior = a;
    }
}

// 3. Exibição do resultado conforme o exemplo do enunciado
console.log(`Valores: ${a}, ${b}, ${c}`);
console.log(`Ordem crescente: ${menor}, ${meio}, ${maior}`);

