import logo from './logo.svg';
import './App.css';
import {useEffect, useState} from "react";

function App() {
    const [product, setProduct] = useState('');
    const [price, setPrice] = useState('');
    const [description, setDescription] = useState('');
    const [products, setProducts] = useState([])


    useEffect(() => {
        fetch('/api/v1/products/')
            .then((response) => response.json())
            .then((data) => setProducts(data))
    }, [])

    async function addProduct() {
        const response = await fetch('/api/v1/products/', {
            body: JSON.stringify({name: product, price, description}),
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        const data = await response.json()
        setProducts([...products, data])

    }

    function deleteProduct(id) {
        return async function () {
            const response2 = await fetch(`/api/v1/products/${id}/`, {
                method: 'DELETE'
            })

            console.log(products)
            setProducts(products.filter((product) => product.id !== id))
        }
    }

    return (
        <div className="App">
            <input placeholder="Product Name" value={product} onChange={(event) => setProduct(event.target.value)}/>
            <br/>
            <input placeholder="Price" type="number" value={price} onChange={(event) => setPrice(event.target.value)}/>
            <br/>
            <textarea placeholder="Description" value={description}
                      onChange={(event) => setDescription(event.target.value)}></textarea>
            <br/>
            <button onClick={addProduct}>Add Product</button>
            <div>
                {products.map((product) => (
                    <div key={product.id}>
                        <h2> {product.name} </h2>
                        <p> {product.description}</p>
                        <p> Price: {product.price}</p>
                        <button> Edit</button>
                        <button onClick={deleteProduct(product.id)}> Delete</button>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default App;
