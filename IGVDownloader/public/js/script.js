const dwnBtn = document.getElementById('dwn-btn')
const inpUrl = document.getElementById('inp-url')

function getVideoSource(shortCode) {
    if (shortCode.search('https://www.instagram.com') != -1) {
        shortCode = shortCode.split('/').reverse()[1]
    }


    console.log(shortCode)
    axios.get('/api/video/' + shortCode)
    .then(function (response) {
        console.log(response)
        createHtml(response.data)
    })
    .catch(function (error) {
        document.getElementById('search-message').innerHTML = `Bir hata meydana geldi <a href="/shortcode"> shortcode'u </a> ya da url'yi kontrol ediniz.`
    })
}

function createHtml(source){
    var a = `
    <a href=${source} target="_blank">
        <button id="dwn-btn" class="btn" style="margin-top: 5px; background-color:red; color:white;">Videoyu İndir</button> 
    </a>`;
    
    document.getElementById("empty-span").innerHTML = a
}


dwnBtn.addEventListener('click', e=> {
    e.preventDefault()
    document.getElementById('search-message').innerHTML = " "
    url = inpUrl.value;
    getVideoSource(url)
})