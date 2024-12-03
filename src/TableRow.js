import React, {useState, useEffect} from 'react';
import { getRecipes } from './recipeService';


function TableRows(props) {
  const [recipeList, setRecipeList] = useState([]);

  useEffect(() => {
    fetch('/recipes')
    .then(res=>res.json())
    .then(data=>setRecipeList(data));
  }, []);

  return (
        recipeList.map(recipe=> (
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
        ))
  )
}

export default TableRows