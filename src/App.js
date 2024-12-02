import './App.css';
import TableRows from './TableRow';

function App() {
  


  return (
    <div className="App">
      <h2>Recipe Table</h2>
      <table className="RecipeTable">
        <tr>
          <th>Recipe Name</th>
          <th>Recipe Time</th>
          <th>Ingredients</th>
          <th>Link</th>
        </tr>
        <TableRows/>
      </table>

    </div>
  );
}

export default App;
