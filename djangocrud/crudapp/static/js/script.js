// alert('1')

const modal=document.getElementById('quest')

function openModal(){
    modal.classList.remove('modal-hidden');
    // alert('opening modal');
}

function removeModal() {
    modal.classList.add('modal-hidden');
    // alert('removing modal');
}