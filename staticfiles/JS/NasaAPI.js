// import API_key from './api.js';
import publicAPI_key from './publicapinasa.js';


const random100 = Math.floor(Math.random() * ( 1 + 99 - 1 ) ) + 1

fetch(`https://images-api.nasa.gov/search?q=space&media_type=image`)
.then(function(response){
    return response.json()
})
.then(function(data){
    
    // ----------------title
    console.log(data.collection.items[random100].data[0].title)

    // ----------------description
    console.log(data.collection.items[random100].data[0].description)

    // ----------------image link
    console.log(data.collection.items[random100].links[0].href)
})

