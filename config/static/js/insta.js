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
        
        if(elem.classList.contains("like")){ 
            var pk = elem.getAttribute('data-name');      
            $.ajax({
              type: "POST",
              url: "/post/like",
              data: {'pk': pk, 'csrfmiddlewaretoken': csrf_token.value },
              dataType: "json",
              success: function(response){
                alert(like_count);
                $("#count-"+pk).html("좋아"+response.like_count+"개");

                var users = $("#like-user-"+pk).text();

                if(users.indexOf(response.nickname) != -1){
                    
                  if(response.like_count == 0){
                    $("#like-user-"+pk).text("");
                  }else{
                  $("#like-user-"+pk).text(users.replace(response.nickname, ""));
                  }
                  $("div.sprite_heart_icon_outline[name="+pk+"]").toggleClass('off on');
                }else{
                  $("#like-user-"+pk).text(response.nickname+users);
                  // $("div.sprite_heart_icon_outline[name="+pk+"]").remove('off');  
                  $("div.sprite_heart_iconxw_outline[name="+pk+"]").toggleClass('on off');
                }
              },
              error: function(request, status, error){ 
                alert("로그인이 필요합니다.");
                window.location.replace("/accounts/login/");
              },
            });
            
        }
        
        
        if(elem.classList.contains("bookmark")){
            var pk = elem.getAttribute('data-name');
            $.ajax({
              type: "POST",
              url: "/post/bookmark",
              data: {'pk': pk, 'csrfmiddlewaretoken': csrf_token.value },
              dataType: "json",
              success: function(response){
     
               // alert("성공"); 
                var users = $("#bookmark-user-"+pk).text();

                if(users.indexOf(response.nickname) != -1){
                  if(response.bookmark_count == 0){
                    $("#bookmark-user-"+pk).text("");
                  }else{
                  $("#bookmark-user-"+pk).text(users.replace(response.nickname, ""));
                  }
                  $("div.sprite_bookmark_outline[data-name="+pk+"]").toggleClass('off on');
                }else{
                  $("#bookmark-user-"+pk).text(response.nickname+users);
                  $("div.sprite_bookmark_outline[data-name="+pk+"]").toggleClass('on off');
                }
              },
              error: function(request, status, error){ 
                // alert("실패");
                alert("로그인이 필요합니다.");
                window.location.replace("/accounts/login/");
              },
            });

        }
        
        
        // if(elem.classList.contains("delc")){    
        //     var pk = elem.getAttribute('data-name');
        //     alert('댓글삭제');
            
        //     $.ajax({
        //       type: "POST",
        //       url: "/post/delete"+pk,
        //       data: {'pk': pk, 'csrfmiddlewaretoken': csrf_token.value },
        //       dataType: "json",
        //       success: function(response){
        //           alert("성공");
        //           if(response.status){
        //               $('#comment'+pk).remove();
        //             }
        //             alert(response.message);
        //       },
        //       error: function(request, status, error){ 
                
        //         alert("실패");
        //         alert("로그인이 필요합니다.");
        //         window.location.replace("/accounts/login/");
        //       },
        //     });

        // }
        
        // if(elem.matches('[data-name="follow"]')){
            
        //     var pk = elem.getAttribute('followname');
            
        //   $.ajax({
        //     type: "POST",
        //     url: "/accounts/follow/",
        //     data: {'pk': pk, 'csrfmiddlewaretoken': csrf_token.value },
        //     dataType: "json",
        //     success: function(response){
        //       alert("성공");
        //       alert(response.message);
        //       if(response.status){
        //         $("input.follow[name="+pk+"]").val("팔로잉");
        //         $("input.follow[name="+pk+"]").toggleClass('follow-btn following-btn');
        //       }else{
        //         $("input.follow[name="+pk+"]").val("팔로우");
        //         $("input.follow[name="+pk+"]").toggleClass('following-btn follow-btn');
        //       }
        //     },
        //     error: function(request, status, error){
        //       alert("로그인이 필요합니다.");
        //       window.location.replace("/accounts/login/");
        //       // alert("code:"+request.status+"\n"+"message:"+request.responseText+"\n"+"error:"+error);
        //     }
        //   })
        // }
        
        // if(elem.matches('[data-name="more"]')){


        //     console.log('더보기');
        // }
        // console.log(elem);

        // console.log(elem.getAttribute('data-name') + 'clicked! ');

        elem.classList.toggle('on');
    }


     function scrollfunc(){
        if (pageYOffset >= 10) {
            header.classList.add('on');
            resizefunc();
            if(side_box){
                side_box.classList.add('on');
            }
        } else {
            header.classList.remove('on');
            if(side_box){
                side_box.classList.remove('on');
                side_box.removeAttribute('style');
            }
            console.log('no func!');
        }
    }



    function resizefunc(){
        if(pageYOffset >= 10){
            let calcWidth = (window.innerWidth * 0.5) + 167;
            // console.log(window.innerWidth);
            if(side_box){
                side_box.style.left =  calcWidth + "px";
            }
        }
    }

    resizefunc();

    setTimeout(function(){
        scrollTo(0,0);
    },100);

    window.addEventListener('resize',resizefunc);
    window.addEventListener('scroll',scrollfunc);
    if(contents){
        contents.addEventListener('click', eventHandler);
    }
})();