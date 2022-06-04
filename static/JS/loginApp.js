const profileOnly = document.querySelectorAll('.profile-only')

// load profile only content on page load
for(el of profileOnly){
    el.style = "visibility: visible;"
}
console.log('hello')



// top-nav

const profileDropdownButton = document.querySelector('#profile-btn-top')
const profileDropdownMenu = document.querySelector('#profile-dropdown')

profileDropdownButton.addEventListener('click', function(){
    
    profileDropdownMenu.classList.toggle('profile-dropdown-wrap')
    console.log('profiledropdown')
})


// groups
const chooseGroup = document.querySelector('#group-choice')
const chooseGroupDropdown = document.querySelector('.hidden-content')
const groupSelection = document.querySelectorAll('.group-radios')
const headerDropdownImg = document.querySelector('#group-popup-img')
const headerDropdownName = document.querySelector('#dropdown-group-text')
const sidebarIMG = document.querySelector('#sidebar-groupimg')
const sidebarText = document.querySelector('#sidebar-grouptext')


chooseGroup.addEventListener('click', function(){
    chooseGroupDropdown.classList.toggle('dropdown-wrap')
    
})            




for(each of groupSelection){
    each.addEventListener('click', function(e){
        
        // img url
        groupIMG = e.target.nextSibling.nextSibling.childNodes[1].src
        
        // text info
        groupName = e.target.nextSibling.nextSibling.htmlFor

        console.log(groupName)
        chooseGroupDropdown.classList.toggle('dropdown-wrap')

        // groupID = e.target.value -1
        // headerDropdownImg.setAttribute('src', '{{groups.'+`${groupID}`+'.avatar.url}}')
        headerDropdownImg.setAttribute('src', groupIMG)
        headerDropdownName.innerHTML = `p/${groupName}`
        sidebarIMG.setAttribute('src', groupIMG)
        sidebarText.innerHTML = `p/${groupName}`


        // AJAX
        // let xhttp = new XMLHttpRequest()
        // xhttp.onreadystatechange = function() {
        //     if (this.readyState == 4 && this.status == 200){
        //     }
        // }
        // console.log(headerDropdownImg)
        // xhttp.open('GET', 'create_thread', true);
        // xhttp.send()

    })            
} 

// subicons
const reportFlag = document.querySelectorAll('.report-flag')

// thread options
const replyButton = document.querySelectorAll('.reply-button')
const replyComment = document.querySelectorAll('.comment-reply-dropdown')

// set on page-load id attributes for dropdown reply boxes
num=0
for(each of replyComment){
    each.setAttribute('id', 'reply-dropdown_#'+num)
    num += 1
}        



// set on page-load id attributes for reply buttons, add event
let i = 0
for(each of replyButton){
    each.setAttribute('id', +i)
    i++
    
    each.addEventListener('click', function(e){
        console.log(e.target.id)
        let replyCommentEach = document.getElementById('reply-dropdown_#'+e.target.id)
        replyCommentEach.classList.toggle('-visible')
        console.log(replyCommentEach)
    })            
}            

// for(item in reportFlag){
//     item.addEventListener('click', function(){
//         item.innerHTML ="<img class='subicons' src='{% static 'images/flag_checked.png' %}' alt='' srcset=''> Report"    
//     })
// }


// images
const addImageTab = document.querySelector('#post-option-images')
const addImageDiv = document.querySelector('#create_thread_image')

addImageTab.addEventListener('click', function(){
    addImageDiv.classList.toggle('title-box')
})            


const imageButton = document.querySelector('#image_input_button')
const imageInput = document.querySelector('#image_input')

imageButton.addEventListener('click', function(){
    imageInput.click()
})            







// const sortbyNew = document.querySelector('#sortNew')
// const sortbyBest = document.querySelector('#sortBest')

