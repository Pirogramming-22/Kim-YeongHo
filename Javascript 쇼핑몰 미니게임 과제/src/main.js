//fetch the Items from the JSON file
function loadItems(){
    return fetch('data/data.json')
        .then(response => response.json()) 
        .then(json => json.items);
}

//Update List with the given items
function displayItems(items){
    const container = document.querySelector('.items');
    container.innerHTML = items.map(item => createHTMLstring(item)).join('');
}

//create HTML list items from the given data item
function createHTMLstring(item){
    return `
      <li class="item">
        <img src="${item.image}" alt="${item.type}" class="item__thumbnail">
        <span class="item__description">${item.gender},${item.size}</span>
      </li>
    `;
}



//main
loadItems()
    .then(items => {
        console.log(items);
        displayItems(items);
        // setEventListeners(items);
    })
    .catch(console.log);