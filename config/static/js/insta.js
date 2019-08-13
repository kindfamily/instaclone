(function () {
    const header = document.querySelector('#header');
    const side_box = document.querySelector('.side_box');
    const contents = document.querySelector('.contents_box');
    const csrf_token = document.getElementById('csrf_token');
    
    function eventHandler(e) {
        let elem = e.target;

        while (!elem.getAttribute('data-name')) {
            elem = elem.parentNode;

            if (elem.nodeName === 'BODY') {
                elem = null;
                return;
            }
        }

        if(elem.matches('[data-name="heartbeat"]')){

            var pk = elem.getAttribute('name');
            console.log("pk : " + pk);
            
            console.log('하트');
            $.ajax({
              type: "POST",
              url: "/post/like",
              data: {'pk': pk, 'csrfmiddlewaretoken': csrf_token.value },
              dataType: "json",
              success: function(response){
     
                $("#count-"+pk).html("좋아요 "+response.like_count+"개");

                var users = $("#like-user-"+pk).text();

                if(users.indexOf(response.nickname) != -1){
                  if(response.like_count == 0){
                    $("#like-user-"+pk).text("");
                  }else{
                  $("#like-user-"+pk).text(users.replace(response.nickname, ""));
                  }
                  $("div.sprite_heart_icon_outline[name="+pk+"]").toggleClass('on off');
                }else{
                  $("#like-user-"+pk).text(response.nickname+users);
                  $("div.sprite_heart_icon_outline[name="+pk+"]").toggleClass('off on');
                }
              },
              error: function(request, status, error){ 
                alert("로그인이 필요합니다.");
                window.location.replace("/accounts/login/");
              },
            });
            
        }else if(elem.matches('[data-name="more"]')){
            console.log('more');
            
            elem.classList.toggle('on');

        }else if(elem.matches('[data-name="share"]')){


            console.log('공유');
        }
        // console.log(elem);

        // console.log(elem.getAttribute('data-name') + 'clicked! ');

        
    }


    function scrollfunc(){

        if (pageYOffset >= 10) {
            header.classList.add('on');
            side_box.classList.add('on');
            resizefunc();

        } else {

            header.classList.remove('on');
            side_box.classList.remove('on');

            // side_box.style.right = '0px';
            side_box.removeAttribute('style');

            console.log('no func!');

        }
    }
    
    window.addEventListener('scroll',scrollfunc);
    contents.addEventListener('click', eventHandler);


})();