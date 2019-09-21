var app = new Vue({
    el: '#projet',
    data: {
        liengithub: null,
        succes: false,
        error: false,
    }, 
    mounted: function() {
        //this.onload()
        this.actualiser()
    },
    delimiters: ["${", "}"],

    methods: {
        actualiser: function(){
            new Toast({message: 'Welcome!, Entrer le lien de votre projet et valider.'});
            this.succes= false
            this.error= false
        },
        subliens: function(keyprojet){
            console.log(keyprojet)
            axios.defaults.xsrfCookieName = 'csrftoken'
            axios.defaults.xsrfHeaderName = 'X-CSRFToken'
            let data = JSON.stringify({
            
                liengithub: this.liengithub,
                projetkey: keyprojet,
                

            })
            axios.post('/sendprojet', data, {
            headers: {
                'Content-Type': 'application/json',
            }
        })
        .then((response) => {

            console.log(response.data)
            if (response.data.statut = "error"){
                new Toast({
                    message: response.data.message,
                    type: 'danger'
                  });
            }else{
                new Toast({
                    message: response.data.message,
                    type: 'danger'
                  });
            }
            this.liengithub = null
            
        })
        .catch((err) => {
            
            console.log(err);
        })
        },
    }
})