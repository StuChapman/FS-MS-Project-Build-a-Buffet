
var bartOne = "Great! So, is the buffet for a: party, wedding, function or corporate-event?";
var eventParty = "A party? Woohoo! <br> How many guests will be there?";
var eventWedding = "A wedding? Congratulations!<br>How many guests will be there?";
var eventFunct = "I can sort that out for you!<br>How many guests will be there?";
var eventCorporate = "Let's impress the boss!<br>How many delegates will be there?";
var guestType

function startBart() {
    $('#chatbox').html(bartOne);
    $('#startbart').hide();
    $('#event').show();
}

function eventBart(event) {
    switch(event) {
        case 'party':
            $('#event').hide();
            $('#guests').show();
            $('#chatbox').html(eventParty);
            guestType = "guests"
            break;
        case 'wedding':
            $('#event').hide();
            $('#guests').show();
            $('#chatbox').html(eventWedding);
            guestType = "guests"
            break;
        case 'funct':
            $('#event').hide();
            $('#guests').show();
            $('#chatbox').html(eventFunct);
            guestType = "guests"
            break;
        case 'corporate':
            $('#event').hide();
            $('#guests').show();
            $('#chatbox').html(eventCorporate);
            guestType = "delegates"
            break;
        default:
            break;
    }
}

function guestsBart() {
    minGuests = $('#minguests').val();
    maxGuests = $('#maxguests').val();
    if (parseInt(maxGuests) < parseInt(minGuests) || parseInt(minGuests) == 0 || minGuests == "") {
        var guestError = "Oops! Can you check those numbers and try again please?"
        $('#chatbox').html(guestError);
        return;
    } 
    if (parseInt(maxGuests) == parseInt(minGuests) || maxGuests == "") {
        var eventGuests = "Right, so " + minGuests + " " + guestType + " will be attending.<br>" +
            "Are any of them: vegan, vegetarian or pescatarian?"
    } else {
         var eventGuests = "Right, so between " + minGuests + " and " + maxGuests + " " + guestType + " will be attending.<br>" +
        "Are any of them: vegan, vegetarian or pescatarian?"
    }
    $('#guests').hide();
    $('#diet').show();
    $('#chatbox').html(eventGuests);
}