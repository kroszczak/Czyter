import {useState, useEffect} from 'react'
import './App.css';

function App() {

  const [initialData, setInitial] = useState([{}])

  useEffect(() => {
    fetch('/api').then(res => res.json()
    ).then(res => setInitial(res))
  }, [])
  
  return (
    <div className="App">

      <h1>{initialData.title}</h1>
      <h1>{initialData.state}</h1>
    </div>
  );
}

export default App;