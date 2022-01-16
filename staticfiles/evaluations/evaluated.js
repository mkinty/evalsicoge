console.log('Hello World Evaluation')
const url = window.location.href
const evaluationBox = document.getElementById('evaluation-box')
const resultBox = document.getElementById('result-box')

$.ajax({
  type: 'GET',
  url: `${url}data/`,
  success: function (response){
//  console.log(response)
  const data = response.data
//  console.log(data)
  data.forEach(el => {
    for (const [question, answers] of Object.entries(el)){
      evaluationBox.innerHTML += `
        <hr>
        <div class="mb-2">
          <b>${question}</b>
        </div>
      `
      answers.forEach(answer => {
      let type = "radio"
      let ans = 'ans'
      if (answer == "saisir text"){
        type = "text"
        ans = "textAns"
        answer = ""
      } else
      if (answer == "saisir date") {
        type = "date"
        ans = "textAns"
        answer = ""
      }
      evaluationBox.innerHTML += `
        <div>
          <input type="${type}" class="${ans}" id="${question}-${answer}" name="${question}" value="${answer}">
          <label for="${question}">${answer}</label>
        </div
      `
      })
    }
  })
  },
  error: function(error){
  console.log(error)
  }
})

const evaluationForm = document.getElementById('evaluation-form')
const csrf = document.getElementsByName('csrfmiddlewaretoken')


const sendData = () => {
  const elementsText = [...document.getElementsByClassName("textAns")]
  const elements = [...document.getElementsByClassName("ans")]
  const data = {}
  data['csrfmiddlewaretoken'] = csrf[0].value
  elementsText.forEach(el => {
    data[el.name] = el.value
  })
  elements.forEach(el => {
    if (el.checked) {
      data[el.name] = el.value
    } else {
        if (!data[el.name]) {
          data[el.name] = null
        }
    }
  })
  $.ajax({
    type: 'POST',
    url: `${url}save/`,
    data: data,
    success: function(response) {
//      console.log(response)
      const results = response.results
      console.log(results)
      evaluationForm.classList.add('not-visible')
      results.forEach(res => {
        const resDiv = document.createElement('div')
        for (const [question, resp] of Object.entries(res)){
//          console.log(question)
//          console.log(resp)
//          console.log("*******")
          resDiv.innerHTML = question
          const cls = ['container', 'p-3', 'text-light', 'h3']
          resDiv.classList.add(...cls)
          if (resp=='not answered') {
            resDiv.innerHTML += ' : pas de réponse'
            resDiv.classList.add('bg-danger')
          } else {
              const answer = resp['answered']

              resDiv.classList.add('bg-success')
              resDiv.innerHTML += ` : ${answer}`
            }
        }
//        const body = document.getElementsByTagName('body')[0]
//        body.append(resDiv)
          resultBox.append(resDiv)
      } )
    },
    error: function(error) {
      console.log(error)
    }
    })
}

evaluationForm.addEventListener('submit', e => {
  e.preventDefault()

  sendData()
})