const tapContainer = document.querySelector('.about');
const flex_Container = document.querySelectorAll('.contents_container');
const taps = document.querySelectorAll('.about > span');


function openCity(e){
    let elem = e.target;
    
    for (var i = 0; i < flex_Container.length; i++) {
        flex_Container[i].classList.remove('active');
        taps[i].classList.remove('on');
    }
    
    if(elem.matches('[class="nick_name"]')){
        
        flex_Container[0].classList.add('active');
        taps[0].classList.add('on');
        
    }else if(elem.matches('[class="book_mark"]')){
        
        flex_Container[1].classList.add('active');
        taps[1].classList.add('on');
        
    }
    
}


tapContainer.addEventListener('click', openCity);