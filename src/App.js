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
          <th>Recipe Name</th>
          <th>Recipe Time</th>
          <th>Ingredients</th>
          <th>Link</th>
        </tr>
        {recipeList.map(recipe=> (
          <tr key={recipe.id}>
            <td>{recipe.name}</td> 
            <td>{recipe.time}</td>
            <td>
            <ul>
            {recipe.ingredients.map((ingredient) => (
              <li>{ingredient}</li>
            ))}
            </ul>
            </td>
            <td><a href={recipe.link}>{recipe.link}</a></td>
          </tr>
        ))}
      </table>

    </div>
  );
}

export default App;
