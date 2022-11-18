// importing react and other files
import './App.css'
import Data from './data'
import List from './List'

// Arrow Function Syntax
const App = () => {
  return (
    <main>
      <section className="container">
        <h2>{Data.length} Birthdays Today</h2>
        <List data={Data} />
        <button>Clear All</button>
      </section>
    </main>
  )
}

export default App
