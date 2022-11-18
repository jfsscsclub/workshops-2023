// Boilerplate code to ensure we are importing REACT
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'

// GET ELEMENT BY ID - just ensure we can access the HTML Element
ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
