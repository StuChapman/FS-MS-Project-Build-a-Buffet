
var bartOne = "Great! So, is the buffet for a: party, wedding, function or corporate-event?";
var eventParty = "A party? Woohoo! <br> How many guests will be there?";
var eventWedding = "A wedding? Congratulations!<br>How many guests will be there?";
var eventFunct = "I can sort that out for you!<br>How many guests will be there?";
var eventCorporate = "Let's impress the boss!<br>How many delegates will be there?";
var guestError = "Oops! Can you check those numbers and try again please?"
var dietBartHot = "<br>What proportion of the menu would you like to be served hot?"
var hotFood = " hot food in this buffet, excellent.<br>Nearly finished - same question for allergy free..."
var bartFinish = "Awesome! That's everything I need.<br>Have a check through the info you've given me then hit the Finish button below to see your recommended buffet..."

var guestType
var minGuests
var maxGuests
var hotProportion
var allegryProportion

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

function dietBart() {
    veganGuests = $('#veganGuests').val();
    veggieGuests = $('#veggieGuests').val();
    pescGuests = $('#pescguests').val();
    if ((parseInt(veganGuests*1) + parseInt(veggieGuests*1) + parseInt(pescGuests*1)) > parseInt(minGuests*1)) {
        $('#chatbox').html(guestError);
        return;
    }
    if ((parseInt(veganGuests*1) + parseInt(veggieGuests*1) + parseInt(pescGuests*1)) == 0) {
        var dietBart = "No problem; there will be a nice mix of food in case anyone has a preference on the day." + dietBartHot
    } else {
         var dietBart = "Great! I'll make sure there are plenty of different choices for everyone." + dietBartHot
    }
    $('#hotfood').show();
    $('#diet').hide();
    $('#chatbox').html(dietBart);
}

function hotBart(proportion) {
    $('#hotfood').hide();
    $('#allergy').show();
    hotProportion = proportion
    $('#chatbox').html(hotProportion + hotFood);
}

function allergyBart(proportion) {
    $('#allergy').hide();
    $('#chatimgbox').hide();
    $('#finishbart').show();
    $('#chatsummary').show();
    $('#finalimgbox').show();
    allegryProportion = proportion
    $('#chatbox').html(bartFinish);
}