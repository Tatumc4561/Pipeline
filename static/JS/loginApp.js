const profileOnly = document.querySelectorAll('.profile-only')
const reportFlag = document.querySelectorAll('.report-flag')
const replyButton = document.querySelectorAll('.reply-button')
const replyComment = document.querySelectorAll('.comment-reply-dropdown')


// load profile only content on page load
for(el of profileOnly){
    el.style = "visibility: visible;"
}

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




// const sortbyNew = document.querySelector('#sortNew')
// const sortbyBest = document.querySelector('#sortBest')

// for(item in reportFlag){
//     item.addEventListener('click', function(){
//         item.innerHTML ="<img class='subicons' src='{% static 'images/flag_checked.png' %}' alt='' srcset=''> Report"
//     })
// }

