
function toggleItem(itemId) {
  const item = document.getElementById(itemId)
  if (item.style.display == 'none') {
    item.style.display = null
  } else {
    item.style.display = 'none'
  }
}


function submitPost() {
  let form = document.getElementById("new-post-form");
  let textEditor = document.getElementById('text-editor')
  form.submit()
}


function addCommentToCommentList() {
  let commentTextArea = document.getElementById('comment-text')
  let ul = document.getElementById('commentList')
  let li = document.createElement('li')
  let div1 = document.createElement('div')
  let div2 = document.createElement('div')
  div1.className = "card mt-2"
  div1.style.width = "100%"
  div2.className = "card-body"
  div1.appendChild(div2)
  li.appendChild(div1)
  div2.appendChild(document.createTextNode(commentTextArea.value))
  ul.appendChild(li)
  toggleItem('comment-form')
}
