const data = fetch('https://swapi-api.hbtn.io/api/people/5/?format=json');
const chara = document.getElementById('character');
data.then(response => response.json())
data.then(data => {
  const charName = data.name;
  chara.textContent = charName;  
})


