
var bartOne = "Great! So, is the buffet for a: party, wedding, function or corporate-event?";
var eventParty = "A party? Woohoo! <br> How many guests will be there?";
var eventWedding = "A wedding? Congratulations!<br>How many guests will be there?";
var eventFunct = "I can sort that out for you!<br>How many guests will be there?";
var eventCorporate = "Let's impress the boss!<br>How many delegates will be there?";

function startBart() {
    $('#chatbox').html(bartOne);
    $('#startbart').hide();
    $('#partybart').show();
    $('#weddingbart').show();
    $('#functionbart').show();
    $('#corporatebart').show();
}

function eventBart(event) {
    switch(event) {
        case 'party':
            $('#chatbox').html(eventParty);
            $('#partybart').hide();
            $('#weddingbart').hide();
            $('#functionbart').hide();
            $('#corporatebart').hide();
            $('#guests').show();
            $('#guestsbart').show();
            break;
        case 'wedding':
            $('#chatbox').html(eventWedding);
            $('#partybart').hide();
            $('#weddingbart').hide();
            $('#functionbart').hide();
            $('#corporatebart').hide();
            $('#guests').show();
            $('#guestsbart').show();
            break;
        case 'funct':
            $('#chatbox').html(eventFunct);
            $('#partybart').hide();
            $('#weddingbart').hide();
            $('#functionbart').hide();
            $('#corporatebart').hide();
            $('#guests').show();
            $('#guestsbart').show();
            break;
        case 'corporate':
            $('#chatbox').html(eventCorporate);
            $('#partybart').hide();
            $('#weddingbart').hide();
            $('#functionbart').hide();
            $('#corporatebart').hide();
            $('#guests').show();
            $('#guestsbart').show();
            break;
        default:
            break;
    }
}

function guestsBart() {
    $('#guests').hide();
    $('#guestsbart').hide();
    minGuests = $('#minguests').val();
    maxGuests = $('#maxguests').val();
    var eventGuests = "Right, so between " + minGuests + " and " + maxGuests + " guests will be attending.<br>" +
        "Are any of them: vegan, vegetarian or pescatarian?"
    $('#chatbox').html(eventGuests);
}