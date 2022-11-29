import { useState } from 'react'
import { useEffect } from 'react'
import Product from "./Product"
import './App.css'

export default function App() {
  const [products, setProducts] = useState([]);
  
  useEffect(() => {
    async function fetchData() {
      // Get data from our endpoint
      const res = await fetch("https://frasercodes.vercel.app/fakeapi/products.json");
      const data = await res.json();

      // Change state
      setProducts(data);
    }

    fetchData();
  }, [] /* THIS IS REALLY IMPORTANT */);

  return (
    <main>
      <h1>My mini-store</h1>

      {products.length !== 0 ? (
        <div className="grid">
          {products.map((product, idx) => <Product data={product} key={idx} />)}
        </div>
      ) : (
        <p>Loading...</p>
      )}
    </main>
  )
}
