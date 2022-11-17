const td = new Date();
const dates = document.querySelectorAll('.div2');
const addContentDiv = document.getElementById('addContentID');
const addBtn = document.getElementById('btnAddRound');
console.log(addContentDiv)

for(const d of dates) {

    var date = new Date(d.innerHTML);
    var diff = new Date(td - date);

    var diffDays = Math.floor(diff /(1000*3600*24));
    if (diffDays === 0) {
        d.innerHTML = 'Idag'
    } else if (diffDays === 1) {
        d.innerHTML = 'Igår'
    } else if (diffDays === -1) {
        d.innerHTML = "Imorgon"
    } else if (diffDays <= 0) {
        d.innerHTML = "om " + diffDays.toString().slice(1) + " dagar"
    } else {
        d.innerHTML = diffDays + " dagar sen";
    }
}


function addContent() {
    if (addContentDiv.style.display === "none") {
        addContentDiv.style.display = "flex";
        addContentDiv.style.position = "sticky"
        addContentDiv.style.top = "0px"
        addBtn.style.display = "none";
        document.getElementById('textInput').focus();
    } else {
        addContentDiv.style.display = "none"
        addBtn.style.display = "block"
    }
}


addBtn.addEventListener('click', addContent);



