const products = [
    { id: 1, name: 'Produto 1', price: 10.00 },
    { id: 2, name: 'Produto 2', price: 15.00 },
];

const cart = [];

function displayProducts() {
    const productList = document.getElementById('product-list');
    productList.innerHTML = '';

    products.forEach(product => {
        const productDiv = document.createElement('div');
        productDiv.innerHTML = `
            <p>${product.name} - R$ ${product.price.toFixed(2)}</p>
            <input type="number" id="quantity-${product.id}" placeholder="Quantidade">
            <button onclick="addToCart(${product.id})">Adicionar ao Carrinho</button>
        `;
        productList.appendChild(productDiv);
    });
}

// Função para adicionar um produto ao carrinho
function addToCart(productId) {
    const quantityInput = document.getElementById(`quantity-${productId}`);
    const quantity = parseInt(quantityInput.value);

    if (quantity > 0) {
        const product = products.find(p => p.id === productId);
        const cartItem = { id: productId, quantity, price: product.price };
        cart.push(cartItem);
        quantityInput.value = '';
        updateCart();
    }
}

// Função para atualizar a exibição do carrinho
function updateCart() {
    const cartDiv = document.getElementById('cart');
    cartDiv.innerHTML = '<h2>Carrinho de Compras</h2>';

    let total = 0;
    cart.forEach(item => {
        const itemTotal = item.quantity * item.price;
        total += itemTotal;

        const itemDiv = document.createElement('div');
        itemDiv.innerHTML = `
            <p>${products.find(p => p.id === item.id).name} - Quantidade: ${item.quantity} - Total: R$ ${itemTotal.toFixed(2)}
            <button onclick="removeFromCart(${item.id})">Excluir</button></p>
        `;
        cartDiv.appendChild(itemDiv);
    });

    const cartTotalSpan = document.createElement('span');
    cartTotalSpan.textContent = `R$ ${total.toFixed(2)}`;
    document.getElementById('cart-total').textContent = '';
    document.getElementById('cart-total').appendChild(cartTotalSpan);
}

// Função para remover um item do carrinho
function removeFromCart(productId) {
    const index = cart.findIndex(item => item.id === productId);
    if (index !== -1) {
        cart.splice(index, 1);
        updateCart();
    }
}

// Inicialize a lista de produtos e o carrinho
displayProducts();
updateCart();