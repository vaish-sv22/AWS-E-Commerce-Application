//const API_URL = "http://172.31.37.47:5000/products";
const API_URL = "/api/products";
async function loadProducts() {

    try {

        const response = await fetch(API_URL);

        const products = await response.json();

        const container = document.getElementById("products");

        container.innerHTML = "";

        products.forEach(product => {

            container.innerHTML += `

            <div class="card">

                <img src="${product.image}">

                <h3>${product.name}</h3>

                <p>${product.description}</p>

                <p class="price">₹${product.price}</p>

                <button onclick="buyProduct('${product.name}')">
                    Buy Now
                </button>

            </div>

            `;

        });

    }

    catch(err){

        document.getElementById("products").innerHTML =
        "<h2>Unable to connect to backend API.</h2>";

        console.log(err);

    }

}

function buyProduct(name){

    alert(name + " added to cart!");

}

loadProducts();
