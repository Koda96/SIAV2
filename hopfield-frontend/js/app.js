$(document).ready(function(e){
    

    $("#form-add").on("submit", function(ev) {
        ev.preventDefault();

        if ($("#file").val() == "") {
            alert("Primero subí una imagen para reconocer.")
            return;
        }

        $("#img-prev").addClass("d-none");
        $("#img-proc").addClass("d-none");
        $("#loader").removeClass("d-none");
        $("#form-container").addClass("d-none");
        


        $.ajax({
            type: 'POST',
            url: 'http://127.0.0.1:4455/upload-image',
            data: new FormData(this),
            dataType: 'json',
            contentType: false,
            cache: false,
            enctype: 'multipart/form-data',
            processData:false,
            success: function(respuesta) {
                if(respuesta.error == 0) {
                    console.log(respuesta);
                    
                    $.ajax({
                        type: 'GET',
                        url: 'http://127.0.0.1:4455/process',
                        dataType: 'json',
                        success: function(respuesta) {
                            if(respuesta.error == 0) {
                                console.log(respuesta);
                                console.log(respuesta.dir);
                                
                                $("#loader").addClass("d-none");
                                //debugger;
                                $("#imgProcesada").removeAttr("src");
                                //debugger;
                                //document.getElementById("imgProcesada").src = respuesta.dir;
                                $("#imgProcesada").attr("src", respuesta.dir + '?' + Math.random());
                                $("#img-proc").removeClass("d-none");
                                
                                $("#file").val("");

                                $("#form-container").removeClass("d-none");

                                
                                
            
                            } else {
                                console.log(respuesta);
                            }
            
            
                        },
                        error: function(respuesta) {
                            console.log(respuesta);
                        }
                    });

                } else {
                    console.log(respuesta);
                }


            },
            error: function(respuesta) {
                console.log(respuesta);
            }
        });
        
    });

    





    
});

function prevImg(input) {
    document.getElementById('imgPreview').src = window.URL.createObjectURL(input.files[0]);
    $("#img-proc").addClass("d-none");
    $("#img-prev").removeClass("d-none");

}