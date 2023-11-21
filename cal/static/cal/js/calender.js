document.addEventListener("DOMContentLoaded", function () {
    const buttonCount = 100;

    const buttonList = document.getElementById("button-list");
    for (let i = 1; i <= buttonCount; i++) {
      const button = document.createElement("button");
      button.textContent = i;
      buttonList.appendChild(button);
    }
  });