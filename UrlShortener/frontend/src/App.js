import logo from './logo.svg';
import './App.css';
import {useEffect,useState} from 'React'

function App() {
  const[urls,setUrl] = useState([])
  const[hasError, setErrors] = useState(false)

  useEffect (() => {
    setUrl([
      {
        "Url": "Url Name",
        "Short-url": "Short Url",
        "Clicks": "Clicks",
        "Created at": "Date"
      }
    ])
},[])
urls.map((Url,index)=>{
  return (
    <div className="App">
      <header className="App-header">
        <h2>Django-React Url Shortner</h2>
        </header>
        <div className="Url-list">
        <div className="Url-name">
          <h2>Url </h2>
          <h2>Url Shortner</h2>
          <h2>Clicks</h2>
          <h2>Created at:</h2>
        </div>
        </div>
      
    </div>
  })
)}

export default App;
