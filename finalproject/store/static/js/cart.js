var updateBtn = document.getElementsByClassName('update-cart')

for(var i = 0; i < updateBtn.length; i++){
    updateBtn[i].addEventListener("click", function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId, 'action:', action)

        console.log('USER:', user)
        if(user === 'AnonymousUser'){
            console.log('Not logged in')
        } else{
            updateUserOrder(productId, action)
        }
    })
}

function updateUserOrder(productID, action){
    var url= 'update/'

    fetch(url, {
        method:"POST",
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken' : csrftoken
        },
        body:JSON.stringify({'productId': productId, 'action': action})
    })

    .then((response) =>{
        return response.json()
    })

    .then((data) =>{
        console.log('data:', data)
        location.reload()
    })
}