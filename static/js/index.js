// I will be using XMLHttpRequests to bring pages into
// index.html

// data to div function
const dataToDiv = (data, div) => {
  div.innerHTML = data
}

// the XMLHttpRequest function to get the view
const getPage = ( (url, func, target) => {
  const xhr = new XMLHttpRequest()
  xhr.open('GET', url, true)
  xhr.onload = () => {
    xhr.readyState === 4 && xhr.status === 200
      ? func(xhr.responseText, target)
      : console.log(xhr.statusText)
  }
  xhr.onerror = () => console.log('error')
  xhr.send()
})


// page specific javascript
const pageLinks = document.getElementsByName('page_link')
const formLinks = document.getElementsByName('form_link')
const pageDiv = document.getElementById('ajax')
const formDiv = document.getElementById('form')

// put click event listeners on the pages
pageLinks.forEach(link => {
  const url = link.getAttribute('url')
  link.addEventListener('click', () => {
  console.log('hey')
    getPage(url, dataToDiv, pageDiv)
  })
})

// put click event listeners on the forms
formLinks.forEach(link => {
  const url = link.getAttribute('url')
  link.addEventListener('click', () => {
  console.log('hey')
    getPage(url, dataToDiv, formDiv)
  })
})

// set up new contact as default value
const contactList = document.getElementById('contact_list').getAttribute('url')
const contactCreate = document.getElementById('contact_create').getAttribute('url')

getPage(contactList, dataToDiv, pageDiv)
getPage(contactCreate, dataToDiv, formDiv)
