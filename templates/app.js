
  function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    var year = document.getElementById("year"); //get the value of the year given
    var month = document.getElementById("month");   // get the value of the month
    var estPrice = document.getElementById("uiEstimatedPrice");  //get the estimated price

    //var url = "http://127.0.0.1:5000/predict_kero_price"; //Use this if you are NOT using nginx
    var url = "/api/predict_kero_price"; // Use this if  you are using nginx

    //send the data to the serverside for execution
    //make a post request to the server endpoint
    $.post(url, {
        year: parseInt(year.value), //get the year
        month: month.value  //get the month
    },function(data, status) {
        console.log(data.estimated_price);
        estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Naira</h2>";
        console.log(status);
    });
  }

  //function to get locations on page load
  function onPageLoad() {
    console.log( "document loaded" );
    //var url = "http://127.0.0.1:5000/month_names"; // Use this if you are NOT using nginx
    var url = "/api/month_names"; // Use this if  you are using nginx

    //make a get request to the server end point
    $.get(url,function(data, status) {
        console.log("got response for get_location_names request");
        if(data) {
            var months = data.months; //get the locations
            var uiMonth = document.getElementById("month"); //get the selected location by the user
            $('#month').empty(); //remove any selected month after execution

            for(var i in months) {                 // this is to get the complete month from the url
                var opt = new Option(months[i]);  //create a new objet Option and index each location
                $('#month').append(opt);       //append all the locations gotten to the select tag
            }
        }
    });
  }
  
  window.onload = onPageLoad;