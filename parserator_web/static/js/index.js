/* TODO: Flesh this out to connect the form to the API and render results
   in the #address-results div. */
"use strict"
$(document).ready(function () {
  function addressRequest () {
    $.ajax({
      type: "GET",
      url: "/api/parse/",
      data: {'address': $('#address').val()},
      success: function (result) {

        $("#address-results").removeAttr('style')
        //in case first entry was an error
        $("h4").text("Parse Results").attr("style", "color: black;")
        //to prevent additional requests to concatenate previous request
        $("#parse-type").empty()
        $(".table tbody").empty()

        $("#parse-type").text(result.type)
        $.each(result.components, function (key, value) {
          var newRow = '<tr><td>'+key+'</td><td>'+value+'</td></tr>'
          $(".table tbody").append(newRow)
        })
      },  
      error: function (error) {
        $("#address-results").removeAttr('style')
        $("#parse-type").empty()
        $(".table tbody").empty()
        $("h4").text(error.responseJSON.detail).attr("style", "color: red;")
      }
    })
  }
  $('#submit').click(function (e) {
    e.preventDefault()
    addressRequest()
    e.target.blur()
  })
})

