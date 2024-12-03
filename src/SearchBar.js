import React, {useState} from 'react'

function SearchBar(props) {
  const [search, setSearch] = useState('');

  const handleInputChange = (e) => {
    const searchTerm = e.target.value;
    setSearch(searchTerm);
  } 
  
  return (
    <input type='text' value={search} onChange={handleInputChange} placeholder='Type to search...'/>
  )
}

export default SearchBar