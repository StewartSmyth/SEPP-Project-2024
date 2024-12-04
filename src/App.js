import './App.css';

import { useState, useEffect} from 'react';

function App() {
  
  const [recipeList, setRecipeList] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [filteredRecipes, setFilteredRecipes] = useState(recipeList);


  useEffect(() => {
    fetch('/recipes')
    .then(res=>res.json())
    .then(data=>setRecipeList(data));
  }, []);

  useEffect(() => {
    setFilteredRecipes(recipeList);
  }, [recipeList]);

  const handleInputChange = (event) => {
    const { value } = event.target
    setSearchTerm(value);
    filterData(value);
  }

  const filterData = (searchTerm) => {
    const filteredData = recipeList.filter((recipe) => 
      recipe.name.toLowerCase().includes(searchTerm.toLowerCase()));
    setFilteredRecipes(filteredData)
  }


  return (
    <div className="App">
      <h2>Recipe Table</h2>
      <input type = "text" placeholder='Search...' value = {searchTerm} onChange={handleInputChange}/>
      <table className="RecipeTable">
        <tr>
          <th>Recipe Name</th>
          <th>Recipe Time</th>
          <th>Ingredients</th>
          <th>Link</th>
        </tr>
        {filteredRecipes.map(recipe => (
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
