import './App.css'
import React, { useState } from 'react'

export default function App() {
  const [flag, setFlag] = useState(false)

  const updateValue = () => {
    setFlag(true)
  }

  if (flag === true) {
    document.body.style.backgroundColor = 'black'
    return (
      <main>
        <img src="https://wallpaperaccess.com/full/1505299.jpg" />
      </main>
    )
  }

  return (
    <main>
      <h1>Press Button</h1>
      <button onClick={updateValue}>Plzzzz</button>
    </main>
  )
}
