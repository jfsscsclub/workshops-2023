import './App.css'

import React, { useState } from 'react'

export default function App() {
  const increaseValue = () => {
    let newValue = value + 1
    setValue(newValue)
  }

  const decreaseValue = () => {
    let newValue = value - 1
    setValue(newValue)
  }
  console.log('hello')

  const [value, setValue] = useState(0)
  document.title = `You clicked ${value} times`
  return (
    <main>
      <h1>{value}</h1>
      <button onClick={decreaseValue}>Decrease</button>
      <button onClick={increaseValue}>Increase</button>
    </main>
  )
}
