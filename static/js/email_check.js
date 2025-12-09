function emailCheck() {
    $(document).ready($("#email").on({
        change: function () {
            $.get("http://127.0.0.1:5000/api/email/", { data: $(this).val() }, (response) => {
                if (response) {
                    $("#lbl").text(response)
                    $(this).css("border", "solid 1px red")
                }


            })
        }

    }))
}
export default emailCheck