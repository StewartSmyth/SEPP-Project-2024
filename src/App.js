import './App.css';
import React, {useState, useEffect} from 'react';

function App() {
  const [helloWorldText, setHelloWorld] = useState(0);

  useEffect(() => {
    fetch('/hello').then(res=>res.json()).then(data=>{
      setHelloWorld(data.Test);
    });

  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <p>HelloWorldText: {helloWorldText}</p>
      </header>
    </div>
  );
}

export default App;
