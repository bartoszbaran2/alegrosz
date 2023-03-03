import logo from './logo.svg';
import './App.css';
import {useState} from "react";

function App() {
    const [product, setProduct] = useState('');
    const [price, setPrice] = useState('');
    const [decsription, setDescription] = useState('');


    async function addProduct(){

    }

    return (
        <div className="App">
            <input placeholder="Product Name" value={product} onChange={(event) => setProduct(event.target.value)}/>
            <br/>
            <input placeholder="Price" type="number" value={price} onChange={(event) => setPrice(event.target.value)}/>
            <br/>
            <textarea placeholder="Description" value={decsription}
                      onChange={(event) => setDescription(event.target.value)}></textarea>
            <br/>
            <button>Add Product</button>
        </div>
    );
}

export default App;
