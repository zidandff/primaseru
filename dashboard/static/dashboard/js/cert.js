let formRaport = $(".form-cert");

for (let i = 0; i < formRaport.length; i++) {
  let form = $(`#${formRaport[i].id}`);
  form.on('change', function() {

    $.ajax({
      url: `/d/sertifikat/verified/`,
      type: "POST",
      data: form.serialize(),
      dataType: 'json',
      success: () => {

        $("#alert-raport-berhasil").removeClass("d-none")
        setTimeout(function() {
          $("#alert-raport-berhasil").addClass("d-none")
        }, 3000);

      },
    });

  });

}
