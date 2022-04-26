
function toggleAuthors() {
  const li = document.getElementById('list-authors')
  if (li.style.display == 'none') {
    li.style.display = null
  } else {
    li.style.display = 'none'
  }
}

function submitPost() {
  let form = document.getElementById("new-post-form");
  let textEditor = document.getElementById('text-editor')
  form.submit()
}

function toggleComment() {
  const commentForm = document.getElementById('comment-form')
  if (commentForm.style.display == 'none') {
    commentForm.style.display = null
  } else {
    commentForm.style.display = 'none'
  }
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
  toggleComment()
}
