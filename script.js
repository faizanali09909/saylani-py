console.log("Javascript Connected");

function handleClick() {
  let marks = document.getElementById("marksVal")["value"];
  let result = document.getElementById("result");
  if (marks > 100) {
    result.innerHTML = "Wrong marks!";
  } else if (marks >= 90) {
    result.innerHTML = "You have passed with distinction!";
  } else if (marks >= 60) {
    result.innerHTML = "You have passed!";
  } else {
    result.innerHTML = "You have failed!";
  }
}