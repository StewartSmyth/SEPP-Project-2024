import './App.css';
import TableRows from './TableRow';
import SearchBar from './SearchBar';

function App() {
  


  return (
    <div className="App">
      <h2>Recipe Table</h2>
      <SearchBar/>
      <table className="RecipeTable">
        <tr>
          <th>Recipe Name</th>
          <th>Recipe Time</th>
          <th>Ingredients</th>
          <th>Link</th>
        </tr>
        <TableRows searchTerm='SearchTerm'/>
      </table>

    </div>
  );
}

export default App;
