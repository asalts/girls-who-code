var wordsList = [];

function init() {
  // Load the words from the dictionary text file to wordsList
  var wordsFile = "https://raw.githubusercontent.com/GirlsFirst/SIP-2017/master/Unit2_Applications/dictionary-attack/dictionary.tit?token=ADcVhZjRMd86ZdhPE2jVvIaJdQdzLA6Yks5YvvVSwA%3D%3D";
  $.get(wordsFile, function(data) {
    document.getElementById("btnSubmit").disabled = true;
    wordsList = data.split('\n');
    document.getElementById("btnSubmit").disabled = false;
  });
}

window.onload = init;

/* ADD YOUR CODE BELOW */
function checkPassword()
{
  var password = document.getElementById("pw");

  var message = "";

  for (var i = 0; i < wordsList.length; i++)
  {
    if (password.value == wordsList[i])
    {
      i = wordsList.length;
      message = "Your password is a match. It is not safe.";
    }
  }

  if (message == "")
  {
    message = "Your password is not a match. It is safe.";
  }

  window.alert(message);
}
