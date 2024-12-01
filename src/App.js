import './App.css';
import React, {useState, useEffect} from 'react';

function App() {
  const [recipeList, setRecipeList] = useState([]);

  useEffect(() => {
    fetch('/recipes')
    .then(res=>res.json())
    .then(data=>setRecipeList(data));
  }, []);

  return (
    <div className="App">
      <h2>Recipe Table</h2>
      <table className="RecipeTable">
        <tr>
          <th>Test</th>
          <th>Test2</th>
          <th>ingredients</th>
        </tr>
        {recipeList.map(recipe=> (
          <tr key={recipe.id}>
            <td>{recipe.Name}</td> 
            <td>{recipe.Test2}</td>
            <td>{recipe.ingredients}</td>
          </tr>
        ))}
      </table>

    </div>
  );
}

export default App;
