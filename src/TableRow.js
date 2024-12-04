import React, {useState, useEffect} from 'react';


function TableRows(props) {
  const [recipeList, setRecipeList] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [filteredRecipes, setFilteredRecipes] = useState(recipeList);


  useEffect(() => {
    fetch('/recipes')
    .then(res=>res.json())
    .then(data=>setRecipeList(data));
  }, []);

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
    <div>
        
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
  </div>

  )
}

export default TableRows