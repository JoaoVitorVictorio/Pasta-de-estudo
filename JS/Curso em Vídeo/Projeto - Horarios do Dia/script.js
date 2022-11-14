function carregar(){
    var msg = window.document.getElementById('msg')
    var img = window.document.getElementById('imagem')
    var data = new Date()
    var hora = data.getHours()
    //var hora = 22
    msg.innerHTML = `Agora são: ${hora} horas.`
    if (hora >= 0 && hora < 12){
        img.src = 'imagens/manhã.png'
        document.body.style.background = '#6BBFF8'
    } else if (hora >= 12 && hora <= 18){
        img.src = 'imagens/tarde.png'
        document.body.style.background = '#D08955'
    } else{
        img.src = 'imagens/noite.png'
        document.body.style.background = '#5F4C73'
    }
}


