import logo from './logo.svg';
import './App.css';

function MyButton(){
  return (
    <button className="my-button">Buy a home</button>
  );
}



function App() {
  return (
    <>
      <div className="App-header">
        <h1>Lloyds Mortgage Calculator</h1>
        <div className="myButton"><MyButton /></div>
      </div>
    </>
  );
}

export default App;
