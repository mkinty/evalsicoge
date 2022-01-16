console.log('Hello world !')

const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalBody = document.getElementById('modal-body-confirm')
const startBtn = document.getElementById('start-button')
const url = window.location.href


modalBtns.forEach(modalBtn => modalBtn.addEventListener('click', () => {
  const pk = modalBtn.getAttribute('data-pk')
  const evaluation = modalBtn.getAttribute('data-evaluation')
  const numQuestions = modalBtn.getAttribute('data-questions')
  modalBody.innerHTML = `
    <div className="h5 mb-3"> Voulez-vous répondre à ces "<b>${numQuestions}</b>" questions pour nous aider à améliorer
     la "<b> ${evaluation}</b>" ?</div>
    <div className="text-muted">Ça ne vous prendra que que 5 minutes.</div>
  `
  startBtn.addEventListener('click', () => {
    window.location.href = url + pk
  })
  console.log(pk)
  console.log(evaluation)
  console.log(numQuestions)
}))