$(document).ready(function() {


    $( document ).tooltip({
      position: {
        my: "center bottom-20",
        at: "center top",
        using: function( position, feedback ) {
          $( this ).css( position );
          $( "<div>" )
            .addClass( "arrow" )
            .addClass( feedback.vertical )
            .addClass( feedback.horizontal )
            .appendTo( this );
        }
      }
    });

  	$( '#datepicker_reservation_from' ).datepicker({
  		minDate: 0,
	  	beforeShowDay: SetDayStyle,
	  	defaultDate: "",
	  	changeMonth: false,
	  	numberOfMonths: 3,
	  	onClose: function( selectedDate ) {
	  		if (selectedDate) {$( "#datepicker_reservation_to" ).datepicker( "option", "minDate", selectedDate );}
	  	}
	  });
	  $( '#datepicker_reservation_to' ).datepicker({
	  	minDate: 0,
	  	beforeShowDay: SetDayStyle,
	  	defaultDate: "",
	  	changeMonth: false,
	  	numberOfMonths: 3,
	  	onClose: function( selectedDate ) {
	  		if (selectedDate) {$( "#datepicker_reservation_from" ).datepicker( "option", "maxDate", selectedDate );}
	  	}
	  });

    function SetDayStyle(date) {

    	var dp_avail_dates = datepicker_reservation_available_rates;
        var enabled = false;
    	var toolTip = "";
    	var cssvacancy = "novacancy";

    	for (var key in dp_avail_dates) {
            var d = new Date(key);
            if (d.getUTCDate() == date.getUTCDate() &&
                d.getUTCMonth() == date.getUTCMonth() &&
                d.getUTCFullYear() == date.getUTCFullYear()) {
                toolTip = dp_avail_dates[key]["rate"];   
        		cssvacancy = dp_avail_dates[key]["style"];
                enabled = true; 
        		break;
        	}
    	}
    	return new Array(enabled, cssvacancy, toolTip);
	}
});
