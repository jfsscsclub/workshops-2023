import { useState, useEffect } from "react"
import "./App.css"

const colors = ["aliceblue", "antiquewhite", "aqua", "aquamarine", "azure", "beige", "bisque", "blanchedalmond", "blue", "blueviolet", "brown"]

export default function App() {
  const [bgColor, setBgColor] = useState(colors[0]);
  const [borderColor, setBorderColor] = useState(colors[2]);

  // Use effect for updating background color
  useEffect(() => {
    console.log("Background color:", bgColor);
    document.body.style.backgroundColor = bgColor;
  }, [bgColor]);

  // useEffect for updating border color
  useEffect(() => {
    console.log("Border color:", borderColor);
    document.body.style.borderColor = borderColor;
  }, [borderColor]);

  // Handling when we have to update the background color
  const handleBGColorClick = () => {
    const newIdx = Math.floor(Math.random() * colors.length);
    const newColor = colors[newIdx];

    setBgColor(newColor);
  };

  // Handling when we have to update the border color
  const handleBorderColorClick = () => {
    const newIdx = Math.floor(Math.random() * colors.length);
    const newColor = colors[newIdx];

    setBorderColor(newColor);
  };

  return (
    <main>
      <h1>Current background color: {bgColor}</h1>
      <h1>Current border color: {borderColor}</h1>
      
      <button onClick={handleBGColorClick}>
        Change Background Color
      </button>
      
      <button onClick={handleBorderColorClick}>
        Change Border Color
      </button>
    </main>
  )
}