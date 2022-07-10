
$(".ajax_form").submit(function(e){
    e.preventDefault();
    var action_url = $(this).attr("action")
    var formData = new FormData($(this).get(0));
    $.ajax({
        type: "POST",
        url: action_url,
        data: formData,
        contentType: false,
        processData: false,
        success: function(response){
            if ("answer" in response){
                document.querySelector('.ajax_answer').innerHTML = "<b>Form answer</b></br>"
                for (let key in response["answer"]) {
                    document.querySelector('.ajax_answer').innerHTML += key + ": " + response["answer"][key] + "</br>"
                }
            }
        }
    })
})