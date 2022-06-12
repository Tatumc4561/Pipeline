
const profileOnly = document.querySelectorAll('.profile-only')

for(el of profileOnly){
    el.style = "visibility: hidden;"
}


// top-nav

const searchDropdownButton = document.querySelector('#search-button')
const searchDropdownMenu = document.querySelector('#search-dropdownz')

searchDropdownButton.addEventListener('click', function(){

    searchDropdownMenu.classList.toggle('search-dropdown-wrap')
    console.log('searching bro')
})