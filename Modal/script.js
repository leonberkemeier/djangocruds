// alert('1')

let modal = document.getElementById('modal')

function openModal(){
    modal.classList.remove('modal-hidden');
    // alert('opening modal');
}

function removeModal() {
    modal.classList.add('modal-hidden');
    // alert('removing modal');
}