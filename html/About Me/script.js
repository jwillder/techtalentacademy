// Date & Time
function dateTime() {
  document.getElementById("datetime").innerHTML = new Date();
}

// 6 Times Table
function sixTimesTable() {
  browsertext = ""
  consoletext = "AH SO YOU CHECK THE CONSOLE!\nFEAST ON THE 6 TIMES TABLE AS YOUR REWARD\n"
  for (let i = 1; i < 13; i++) {
    text = i + " x 6 = " + i*6
    browsertext += text + "<br>";
    consoletext += text + "\n";
  }
  document.getElementById("sixtimestable").innerHTML = browsertext;
  console.log(consoletext);
}

// Voting Age Calculator
function votingAgeCalculator() {
  let age = document.getElementById("age").value;

  if (age == "" ) {
    document.getElementById("votingresult").innerHTML = "Oops, you didn't enter an age!";
  }
  else if (age >= 120) {
    document.getElementById("votingresult").innerHTML = "I highly doubt you are " + age + " years old.";
  }
  else if (age >= 18) {
    document.getElementById("votingresult").innerHTML = "The responsibilites of adulthood weigh heavily on your shoulders. Vote to your hearts content.";
  }
  else if (age>=16) {
    document.getElementById("votingresult").innerHTML = "Och aye, you can vote in Scotland!";
  }
  else if (age < 16) {
    document.getElementById("votingresult").innerHTML = "Sorry kiddo, you're too young to vote.";
  }
  else {
    document.getElementById("votingresult").innerHTML = "Numbers my friend, I only understand numbers!";
  }
}

// Hello
function hello() {
  let firstname = document.getElementById("firstname").value;
  let lastname = document.getElementById("lastname").value;

  if (firstname == "" || lastname == "") {
    document.getElementById("hello").innerHTML = "Gonna need you to enter a first name AND a last name, buddy.";
  }
  else {
    document.getElementById("hello").innerHTML = "Well met " + firstname + " " + lastname + ".";
  }
}