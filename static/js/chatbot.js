window.addEventListener('keypress', function (e) {
    if (e.keyCode == 13 ) {
        e.preventDefault();
        ajaxFunction();
    }
}, false);
$(document).ready(function(){
        document.getElementById('summit').onclick = function() {
          ajaxFunction();
    }
});

function ajaxFunction() {
    var stringtext = document.getElementById('text').value;

    $.ajax({
        url: '/translate',
        data: stringtext.toString(),
        type: 'POST',
        contentType: false,
        cache: false,
        processData: false,
        success: function (response) {
          console.log("nnnn");
            console.log(response.status);
            var temp = JSON.parse(response)
            var str_me = temp["me"]
            var str_bot = temp["bot"]
            document.getElementById('text').value ="";


            var div = document.createElement("DIV");
            var li = document.createElement("LI");
            var span = document.createElement("SPAN")
            var img = document.createElement("IMG");
            img.setAttribute("class","img");
            img.setAttribute("src","./static/images/person_1.png");
            span.innerHTML=str_me;
            li.appendChild(span);
            li.appendChild(img);
            li.setAttribute("class","me");
            div.appendChild(li);
            div.setAttribute("class","message_chat")
            document.getElementById("bot").appendChild(div);


            var li_bot = document.createElement("LI");
            var span_bot = document.createElement("SPAN");
            var img_bot = document.createElement("IMG");
            img_bot.setAttribute("class","img");
            img_bot.setAttribute("src","./static/images/bot_1.png");
            span_bot.innerHTML=str_bot;
            li_bot.appendChild(img_bot);
            li_bot.appendChild(span_bot);
            li_bot.setAttribute("class","bot");
            document.getElementById("bot").appendChild(li_bot);

            console.log(str_me);

        },
        error: function (error) {
            console.log(error);
        }
    });
}